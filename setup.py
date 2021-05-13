import os
from typing import List, Tuple

import setuptools

data_files: List[Tuple[str, List[str]]] = []

if os.name == 'posix':
    data_files.append(('share/applications', ['data/ch.unige.tat.desktop']))

setuptools.setup(
    setup_requires=['pbr'],
    pbr=True,
    data_files=data_files
)
