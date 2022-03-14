'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: GPL-3.0
============================================================================'''

from src.gui_layout.ui_gui_start import *


def gui_start(self):
    """Actiivates the start window of the GUI

    You can decide if you want to train a new model using
    AutoKeras or if you want to load an already trained
    model.
    """
    self.gui_start_ui = UIGUIStart(self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
                                   self.FONT_STYLE, self)

    self.gui_start_ui.load_model.clicked.connect(
        lambda: next_window(self, "AutoML"))
    self.gui_start_ui.train_model.clicked.connect(
        lambda: next_window(self, "LoadModel"))

    self.setCentralWidget(self.gui_start_ui)
    self.show()


def next_window(self, n):
    """
    Defines which one is the next window to open.

    Args:
        n:  Next window to open
    """
    if n == "AutoML":
        self.automl_data()

    elif n == "LoadModel":
        self.project_data()
