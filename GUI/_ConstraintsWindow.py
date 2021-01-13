import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UIConstraintsWindow import *


        
def ConstraintsWindow(self, n, target):
    
    if n == "Next":
        self.target = target
        print(self.target)
        
        if self.target == "?":
            self.Dot.setVisible(False)
        if self.target == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("Please choose a task")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            
            return

    self.Window3 = UIConstraintsWindow(self.FONT_STYLE, self)
    
    if "Params" in self.constraints:
        self.Window3.Params.setChecked(True)
        self.set_params()
        self.Window3.Params_factor.setText(str(self.params_factor))
    if "Floats" in self.constraints:
        self.Window3.Floats.setChecked(True)
        self.set_floats()
        self.Window3.Floats_factor.setText(str(self.floats_factor))
    if "Complex" in self.constraints:
        self.Window3.Complex.setChecked(True)
        self.set_complex()
        self.Window3.Complex_factor.setText(str(self.complex_factor)) 
        
    self.Window3.Params.toggled.connect(self.set_params)
    self.Window3.Floats.toggled.connect(self.set_floats)
    self.Window3.Complex.toggled.connect(self.set_complex)

    
    self.Window3.Back.clicked.connect(lambda:self.TaskWindow("Back"))
    self.Window3.Next.clicked.connect(lambda:self.SettingsWindow("Next"))
    
    self.setCentralWidget(self.Window3)
    self.show()