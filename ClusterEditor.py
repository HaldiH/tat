from PySide6.QtWidgets import QMainWindow, QLayout, QLabel, QWidget
from PySide6.QtGui import QImage, QPixmap, QMouseEvent
from PySide6.QtCore import QSize, Slot

import numpy as np
import cv2 as cv

from clustereditor import Ui_EditorWindow
from PreviewWindow import PreviewWindow
from ImageEntry import ImageEntry
from SourceImageEntry import SourceImageEntry
from Utils import load_image, fit_to_frame, array2d_to_pixmap, apply_colormap

from typing import Optional


class ClusterEditor(PreviewWindow):
    def __init__(self, parent: Optional[QWidget], cluster_path: str, layers_paths: [str]):
        super(ClusterEditor, self).__init__(parent)
        self.ui = Ui_EditorWindow()
        self.ui.setupUi(self)
        self.ui.mergeButton.clicked.connect(self.merge)

        self.cluster_path = cluster_path
        self.layers_paths = layers_paths
        self.image_shape: Optional[tuple] = None
        layout: QLayout = self.ui.scrollAreaLayersContents.layout()
        first = True
        for i in range(len(layers_paths)):
            layer_path = layers_paths[i]
            qim = load_image(layer_path)
            ime = SourceImageEntry(layout.parent(), qim, layer_path, str(i), False)
            ime.registerMousePressHandler(self.image_entry_click_handler)
            self.register_source_image_entry(ime)

            if first:
                self.set_preview_image(qim, ime)
                first = False

    def source_layout(self) -> QLayout:
        return self.ui.scrollAreaLayersContents.layout()

    def image_preview(self) -> QLabel:
        return self.ui.imageLabel

    @Slot()
    def merge(self):
        first = True
        merged: Optional[np.ndarray] = None
        for ime in self._source_image_entries:
            ime: SourceImageEntry
            if not ime.isChecked():
                continue
            if first:
                merged = np.load(f"{ime.image_path[0:ime.image_path.rfind('.')]}.npy")
                first = False
            else:
                if merged is None:
                    raise ReferenceError
                merged |= np.load(f"{ime.image_path[0:ime.image_path.rfind('.')]}.npy")
            ime.close()
        if merged is None:
            return
        colored = apply_colormap(merged)
        cv.imwrite("merged.png", colored)
        qim = QImage("merged.png")
        merged_ime = SourceImageEntry(self.source_layout().parent(), qim, "merged.png", "merged", False)
        merged_ime.registerMousePressHandler(self.image_entry_click_handler)
        self.set_preview_image(qim, merged_ime)
        self.register_source_image_entry(merged_ime)
