from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QSizePolicy, QFrame
from PySide6.QtGui import QImage, QPixmap, QColor, QMouseEvent
from PySide6.QtCore import Qt, QEvent, QSize
from typing import Callable, Final
from Utils import fit_to_frame


class ImageEntry(QWidget):
    def __init__(self, parent: QWidget, image: QImage, path: str, name: str):
        super(ImageEntry, self).__init__(parent)
        self.__selected = False
        self.__ime_layout = QVBoxLayout(self)
        self.__mouse_pressed_handlers = []
        self.setAutoFillBackground(True)
        self.__default_background_color = self.palette().color(self.backgroundRole())
        self.image_path: Final = path

        image_label = QLabel("Preview", self)
        image_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        image_label.setAlignment(Qt.AlignCenter)
        # qpix = QPixmap.fromImage(image)
        # image_label.setPixmap(qpix.scaledToHeight(image_label.height()))
        image_label.setPixmap(fit_to_frame(QPixmap.fromImage(image), QSize(image_label.width(), image_label.height())))

        name_label = QLabel(name, self)
        name_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        name_label.setAlignment(Qt.AlignCenter)

        self.__ime_layout.addWidget(image_label, alignment=Qt.AlignHCenter)
        self.__ime_layout.addWidget(name_label, alignment=Qt.AlignHCenter)

        self.setLayout(self.__ime_layout)

    def layout(self) -> QVBoxLayout:
        return self.__ime_layout

    def setSelected(self, selected: bool) -> None:
        if selected:
            self.__setBackgroundColor(Qt.gray)
            self.__selected = True
            return

        self.__setBackgroundColor(self.__default_background_color)
        self.__selected = False

    def isSelected(self) -> bool:
        return self.__selected

    def __setBackgroundColor(self, color: QColor):
        pal = self.palette()
        pal.setColor(self.backgroundRole(), color)
        self.setPalette(pal)

    def registerMousePressHandler(self, handler: Callable):
        self.__mouse_pressed_handlers.append(handler)

    def clearMousePressHandler(self):
        self.__mouse_pressed_handlers.clear()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        for hdl in self.__mouse_pressed_handlers:
            hdl(self, event)
