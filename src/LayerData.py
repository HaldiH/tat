from typing import Optional, Final


class LayerData:
    def __init__(self, image_path: str, array_path: str, is_merger=False, merged_from: Optional[str] = None):
        self.image_path: Final[str] = image_path
        self.array_path: Final[str] = array_path
        self.is_merger: Final[bool] = is_merger
        self.merged_from: Final[Optional[str]] = merged_from
