import sys
from cx_Freeze import setup, Executable
from pbr.packaging import get_version

build_exe_options = {"packages": ["PySide6", "cv2", "skimage"], "excludes": []}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="tat",
    version="{}.{}.{}".format(*get_version("tat").split(".")),
    description="Tomography Analysis Tool",
    options={"build_exe": build_exe_options},
    executables=[Executable("src/tat/__main__.py", base=base, target_name="tat")]
)
