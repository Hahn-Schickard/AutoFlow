import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from src.GUIEvents import MainWindow


#from Threads.Loading_images_thread import *
#from Threads.Create_project_thread import *
#from Threads.Prune_model_thread import *


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

w = MainWindow()
w.show()
#w.setFixedSize(w.size())
sys.exit(app.exec_())
