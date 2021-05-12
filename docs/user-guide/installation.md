# Installation of TAT

!!! note
    An installer for Windows will be available in a future release.

## Via pip

### Requirements

During this section, we will assume that you have Python installed. If it is not the case, you can install it by downloading it on the [official Python website](https://www.python.org/downloads/) or using your distribution package manager if you are on Linux. Python 3.8 or superior is required.

### Installation

In a command prompt, write the following command to install the `tat` package add all its dependencies using the `pip` tool:

```shell
pip install tat
```

!!! note
    If you are using windows, it may happends that `pip` is not in your path. So you will need to add `python -m pip` to install the package, e.g.
    ```shell
    python -m pip install tat
    ```

## Via sources

### Getting the sources

As this project is open source, you can directly download the sources on the [Git repo](https://gitlab.unige.ch/Hugo.Haldi/tat). You can either download the sources as a zip on the website [gitlab.unige.ch/Hugo.Haldi/tat](https://gitlab.unige.ch/Hugo.Haldi/tat), or use [Git](https://git-scm.com):

```shell
git clone https://gitlab.unige.ch/Hugo.Haldi/tat.git tat
cd tat/
```

### Executing from sources

Once you download the sources, there will be an executable than you can run in the project root, called `main.py`. Run this file with Python to execute the application:

```shell
python main.py
```

## Executing the application

### Via the command line interface

TAT is a module and has a startup script, so you can run it with the following command:

```shell
python -m tat
```
