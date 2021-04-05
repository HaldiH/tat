from PySide6.QtWidgets import QWidget, QCheckBox, QSizePolicy
from PySide6.QtGui import QImage
from PySide6.QtCore import Qt
from ImageEntry import ImageEntry

from typing import Optional


class SourceImageEntry(ImageEntry):
    def __init__(self, parent: QWidget, image: QImage, path: str, name: str, array_path: Optional[str] = None,
                 default_check=True):
        super(SourceImageEntry, self).__init__(parent, image, path, name, array_path)
        layout = self.layout()

        self.__check_box = QCheckBox(self)
        self.__check_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        self.__check_box.setChecked(default_check)

        layout.addWidget(self.__check_box, alignment=Qt.AlignHCenter)

    def isChecked(self) -> bool:
        return self.__check_box.isChecked()

    def setChecked(self, checked):
        self.__check_box.setChecked(checked)
