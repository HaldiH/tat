from ImageEntry import ImageEntry
from PySide6.QtWidgets import QWidget


class LayerImageEntry(ImageEntry):
    def __init__(self, parent: QWidget, image, path, name):
        super(LayerImageEntry, self).__init__(parent, image, path, name)

