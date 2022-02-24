# Tomography Analysis Tool

A tool for 2D tomographic images clustering using the k-means method.

[![Python package](https://github.com/ShinoYasx/tat/actions/workflows/python-package.yml/badge.svg)](https://github.com/ShinoYasx/tat/actions/workflows/python-package.yml)
[![Package](https://github.com/ShinoYasx/tat/actions/workflows/package.yml/badge.svg)](https://github.com/ShinoYasx/tat/actions/workflows/package.yml)
[![Documentation Status](https://readthedocs.org/projects/tat/badge/?version=latest)](https://tat.readthedocs.io/en/latest/?badge=latest)

## Dependencies

- [PySide6](https://pypi.org/project/PySide6/) - [API reference](https://doc.qt.io/qtforpython-6/modules.html)
- [numpy](https://pypi.org/project/numpy/) - [API reference](https://numpy.org/doc/stable/reference/index.html)
- [opencv](https://pypi.org/project/opencv-python/) - [API reference](https://docs.opencv.org/master/index.html)
- [scikit-image](https://pypi.org/project/scikit-image/) - [API reference](https://scikit-image.org/docs/stable/api/api.html)
- [scikit-learn](https://pypi.org/project/scikit-learn/) - [API reference](https://scikit-learn.org/stable/modules/classes.html)

## Install

### Standalone installer

#### Windows

There is only Windows installer currently supported. For Linux or macOS, get the [pip version](#pip). To get the installer, go to the [release page](https://github.com/ShinoYasx/tat/releases), and click on the file you want to download.

The `.msi` file is an installer that will automatically put all the files in the selected directory and will create desktop and start menu shortcuts. The zip file is a _portable_ version containing the executable `tat.exe` and all the required dependencies (no installation required).

### Pip

This application is also available on [PyPI](https://pypi.org/project/tat/). You can install it using the `pip` tool :

```bash
pip install tat
```

## Usage

If you used the installer, a shortcut named _Tomography Analysis Tool_ will be available in the start menu and on the Desktop. Just click it to open the application.

If you used the pip version, you can use the command line to run the application or launch it via the start menu (search for _tat_) if you are running on Windows.

e.g.

```bash
python -m tat
```
