from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QSize


def fit_to_frame(image: QPixmap, frame: QSize) -> QPixmap:
    frame_width, frame_height = frame.toTuple()
    dw = abs(image.width() - frame_width)
    dh = abs(image.height() - frame_height)
    return image.scaledToWidth(frame_width) if dw > dh else image.scaledToHeight(frame_height)


def load_image(path: str) -> QImage:
    return QImage(path)
