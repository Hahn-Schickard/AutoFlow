''' Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

"""This is the start file to run the AUTOFlow GUI

In this file we import the libarys and define the GUI with all the layouts

  Typical usage example:

  python start.py
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from src.GUIEvents import MainWindow





app = QApplication(sys.argv)
# Force the style to be the same on all OSs:
app.setStyle("Fusion")

# Now use a palette to switch to dark colors:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)

app.setStyleSheet("QPushButton:pressed { background-color: rgb(10, 100, 200) }" "QPushButton:checked { background-color: rgb(10, 100, 200) }" "QPushButton::hover { background-color : rgb(10, 100, 200)}" )

screen_width = app.primaryScreen().size().width()
screen_height = app.primaryScreen().size().height()

print("screen_width:",screen_width)
print("screen_height:",screen_height)

w = MainWindow(screen_width, screen_height)
w.show()
w.setFixedSize(w.size())
sys.exit(app.exec_())