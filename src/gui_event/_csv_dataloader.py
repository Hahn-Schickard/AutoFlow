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

from src.gui_layout.ui_csv_dataloader import *


def csv_dataloader(self, MainWindow):
    """Activates the GUI window to preview and load CSV data.

    With the help of the check boxes the separators can be selected.
    There are three buttons to interact with. With "Browse" you can
    select the CSV file you want to use. "Preview" shows format of
    the CSV file according to the selected separators. "Load data"
    selects the settings of the preview and take them to train the
    model later.

    Args:
        MainWindow: Main window if the GUI
    """
    self.csv_dataloader_ui = UICSVDataloader(self.WINDOW_WIDTH,
                                             self.WINDOW_HEIGHT,
                                             self.FONT_STYLE)

    self.csv_dataloader_ui.browse.clicked.connect(
        lambda: self.browse_csv_data(self.csv_dataloader_ui))
    self.csv_dataloader_ui.preview.clicked.connect(
        lambda: self.preview_csv_data(self.csv_dataloader_ui))
    self.csv_dataloader_ui.load_data.clicked.connect(
        lambda: self.load_csv_data(self.csv_dataloader_ui, MainWindow))

    self.csv_dataloader_ui.show()
