from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage, QMouseEvent

from ClusterEditor import ClusterEditor
from PreviewWindow import PreviewWindow
from ImageEntry import ImageEntry

import numpy as np

from typing import Optional, Final


class ClusterImageEntry(ImageEntry):
    def __init__(self, parent: QWidget, image: QImage, path: str, name: str, layers_paths: [str]):
        super(ClusterImageEntry, self).__init__(parent, image, path, name)
        self.layers_paths = layers_paths
        self.editorWindow: Optional[PreviewWindow] = None

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if self.editorWindow is not None and self.editorWindow.isVisible():
            self.editorWindow.activateWindow()
            return
        self.editorWindow = ClusterEditor(self.parent(), self.image_path, self.layers_paths, self.basename)
        self.editorWindow.show()
