""" Python wrapper for QCustomPlot2
"""

__version__ = '2.1.1'

# Trick to load Qt DLL's before PySide6QCustomPlot2.
import PySide6.QtWidgets
import PySide6.QtCore
import PySide6.QtPrintSupport

# Now load PySide6QCustomPlot2
from .PySide6QCustomPlot2 import *
