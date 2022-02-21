import sys
from cx_Freeze import setup, Executable
from pbr.packaging import get_version

build_exe_options = {"packages": [], "excludes": []}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="tat",
    version="{}.{}.{}".format(*get_version("tat").split(".")),
    description="Tomography Analysis Tool",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, target_name="tat")]
)
