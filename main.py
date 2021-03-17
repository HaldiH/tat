import sys
import os

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow
from PySide6.QtCore import Slot, QEvent, QSize
from PySide6.QtGui import QPixmap, QImage

from api import Tat
from mainwindow import Ui_MainWindow
from SourceImageEntry import SourceImageEntry
from ImageEntry import ImageEntry
from Utils import fit_to_frame, load_image

import numpy as np
import cv2 as cv


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.input_directory = ""
        self.output_directory = ""

        self.__selected_image_entry = None
        self.__source_image_entries: [SourceImageEntry] = []
        self.__generated_images_entries: [ImageEntry] = []

        self.ui.buttonInputDir.clicked.connect(self.load_input_directory)
        self.ui.buttonOutputDir.clicked.connect(self.load_output_directory)
        self.ui.buttonGenerate.clicked.connect(self.generate)
        self.ui.buttonCheckUncheck.clicked.connect(self.select_deselect)
        self.ui.buttonClearGenerated.clicked.connect(self.clear_generated)

    def select_deselect(self):
        all_checked = True
        for ime in self.__source_image_entries:
            if not ime.isChecked():
                all_checked = False
                break

        for ime in self.__source_image_entries:
            ime.setChecked(not all_checked)

    def clear_generated(self):
        for ime in self.__generated_images_entries:
            ime.close()

    def image_entry_handler(self, sender: ImageEntry, event: QEvent):
        if sender is self.__selected_image_entry:
            return

        self.__selected_image_entry.setSelected(False)
        self.__selected_image_entry = sender
        sender.setSelected(True)
        self.preview_image(load_image(sender.image_path))

    def preview_image(self, image: QImage):
        self.ui.imagePreview.setPixmap(
            fit_to_frame(QPixmap.fromImage(image), QSize(self.ui.imagePreview.width(), self.ui.imagePreview.height())))

    def set_preview_image(self, image: QImage, image_entry: ImageEntry):
        self.preview_image(image)
        if self.__selected_image_entry is not None:
            self.__selected_image_entry.setSelected(False)
        self.__selected_image_entry = image_entry
        image_entry.setSelected(True)

    def clear_image_entries(self):
        for ime in self.__source_image_entries:
            ime.close()
        self.__source_image_entries.clear()

    @Slot()
    def load_input_directory(self):
        self.input_directory = QFileDialog.getExistingDirectory(parent=self)
        if len(self.input_directory) == 0:
            return

        self.clear_image_entries()

        self.ui.labelInDir.setText(f"Loaded: {self.input_directory}")

        src_layout = self.ui.scrollAreaWidgetContentsSrc.layout()
        first = True
        for entry in os.scandir(self.input_directory):
            qim = load_image(entry.path)

            ime = SourceImageEntry(src_layout.parent(), qim, entry.path, entry.name)
            ime.registerMousePressHandler(self.image_entry_handler)
            self.__source_image_entries.append(ime)
            src_layout.addWidget(ime)

            if first:
                self.set_preview_image(qim, ime)
                first = False

        if len(self.output_directory) != 0:
            self.ui.buttonGenerate.setEnabled(True)

    @Slot()
    def load_output_directory(self):
        self.output_directory = QFileDialog.getExistingDirectory(parent=self)
        if len(self.output_directory) == 0:
            return

        self.ui.labelOutDir.setText(f"Loaded: {self.output_directory}")
        if len(self.input_directory) != 0:
            self.ui.buttonGenerate.setEnabled(True)

    @Slot()
    def generate(self):
        layout = self.ui.scrollAreaWidgetContentsDst.layout()
        first = True
        for ime in self.__source_image_entries:
            ime: SourceImageEntry
            if not ime.isChecked() or not Tat.is_image(ime.image_path):
                continue

            input_basename = (lambda basename: basename[0:basename.rfind(".")])(os.path.basename(ime.image_path))
            layers = Tat.generate_layers(np.asarray(cv.imread(ime.image_path, flags=cv.IMREAD_GRAYSCALE)),
                                         self.ui.clusterCount.value(), self.ui.runCount.value(),
                                         self.ui.maxIterCount.value())
            for i in range(len(layers)):
                layer = layers[i].astype(np.uint8)
                output_basename = f"{input_basename}_layer_{i}.png"
                output_path = os.path.join(self.output_directory, output_basename)

                colored = cv.applyColorMap(layer * 255, cv.COLORMAP_VIRIDIS)
                cv.imwrite(output_path, colored)

                qim = load_image(output_path)
                ime = ImageEntry(layout.parent(), qim, output_path, output_basename)
                ime.registerMousePressHandler(self.image_entry_handler)
                layout.addWidget(ime)
                self.__generated_images_entries.append(ime)

                if first:
                    self.set_preview_image(qim, ime)
                    first = False


class App(QApplication):
    def __init__(self):
        super(App, self).__init__()
        self.main_window = MainWindow()
        self.main_window.show()


if __name__ == "__main__":
    app = App()
    sys.exit(app.exec_())
