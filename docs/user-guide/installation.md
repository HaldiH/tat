# Installation of TAT

## Via installer (only Windows currently supported)

There is only Windows installer currently supported. For Linux or macOS, get the [pip version](#via-pip) or [compile the sources](#via-sources). To get the installer, go to the [release page](https://github.com/ShinoYasx/tat/releases), and click on the file you want to download.

The `.msi` file is an installer that will automatically put all the files in the selected directory and will create desktop and start menu shortcuts. The zip file is a _portable_ version containing the executable `tat.exe` and all the required dependencies (no installation required).

This version is a standalone, meaning that you don't need any prerequisite (e.g. having a python distribution installed) to run the application.

## Via pip

### Requirements

During this section, we will assume that you have Python installed. If it is not the case, you can install it by downloading it on the [official Python website](https://www.python.org/downloads/) or using your distribution package manager if you are on Linux. Python 3.8 or superior is required.

### Installation

In a command prompt, write the following command to install the `tat` package add all its dependencies using the `pip` tool :

```shell
pip install tat
```

:::{note}
If you are using Windows, it may happends that `pip` is not in your path. So you will need to add `python -m pip` to install the package, e.g.
    ```shell
    python -m pip install tat
    ```
:::

## Via sources

### Getting the sources

As this project is open source, you can directly download the sources on the [Git repo](https://github.com/ShinoYasx/tat). You can either download the sources as a zip on the website [https://github.com/ShinoYasx/tat](https://github.com/ShinoYasx/tat), or use [Git](https://git-scm.com) :

```shell
git clone https://github.com/ShinoYasx/tat tat
cd tat/
```

### Installing from sources

Once you download the sources, there will be an executable than you can run in the project root, called `setup.py`. Run this file will install TAT in your current python environment :

```shell
python setup.py install
```

## Executing the application

### Via the command line interface

TAT is a module and has a startup script, so you can run it with the following command :

```shell
python -m tat
```

Or if the Python scripts are in your path :

```shell
tat
```

### Via a desktop environment

#### Windows

If you used the installer, a shortcut should be available on the Desktop and in the Start Menu named _Tomography Analysis Tool_. Just click on it to start the application.

If you used pip or sources installation, an executable file should be available in the start menu, to find it simply type `tat` in the search bar. Click `tat.exe` to open the application.

#### Linux

If you are on Linux, there will be no default desktop executable. You can however download [this file](https://github.com/ShinoYasx/tat/blob/master/data/ch.unige.tat.desktop) and put it into `~/.local/share/applications`, or with a one-liner bash command :

```shell
curl --create-dirs -O --output-dir ~/.local/share/applications/ https://raw.githubusercontent.com/ShinoYasx/tat/master/data/ch.unige.tat.desktop
```
