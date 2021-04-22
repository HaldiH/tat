import os
import threading
from pathlib import Path
from typing import Optional

import numpy as np
import cv2 as cv

from PySide6.QtWidgets import QFileDialog, QLabel, QLayout, QDialog, QProgressBar
from PySide6.QtCore import Slot

from .api import Tat
from . import CheckableImageEntry, PreviewWindow, ClusterImageEntry, ClusterEditor
from .LayerData import LayerData
from .Ui_MainWindow import Ui_MainWindow
from .Ui_ProgressBar import Ui_ProgressBar
from .Utils import load_image, apply_colormap


class MainWindow(PreviewWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.input_directory = ""
        self.output_directory = ""
        self.editor_window: Optional[ClusterEditor] = None

        self.__generated_images_entries: list[ClusterImageEntry] = []

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

    def open_preview_window(self, calling_image_entry: ClusterImageEntry):
        if self.editor_window is not None and self.editor_window.isVisible():
            self.editor_window.activateWindow()
            return
        self.editor_window = ClusterEditor(self, calling_image_entry)
        self.editor_window.register_merge_handler(self.merge_layers)
        self.editor_window.show()

    def merge_layers(self, layers_indices: list[int]) -> None:
        """
        Merge all the specified layers
        :param layers_indices: A range of the layers to merge
        :return: None
        """
        if len(layers_indices) == 0:
            return

        for ime in self.__generated_images_entries:
            merged: Optional[np.ndarray] = None
            merged_str = ""
            for i in layers_indices:
                merged_str += str(i) if i == layers_indices[0] else f"+{str(i)}"

                layer_data: LayerData = ime.get_layer_data(i)
                layer = np.load(layer_data.array_path)
                merged = layer if merged is None else merged | layer

            for i in sorted(layers_indices, reverse=True):
                ime.remove_layer(i)

            if merged is None:
                break

            colored = apply_colormap(merged)
            merged_dir = os.path.join(os.path.dirname(ime.image_path), "merged")
            Path(merged_dir).mkdir(exist_ok=True)
            merged_path_no_ext = os.path.join(merged_dir, f"{ime.basename}_layers_{merged_str}")
            merged_image_path = f"{merged_path_no_ext}.png"
            merged_array_path = f"{merged_path_no_ext}.npy"

            cv.imwrite(merged_image_path, colored)
            np.save(merged_array_path, merged)

            ime.add_layer_data(LayerData(merged_image_path, merged_array_path, is_merger=True, merged_from=merged_str))

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

            ime = CheckableImageEntry(src_layout.parent(), qim, entry.name, entry.path)
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
    def generate_handler(self):
        progress_bar = QDialog(self)
        progress_bar.ui = Ui_ProgressBar()
        progress_bar.ui.setupUi(progress_bar)

        container = self.ui.scrollAreaWidgetContentsDst.layout()
        img_count = 0
        for index, ime in enumerate(self._source_image_entries):
            ime: CheckableImageEntry
            if not ime.isChecked():
                continue
            thread = threading.Thread(target=self.generate_cluster, args=(ime, container, progress_bar.ui.progressBar))
            thread.start()
            img_count += 1

        progress_bar.ui.progressBar.setMaximum(img_count)
        progress_bar.show()

    # WIP
    def generate_cluster(self, ime: CheckableImageEntry, container: QLayout, progressbar: QProgressBar):
        input_basename_no_ext = (lambda basename: basename[0:basename.rfind(".")])(os.path.basename(ime.image_path))
        layers, cluster = Tat.generate_layers(np.asarray(cv.imread(ime.image_path, flags=cv.IMREAD_GRAYSCALE)),
                                              self.ui.clusterCount.value(), self.ui.runCount.value(),
                                              self.ui.maxIterCount.value())

        layers_data: list[LayerData] = []
        for i, layer in enumerate(layers):
            output_path_no_ext = os.path.join(self.output_directory, f"{input_basename_no_ext}_layer_{i}")
            output_image_path = f"{output_path_no_ext}.png"
            output_matrix_path = f"{output_path_no_ext}.npy"
            np.save(output_matrix_path, layer)
            cv.imwrite(output_image_path, apply_colormap(layer, cv.COLORMAP_VIRIDIS))
            layers_data.append(LayerData(output_image_path, output_matrix_path))

        output_path_no_ext = os.path.join(self.output_directory, f"{input_basename_no_ext}_cluster")
        output_image_path = f"{output_path_no_ext}.png"
        output_array_path = f"{output_path_no_ext}.pny"

        np.save(output_array_path, cluster)
        cv.imwrite(output_image_path, apply_colormap(cluster, cv.COLORMAP_JET))

        qim = load_image(output_image_path)
        ime = ClusterImageEntry(container.parent(), qim, output_image_path, output_array_path, input_basename_no_ext,
                                layers_data)
        ime.registerMousePressHandler(self.image_entry_click_handler)
        ime.register_merge_action(self.merge_layers)
        ime.register_mouse_double_click_action(self.open_preview_window)
        container.addWidget(ime)
        self.__generated_images_entries.append(ime)
        progressbar.setValue(progressbar.value() + 1)

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

            layers_data: list[LayerData] = []
            for i, layer in enumerate(layers):
                output_path_no_ext = os.path.join(self.output_directory, f"{input_basename_no_ext}_layer_{i}")
                output_image_path = f"{output_path_no_ext}.png"
                output_array_path = f"{output_path_no_ext}.npy"
                np.save(output_array_path, layer)
                cv.imwrite(output_image_path, apply_colormap(layer, cv.COLORMAP_VIRIDIS))
                layers_data.append(LayerData(output_image_path, output_array_path))

            output_path_no_ext = os.path.join(self.output_directory, f"{input_basename_no_ext}_cluster")
            output_image_path = f"{output_path_no_ext}.png"
            output_array_path = f"{output_path_no_ext}.npy"

            np.save(output_array_path, cluster)
            cv.imwrite(output_image_path, apply_colormap(cluster, cv.COLORMAP_JET))

            qim = load_image(output_image_path)
            ime = ClusterImageEntry(layout.parent(), qim, output_image_path, output_array_path, input_basename_no_ext,
                                    layers_data)
            ime.registerMousePressHandler(self.image_entry_click_handler)
            ime.register_merge_action(self.merge_layers)
            ime.register_mouse_double_click_action(self.open_preview_window)
            layout.addWidget(ime)
            self.__generated_images_entries.append(ime)

            if first:
                self.set_preview_image(qim, ime)
                first = False
