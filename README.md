# PySide6QCustomPlot2
Python binding based on QCustomPlot 2, adapted to PySide6

# Introduction

These are PySide6 bindings for the [QCustomPlot library](https://www.qcustomplot.com/).

# Building

## Windows

Install required software:
- Qt 6.7.3 MSVC2019_64bit
- Visual studio 2019 C++ compiler
- CMD or PyCharm

Create a virtual environment:

     py -3.11 -m venv .venv
     .venv\scripts\activate.bat

Install pyside6 shiboken6 and generator:

     pip install build py-build-cmake
     pip install --index-url=https://download.qt.io/official_releases/QtForPython/ --trusted-host download.qt.io shiboken6==6.3.2 pyside6==6.3.2 shiboken6_generator==6.3.2

If the installation is slow, you can try use the following address:

     pip install --index-url=https://mirrors.tuna.tsinghua.edu.cn/qt/official_releases/QtForPython/ --trusted-host download.qt.io shiboken6==6.7.3 pyside6==6.7.3 shiboken6_generator==6.7.3

Use visual studio 2019 for compilation:

     "C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Auxiliary\Build\vcvars64.bat"

Now check the file CMakeLists.txt, and adjust paths to Qt and python:
- MY_SITE_PACKAGES_PATH
- MY_PYTHON_INSTALL_PATH
- MY_QT_INSTALL

Build the bindings:

    > mkdir build
    > cd build
    > cmake -G Ninja ..
    > ninja

To build a python wheel:

    > pip install build py-build-cmake
    > python -m build --no-isolation --wheel

Install the wheel:

    > pip install dist\pyside6qcustomplot-2.1.1-cp311-cp311-win_amd64.whl

Or you can directly use genWhl.py under the tools file:
    
    > python tools/genWhl.py

The following command will generate a pyi file and rename it to PySide6QCustomPlot2(Capital letters):

    > python tools/genPyiReWhl.py

# Todo

At present, only a few commonly used classes are bound

# Acknowledgements

This project is inspired by and built upon the following excellent projects (in no particular order):

- [**QCustomPlot**](https://www.qcustomplot.com/) – A high-performance plotting library for Qt, which provides the core C++ drawing functionality.  
- [**PySide6**](https://wiki.qt.io/Qt_for_Python) – The official Python bindings for the Qt framework.  
- [**Shiboken**](https://doc.qt.io/qtforpython-6/shiboken6/shibokenmodule.html) – The binding generator used to bridge Python and C++ code.
- [**PySide6QCustomPlot**](https://github.com/DEMCON/PySide6QCustomPlot) – An earlier Python binding implementation of QCustomPlot, which served as a reference for this project.  
