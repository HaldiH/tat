import sys
import os

from PySide6.QtWidgets import QApplication, QFileDialog, QLabel, QLayout
from PySide6.QtCore import Slot, QEvent, QSize
from PySide6.QtGui import QPixmap, QImage, QResizeEvent

from api import Tat
from mainwindow import Ui_MainWindow
from SourceImageEntry import SourceImageEntry
from ImageEntry import ImageEntry
from PreviewWindow import PreviewWindow
from ClusterImageEntry import ClusterImageEntry
from Utils import fit_to_frame, load_image, apply_colormap

import numpy as np
import cv2 as cv


class MainWindow(PreviewWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.input_directory = ""
        self.output_directory = ""

        self.__generated_images_entries: [ClusterImageEntry] = []

        self.ui.buttonInputDir.clicked.connect(self.load_input_directory)
        self.ui.buttonOutputDir.clicked.connect(self.load_output_directory)
        self.ui.buttonGenerate.clicked.connect(self.generate)
        self.ui.buttonCheckUncheck.clicked.connect(self.select_deselect)
        self.ui.buttonClearGenerated.clicked.connect(self.clear_generated)

    def source_layout(self) -> QLayout:
        return self.ui.scrollAreaWidgetContentsSrc.layout()

    def image_preview(self) -> QLabel:
        return self.ui.imagePreview

    def clear_generated(self):
        for ime in self.__generated_images_entries:
            ime.close()

    def clear_image_entries(self):
        super(MainWindow, self).clear_image_entries()
        for ime in self.__generated_images_entries:
            ime.close()
        self.__generated_images_entries.clear()

    @Slot()
    def load_input_directory(self):
        self.input_directory = QFileDialog.getExistingDirectory(self)
        if len(self.input_directory) == 0:
            return

        self.clear_image_entries()
        self.clear_preview_image()

        # self.ui.labelInDir.setText(f"Loaded: {self.input_directory}")

        src_layout = self.source_layout()
        first = True
        for entry in os.scandir(self.input_directory):
            if not Tat.is_image(entry.path):
                continue

            qim = load_image(entry.path)

            ime = SourceImageEntry(src_layout.parent(), qim, entry.path, entry.name)
            ime.registerMousePressHandler(self.image_entry_click_handler)
            self.add_source_image_entry(ime)

            if first:
                self.set_preview_image(qim, ime)
                first = False

        if len(self.output_directory) != 0:
            self.ui.buttonGenerate.setEnabled(True)

    @Slot()
    def load_output_directory(self):
        self.output_directory = QFileDialog.getExistingDirectory(self)
        if len(self.output_directory) == 0:
            return

        # self.ui.labelOutDir.setText(f"Loaded: {self.output_directory}")
        if len(self.input_directory) != 0:
            self.ui.buttonGenerate.setEnabled(True)

    @Slot()
    def generate(self):
        layout = self.ui.scrollAreaWidgetContentsDst.layout()
        first = True
        for ime in self._source_image_entries:
            if not ime.isChecked() or not Tat.is_image(ime.image_path):
                continue

            input_basename = (lambda basename: basename[0:basename.rfind(".")])(os.path.basename(ime.image_path))
            layers, cluster = Tat.generate_layers(np.asarray(cv.imread(ime.image_path, flags=cv.IMREAD_GRAYSCALE)),
                                                  self.ui.clusterCount.value(), self.ui.runCount.value(),
                                                  self.ui.maxIterCount.value())

            layers_paths: [str] = []
            output_basename = f"{input_basename}_cluster.png"
            output_path = os.path.join(self.output_directory, output_basename)

            np.save(f"{output_path[0:output_path.rfind('.')]}.npy", cluster)

            cv.imwrite(output_path, apply_colormap(cluster, cv.COLORMAP_JET))
            qim = load_image(output_path)
            ime = ClusterImageEntry(layout.parent(), qim, output_path, input_basename, layers_paths)
            ime.registerMousePressHandler(self.image_entry_click_handler)
            layout.addWidget(ime)
            self.__generated_images_entries.append(ime)

            if first:
                self.set_preview_image(qim, ime)
                first = False

            for i in range(len(layers)):
                layer = layers[i].astype(np.uint8)
                output_basename = f"{input_basename}_layer_{i}.png"
                output_path = os.path.join(self.output_directory, output_basename)
                np.save(f"{output_path[0:output_path.rfind('.')]}.npy", layer)
                layers_paths.append(output_path)

                cv.imwrite(output_path, apply_colormap(layer, cv.COLORMAP_VIRIDIS))


class App(QApplication):
    def __init__(self):
        super(App, self).__init__()
        self.main_window = MainWindow()
        self.main_window.show()


if __name__ == "__main__":
    app = App()
    sys.exit(app.exec_())
