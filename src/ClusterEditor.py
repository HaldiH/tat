import os
from typing import Optional, Callable, Any

import cv2 as cv
import numpy as np

from PySide6.QtWidgets import QLayout, QLabel, QWidget, QGridLayout
from PySide6.QtGui import QImage, QMouseEvent, QCloseEvent, QResizeEvent, QMoveEvent, QPixmap
from PySide6.QtCore import Slot, QSize, QPoint, Qt

from .Ui_EditorWindow import Ui_EditorWindow
from . import PreviewWindow, ClusterImageEntry, LayerImageEntry
from .Utils import load_image, array2d_to_pixmap, fit_to_frame, create_cluster


class CLusterPreviewWindow(QWidget):
    def __init__(self, parent: Optional[QWidget] = None, size: QSize = QSize(600, 600), image: Optional[QImage] = None):
        super(CLusterPreviewWindow, self).__init__(parent)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.resize(size)

        self.imageLabel = QLabel("Cluster Preview", self)
        self.imageLabel.setAlignment(Qt.AlignCenter)

        layout = QGridLayout(self)
        layout.addWidget(self.imageLabel)

        if image is not None:
            self.imageLabel.setPixmap(fit_to_frame(QPixmap.fromImage(image), QSize(self.width(), self.height())))

    def update_cluster_preview(self, array: np.ndarray):
        self.imageLabel.setPixmap(fit_to_frame(array2d_to_pixmap(array, normalize=True, colormap=cv.COLORMAP_JET),
                                               QSize(self.width(), self.height())))


class ClusterEditor(PreviewWindow):
    def __init__(self, parent: Optional[QWidget], calling_image_entry: ClusterImageEntry):
        super(ClusterEditor, self).__init__(parent)
        self.ui = Ui_EditorWindow()
        self.ui.setupUi(self)
        self.ui.mergeButton.clicked.connect(self.merge)
        self.ui.applyButton.clicked.connect(self.apply_to_all)
        self.ui.resetButton.clicked.connect(self.reset)

        self.merge_callback: Optional[Callable[[list[int]], Any]] = None

        self._source_image_entries: list[LayerImageEntry] = []
        self._selected_image_entry: Optional[LayerImageEntry] = None
        self.cluster_image_entry: ClusterImageEntry = calling_image_entry
        self.applied_mergers: list[list[int]] = []
        self.cluster_array: np.ndarray = np.load(self.cluster_image_entry.array_path)

        side_length = self.height() - self.menuBar().height()
        self.cluster_preview_window = CLusterPreviewWindow(self, QSize(side_length, side_length),
                                                           load_image(self.cluster_image_entry.image_path))
        # self.cluster_preview_window.show()

        # first = True
        for i in range(self.cluster_image_entry.layer_count()):
            layer_data = self.cluster_image_entry.get_layer_data(i)
            array = np.load(layer_data.array_path)
            qim: QImage = load_image(layer_data.image_path)
            ime = LayerImageEntry(self, qim, array, f"merger {str(i)}" if layer_data.is_merger else str(i))
            ime.registerMousePressHandler(self.image_entry_click_handler)
            self.add_source_image_entry(ime)

            # if first:
            # self.set_preview_image(qim, ime)
            # first = False

    def source_layout(self) -> QLayout:
        return self.ui.scrollAreaLayersContents.layout()

    def image_preview(self) -> QLabel:
        return self.ui.imageLabel

    def register_merge_handler(self, hdl: Callable[[list[int]], Any]):
        self.merge_callback = hdl

    def image_entry_click_handler(self, sender: LayerImageEntry, event: QMouseEvent) -> None:
        assert type(sender) == LayerImageEntry
        self.set_preview_image(array2d_to_pixmap(sender.array, normalize=True).toImage(), sender)

    def resizeEvent(self, event: QResizeEvent) -> None:
        if self._selected_image_entry is None:
            return
        self.draw_preview_image(array2d_to_pixmap(self._selected_image_entry.array, normalize=True).toImage())

    def moveEvent(self, event: QMoveEvent) -> None:
        position = event.pos()
        self.cluster_preview_window.move(position - QPoint(self.cluster_preview_window.width(), 0))
        if self.cluster_preview_window.isHidden():
            self.cluster_preview_window.show()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.cluster_preview_window.close()
        self.cluster_preview_window = None

    @Slot()
    def merge(self):
        checked_entries: list[int] = []
        merger_str = ""
        merger: Optional[np.ndarray] = None
        for index, ime in enumerate(self._source_image_entries):
            if not ime.isChecked():
                continue

            merger_str += str(index) if merger is None else f"+{str(index)}"

            checked_entries.append(index)
            merger = self._source_image_entries[index].array if merger is None else merger | self._source_image_entries[
                index].array
            ime.setChecked(False)
            ime.close()

        if len(checked_entries) == 0:
            return

        for i in reversed(checked_entries):
            self._source_image_entries.pop(i)

        self.cluster_array = create_cluster([ime.array for ime in self._source_image_entries])
        self.cluster_preview_window.update_cluster_preview(self.cluster_array)

        self.applied_mergers.append(checked_entries)

        qim: QImage = array2d_to_pixmap(merger, normalize=True).toImage()

        merged_ime = LayerImageEntry(self, qim, merger, f"merger {merger_str}")
        merged_ime.registerMousePressHandler(self.image_entry_click_handler)
        self.set_preview_image(qim, merged_ime)
        self.add_source_image_entry(merged_ime)

    @Slot()
    def apply_to_all(self):
        assert self.merge_callback is not None, "The callback is not defined"
        for merger in self.applied_mergers:
            self.merge_callback(merger)
        self.applied_mergers.clear()

    @Slot()
    def reset(self):
        if len(self.applied_mergers) == 0:
            return

        self.applied_mergers.clear()

        for ime in self._source_image_entries:
            ime.close()

        self._source_image_entries.clear()

        self.cluster_array = np.load(self.cluster_image_entry.array_path)
        self.cluster_preview_window.update_cluster_preview(self.cluster_array)

        for i in range(self.cluster_image_entry.layer_count()):
            layer_data = self.cluster_image_entry.get_layer_data(i)
            array = np.load(layer_data.array_path)
            qim: QImage = load_image(layer_data.image_path)
            ime = LayerImageEntry(self, qim, array, f"merger {str(i)}" if layer_data.is_merger else str(i))
            ime.registerMousePressHandler(self.image_entry_click_handler)
            self.add_source_image_entry(ime)
            if i == 0:
                self.set_preview_image(load_image(layer_data.image_path), ime)
