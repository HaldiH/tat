import sys

from src import MainWindow

from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication()
    app.main_window = MainWindow()
    app.main_window.show()
    sys.exit(app.exec_())
