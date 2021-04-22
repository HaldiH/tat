from __future__ import annotations

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage, QMouseEvent

from . import ImageEntry

from typing import Optional, Callable, Any


class ClusterImageEntry(ImageEntry):
    def __init__(self, parent: QWidget, image: QImage, image_path: str, array_path: str, name: str,
                 layers_paths: list[tuple[str, str]]):
        """
        Instantiate a ClusterImageEntry object
        :param parent: The widget calling the method
        :param image: The image that will be used to draw the preview thumbnail
        :param image_path: The path of the cluster image
        :param name: The name that will be showed below the thumbnail
        :param layers_paths: A list of tuples containing every layer image and matrix path
        """
        super(ClusterImageEntry, self).__init__(parent, image, image_path, name, array_path)
        t = list(zip(*layers_paths))
        self.__layers_images_paths = list(t[0])
        self.__layers_arrays_paths = list(t[1])
        self.__merge_actions: list[Callable[[[int]], Any]] = []
        self.__mouse_double_click_actions: list[Callable[[ClusterImageEntry], Any]] = []

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        for action in self.__mouse_double_click_actions:
            action(self)

    def layer_count(self) -> int:
        return len(self.__layers_images_paths)

    def add_layer_paths(self, image_path, array_path):
        self.__layers_images_paths.append(image_path)
        self.__layers_arrays_paths.append(array_path)

    def get_layer_paths(self, index: int) -> tuple[str, str]:
        return self.__layers_images_paths[index], self.__layers_arrays_paths[index]

    def remove_layer(self, index: int) -> tuple[str, str]:
        return self.__layers_images_paths.pop(index), self.__layers_arrays_paths.pop(index)

    def register_merge_action(self, action: Callable[[[int]], Any]):
        self.__merge_actions.append(action)

    def register_mouse_double_click_action(self, action: Callable[[ClusterImageEntry], Any]):
        self.__mouse_double_click_actions.append(action)
