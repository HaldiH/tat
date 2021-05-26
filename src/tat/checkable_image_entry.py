from PySide6.QtWidgets import QWidget, QCheckBox, QSizePolicy
from PySide6.QtGui import QImage
from PySide6.QtCore import Qt

from .image_entry import ImageEntry

from typing import Optional


class CheckableImageEntry(ImageEntry):
    def __init__(self, parent: QWidget, image: QImage, name: str, image_path: str = None,
                 array_path: str = None, default_check=True):
        super(CheckableImageEntry, self).__init__(parent, image, image_path, name, array_path)

        self.__check_box = QCheckBox(self)
        self.__check_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        self.__check_box.setChecked(default_check)

        self.layout().insertWidget(1, self.__check_box, alignment=Qt.AlignHCenter)

    def isChecked(self) -> bool:
        return self.__check_box.isChecked()

    def setChecked(self, checked) -> bool:
        self.__check_box.setChecked(checked)
