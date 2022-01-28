''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.GUILayout.UIStartWindow import *


def StartWindow(self):
    """Activates the GUI window to select output path, project name
       and model path.

    The GUI gets activated. If you get "Back" from the "OptiWindow"
    "project_name", "output_path" and "model_path" get set. This data
    can be entered/selected via an input field and browse window.
    not a message box appears
    """

    self.Window1 = UIStartWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)
    
    self.Window1.project_name.setText(self.project_name)
    self.set_output_path_label(self.Window1)
    self.set_model_path_label(self.Window1)


    self.Window1.output_path_Browse.clicked.connect(lambda:self.get_output_path(self.Window1))
    self.Window1.read_model_browse.clicked.connect(lambda:self.get_model_path(self.Window1))
    
    self.Window1.Next.clicked.connect(lambda:nextWindow(self, "Next"))
    self.Window1.Back.clicked.connect(lambda:nextWindow(self, "Back"))
    
    self.setCentralWidget(self.Window1)
    self.show()



def nextWindow(self,n):
    self.project_name =  self.Window1.project_name.text()
    self.output_path =  self.Window1.output_path_label.text()
    self.model_path =  self.Window1.model_path_label.text()

    if n == "Back":
        self.GUIStart()

    elif n == "Next":
        if self.project_name == "" or self.model_path == "" or self.output_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            
            msg.setText("Please enter your data")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            
            return
        self.TargetWindow()