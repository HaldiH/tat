---
title: TAT Documentation
summary: Tomography Analysis Tool Documentation
authors:
    - Hugo Haldi
date: 2021-05-12
---

# Welcome to TAT

Welcome to the documentation of the TAT GUI. TAT (for Tomography Analysis Tool) is a graphical interface letting you generate clusters for tomography images using the k-means method and manipulate clusters.

## Getting started

If you are a user, you can follow the [installation guide](user-guide/installation.md) and see the [user manual](user-guide/manual.md).

### Latest release

<table id="downloadTable">
    <tr>
        <th>Asset</th>
        <th>Download count</th>
    </tr>
</table>

### Quick start

Check if an installer is available for your system on the [release page](https://github.com/ShinoYasx/tat/releases) and get the latest version.

---

If your system is not supported or you want to install the pip version, follow these steps.

TAT needs Python >= 3.8 and 3.8.1 on Windows.

TAT is available in PyPI, thus you can install it with `pip` :

```shell
pip install tat
```

And then you can run the application as a Python module :

```shell
python -m tat
```

Or directly as a program if Python scripts are in path :

```shell
tat
```

And if you are using Windows, you can start the executable file created in the start menu under the name of `tat`.

```{toctree}
:caption: User Guide
:hidden:
Installation <user-guide/installation>
Interface manual <user-guide/manual>
```

```{toctree}
:caption: Developer Guide
:hidden:
References <dev-guide/references>
```

```{toctree}
:caption: About
:hidden:
license
Release Notes <changelog>
```

## Cite us

T. Bagni, H. Haldi, D. Mauro, C. Senatore. [Tomography analysis tool: an application for image analysis based on unsupervised machine learning](https://doi.org/10.1088/2633-1357/ac54bf) (2022) IOPSciNotes

Bagni, T., Bovone, G., Rack, A. et *al*. [Machine learning applied to X-ray tomography as a new tool to analyze the voids in RRP Nb<sub>3</sub>Sn wires](https://doi.org/10.1038/s41598-021-87475-6). *Sci Rep* **11**, 7767 (2021).
