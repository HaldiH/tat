import sys
from cx_Freeze import setup, Executable

sys.path.insert(0, "src")

build_exe_options = {
    "packages": [
        "PySide6",
        "cv2",
        "skimage",
        "tat"
    ],
    "excludes": [
        "tkinter"
    ],
    "path": sys.path
}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

version = ""
with open("version.txt") as f:
    version = f.read().rstrip("\n")

setup(
    name="tat",
    version=version,
    description="Tomography Analysis Tool",
    options={"build_exe": build_exe_options},
    executables=[Executable("src/tat/__main__.py",
                            base=base, target_name="tat")]
)
