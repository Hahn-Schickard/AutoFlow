''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.GUILayout.UICSVDataloaderWindow import *


def CSVDataloaderWindow(self, LastWindow):
    """Activates the GUI window to preview and load CSV data.

    With the help of the check boxes the separators can be selected 
    There are three buttons to interact with. With "Browse" you can
    select the CSV file you want to use. "Preview" shows format of
    the CSV file according to the selected separators. "Load data"
    selects the settings of the preview and take them to train the
    model later.    
    """

    self.Window3_1 = UICSVDataloaderWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE)

    self.Window3_1.Browse.clicked.connect(lambda: self.browseCSVData(self.Window3_1))
    self.Window3_1.Preview.clicked.connect(lambda: self.previewCSVData(self.Window3_1))
    self.Window3_1.Load_data.clicked.connect(lambda: self.loadCSVData(self.Window3_1, LastWindow))

    self.Window3_1.show()