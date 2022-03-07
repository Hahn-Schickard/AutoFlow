'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

from src.GUILayout.UITargetWindow import *


def TargetWindow(self):
    """Select a button to choose your device.

    You can choose via three different buttons on which device you want
    to exectue the model. If "Back" is pressed you get back to the start
    window. If you choose a device you get to the optimization window.
    """
    self.Window2 = UITargetWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
                                  self.FONT_STYLE, self)

    self.Window2.mcu.clicked.connect(lambda: nextWindow(self, "Next", "MCU"))
    self.Window2.fpga.clicked.connect(lambda: nextWindow(self, "Next", "FPGA"))
    self.Window2.sbc.clicked.connect(lambda: nextWindow(self, "Next", "SBC"))

    self.Window2.back.clicked.connect(lambda: nextWindow(self, "Back", None))

    self.setCentralWidget(self.Window2)
    self.show()


def nextWindow(self, n, target):
    """
    Defines which one is the next window to open.

    Args:
        n:      Go forward or go back
        target: Target to execute the neural network
    """
    if n == "Back":
        self.StartWindow()

    elif n == "Next":
        self.target = target
        print("Target:", self.target)

        if (self.target == "MCU" or self.target == "FPGA" or
                self.target == "SBC"):
            self.OptiWindow()
