import os

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

from typing import Optional, Final


class ClusterEditor(PreviewWindow):
    def __init__(self, parent: Optional[QWidget], cluster_path: str, layers_paths: [str], basename: str):
        super(ClusterEditor, self).__init__(parent)
        self.ui = Ui_EditorWindow()
        self.ui.setupUi(self)
        self.ui.mergeButton.clicked.connect(self.merge)

        self.cluster_path = cluster_path
        self.layers_paths = layers_paths
        self.output_dir: Final[str] = os.path.dirname(cluster_path)
        self.basename: Final[str] = basename
        self.image_shape: Optional[tuple] = None
        layout: QLayout = self.ui.scrollAreaLayersContents.layout()
        first = True
        i = 0
        for i in range(len(layers_paths)):
            layer_path: str = layers_paths[i]
            qim: QImage = load_image(layer_path)
            ime = SourceImageEntry(layout.parent(), qim, layer_path, str(i),
                                   f"{layer_path[0:layer_path.rfind('.')]}.npy", False)
            ime.registerMousePressHandler(self.image_entry_click_handler)
            self.add_source_image_entry(ime)

            if first:
                self.set_preview_image(qim, ime)
                first = False
        self.__layer_count = i

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
                merged = np.load(ime.array_path)
                first = False
            else:
                if merged is None:
                    raise ReferenceError
                merged |= np.load(ime.array_path)
            ime.close()
        if merged is None:
            return

        colored = apply_colormap(merged)
        self.__layer_count += 1
        merged_basename = f"{self.basename}_layer_{self.__layer_count}"
        merged_image_path = f"{os.path.join(self.output_dir, merged_basename)}.png"
        merged_array_path = f"{os.path.join(self.output_dir, merged_basename)}.npy"
        cv.imwrite(merged_image_path, colored)
        qim: QImage = load_image(merged_image_path)
        np.save(merged_array_path, merged)

        merged_ime = SourceImageEntry(self.source_layout().parent(), qim, merged_image_path, str(self.__layer_count),
                                      merged_array_path, False)
        merged_ime.registerMousePressHandler(self.image_entry_click_handler)
        self.set_preview_image(qim, merged_ime)
        self.add_source_image_entry(merged_ime)
