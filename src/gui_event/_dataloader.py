'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: GPL-3.0
============================================================================'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.gui_layout.ui_dataloader import *


def dataloader(self):
    """Activates the GUI window of the data loader.

    With the dropdown menu you can select whether the training data
    should be transferred in a file or folder.
    """
    self.dataloader_ui = UIDataloader(self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
                                      self.FONT_STYLE, self)

    if self.data_loader_path is not None:
        self.set_label(self.dataloader_ui.data_path_label,
                       self.data_loader_path, Qt.AlignCenter)

    self.dataloader_ui.select_data_browse.clicked.connect(
        lambda: self.get_data_loader(self.dataloader_ui,
                                     self.dataloader_ui.data_path_label))

    self.dataloader_ui.back.clicked.connect(lambda: next_window(self, "Back"))
    self.dataloader_ui.next.clicked.connect(lambda: next_window(self, "Next"))

    self.setCentralWidget(self.dataloader_ui)
    self.show()


def next_window(self, n):
    """
    Defines which one is the next window to open.

    Args:
        n:  Go forward or go back
    """
    self.data_loader_path = self.dataloader_ui.data_path_label.text()

    if n == "Back":
        self.optimization_algo()

    elif n == "Next":

        if self.data_loader_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Please enter a data loader.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

        self.create_project()
