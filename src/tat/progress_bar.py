from PySide6.QtWidgets import QDialog, QWidget, QProgressBar
from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import Signal, Slot

from typing import Optional

from .ui_progress_bar import Ui_ProgressBar


class ProgressWindow(QDialog):
    cancelled = Signal()

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.__ui = Ui_ProgressBar()
        self.__ui.setupUi(self)
        self.__ui.cancelButton.clicked.connect(self.cancelled)
        self.__ui.cancelButton.clicked.connect(lambda: self.close())

    def closeEvent(self, event: QCloseEvent) -> None:
        self.cancelled.emit()

    def progress_bar(self) -> QProgressBar:
        return self.__ui.progressBar
