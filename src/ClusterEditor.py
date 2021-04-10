import os

from PySide6.QtWidgets import QLayout, QLabel, QWidget
from PySide6.QtGui import QImage
from PySide6.QtCore import Slot

from clustereditor import Ui_EditorWindow
from PreviewWindow import PreviewWindow
from SourceImageEntry import SourceImageEntry
from Utils import load_image

from typing import Optional


class ClusterEditor(PreviewWindow):
    def __init__(self, parent: Optional[QWidget], calling_image_entry: []):
        super(ClusterEditor, self).__init__(parent)
        self.ui = Ui_EditorWindow()
        self.ui.setupUi(self)
        self.ui.mergeButton.clicked.connect(self.merge)

        self.cluster_image_entry = calling_image_entry
        layout: QLayout = self.ui.scrollAreaLayersContents.layout()

        first = True
        for i in range(self.cluster_image_entry.layer_count()):
            image_layer_path, array_layer_path = self.cluster_image_entry.get_layer_paths(i)
            qim: QImage = load_image(image_layer_path)
            ime = SourceImageEntry(layout.parent(), qim, image_layer_path, str(i), array_layer_path, False)
            ime.registerMousePressHandler(self.image_entry_click_handler)
            self.add_source_image_entry(ime)

            if first:
                self.set_preview_image(qim, ime)
                first = False

    def source_layout(self) -> QLayout:
        return self.ui.scrollAreaLayersContents.layout()

    def image_preview(self) -> QLabel:
        return self.ui.imageLabel

    @Slot()
    def merge(self):
        checked_entries: [int] = []
        for i in range(len(self._source_image_entries)):
            ime: SourceImageEntry = self._source_image_entries[i]
            if ime.isChecked():
                checked_entries.append(i)
                ime.setChecked(False)
                ime.close()

        if len(checked_entries) == 0:
            return

        self.cluster_image_entry.merge(checked_entries)

        merged_image_path, merged_array_path = self.cluster_image_entry.get_layer_paths(-1)
        qim: QImage = load_image(merged_image_path)

        merged_ime = SourceImageEntry(self.source_layout().parent(), qim, merged_image_path,
                                      str(self.cluster_image_entry.layer_count() - 1), merged_array_path, False)
        merged_ime.registerMousePressHandler(self.image_entry_click_handler)
        self.set_preview_image(qim, merged_ime)
        self.add_source_image_entry(merged_ime)
