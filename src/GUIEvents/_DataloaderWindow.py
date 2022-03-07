'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.GUILayout.UIDataloaderWindow import *


def DataloaderWindow(self):
    """Activates the GUI window of the data loader.

    With the dropdown menu you can select whether the training data
    should be transferred in a file or folder.
    """
    self.Window3 = UIDataloaderWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
                                      self.FONT_STYLE, self)

    if self.data_loader_path is not None:
        self.set_label(self.Window3.data_path_label, self.data_loader_path,
                       Qt.AlignCenter)

    self.Window3.select_data_browse.clicked.connect(
        lambda: self.get_data_loader(self.Window3,
                                     self.Window3.data_path_label))

    self.Window3.back.clicked.connect(lambda: nextWindow(self, "Back"))
    self.Window3.next.clicked.connect(lambda: nextWindow(self, "Next"))

    self.setCentralWidget(self.Window3)
    self.show()


def nextWindow(self, n):
    """
    Defines which one is the next window to open.

    Args:
        n:  Go forward or go back
    """
    self.data_loader_path = self.Window3.data_path_label.text()

    if n == "Back":
        self.OptiWindow()

    elif n == "Next":

        if self.data_loader_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Please enter a data loader.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

        self.LoadWindow()
