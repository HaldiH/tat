import numpy as np

from . import CheckableImageEntry

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage


class LayerImageEntry(CheckableImageEntry):
    def __init__(self, parent: QWidget, image: QImage, array: np.ndarray, name: str):
        super(LayerImageEntry, self).__init__(parent, image, name, default_check=False)

        self.array = array
