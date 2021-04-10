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
from typing import Optional

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

    def merge_layers(self, layers_indices: [int]) -> None:
        """
        Merge all the specified layers
        :param layers_indices: A range of the layers to merge
        :return: None
        """
        for ime in self.__generated_images_entries:
            ime: ClusterImageEntry
            merged: Optional[np.ndarray] = None
            for i in layers_indices:
                _, layer_matrix_path = ime.get_layer_paths(i)
                layer = np.load(layer_matrix_path)
                merged = layer if merged is None else merged | layer

            for i in sorted(layers_indices, reverse=True):
                ime.remove_layer(i)

            if merged is None:
                break

            colored = apply_colormap(merged)
            merged_path_no_ext = os.path.join(os.path.dirname(ime.image_path),
                                              f"{ime.basename}_layer_{ime.layer_count() - 1}")
            merged_image_path = f"{merged_path_no_ext}.png"
            merged_array_path = f"{merged_path_no_ext}.npy"

            cv.imwrite(merged_image_path, colored)
            np.save(merged_array_path, merged)

            ime.add_layer_paths(merged_image_path, merged_array_path)

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

            input_basename_no_ext = (lambda basename: basename[0:basename.rfind(".")])(os.path.basename(ime.image_path))
            layers, cluster = Tat.generate_layers(np.asarray(cv.imread(ime.image_path, flags=cv.IMREAD_GRAYSCALE)),
                                                  self.ui.clusterCount.value(), self.ui.runCount.value(),
                                                  self.ui.maxIterCount.value())

            layers_paths: [tuple[str, str]] = []
            for i in range(len(layers)):
                layer = layers[i].astype(np.uint8)
                output_path_no_ext = os.path.join(self.output_directory, f"{input_basename_no_ext}_layer_{i}")
                output_image_path = f"{output_path_no_ext}.png"
                output_matrix_path = f"{output_path_no_ext}.npy"
                np.save(output_matrix_path, layer)
                cv.imwrite(output_image_path, apply_colormap(layer, cv.COLORMAP_VIRIDIS))
                layers_paths.append((output_image_path, output_matrix_path))

            output_path_no_ext = os.path.join(self.output_directory, f"{input_basename_no_ext}_cluster")
            output_image_path = f"{output_path_no_ext}.png"

            np.save(f"{output_path_no_ext}.npy", cluster)
            cv.imwrite(output_image_path, apply_colormap(cluster, cv.COLORMAP_JET))

            qim = load_image(output_image_path)
            ime = ClusterImageEntry(layout.parent(), qim, output_image_path, input_basename_no_ext, layers_paths)
            ime.registerMousePressHandler(self.image_entry_click_handler)
            ime.register_merge_action(self.merge_layers)
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
