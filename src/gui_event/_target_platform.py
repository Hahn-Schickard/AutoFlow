'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

from src.gui_layout.ui_target_platform import *


def target_platform(self):
    """Select a button to choose your device.

    You can choose via three different buttons on which device you want
    to exectue the model. If "Back" is pressed you get back to the start
    window. If you choose a device you get to the optimization window.
    """
    self.target_platform_ui = UITargetPlatform(
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)

    self.target_platform_ui.mcu.clicked.connect(
        lambda: next_window(self, "Next", "MCU"))
    self.target_platform_ui.fpga.clicked.connect(
        lambda: next_window(self, "Next", "FPGA"))
    self.target_platform_ui.sbc.clicked.connect(
        lambda: next_window(self, "Next", "SBC"))

    self.target_platform_ui.back.clicked.connect(
        lambda: next_window(self, "Back", None))

    self.setCentralWidget(self.target_platform_ui)
    self.show()


def next_window(self, n, target):
    """
    Defines which one is the next window to open.

    Args:
        n:      Go forward or go back
        target: Target to execute the neural network
    """
    if n == "Back":
        self.project_data()

    elif n == "Next":
        self.target = target
        print("Target:", self.target)

        if (self.target == "MCU" or self.target == "FPGA" or
                self.target == "SBC"):
            self.optimization_algo()
