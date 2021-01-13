import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from UIWindows.UITaskWindow import *

        
def TaskWindow(self, n):
    
    if n == "Next":
        
        self.project_name = self.Window1d.Projekt_Name.text()
        self.output_path_ml = self.Window1d.Output_Pfad.text()
        self.data_loader_path_ml = self.Window1d.Daten_Pfad.text() 
            
    if self.project_name == "" or self.output_path == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
         
        msg.setText("Please enter your data")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
        
        return
    
    if n == "Back":
        
        if "Params" in self.constraints:
            self.params_factor = float(self.Window3.Params_factor.text())
        if "Floats" in self.constraints:
            self.floats_factor = float(self.Window3.Floats_factor.text())
        if "Complex" in self.constraints:
            self.complex_factor = float(self.Window3.Complex_factor.text())

    print(self.data_loader_path_ml)
    
    
    self.Window2 = UITaskWindow(self.FONT_STYLE, self)
    
    
    self.Window2.ImageClassification.clicked.connect(lambda:self.ConstraintsWindow("Next","imageClassification"))
    self.Window2.ImageRegression.clicked.connect(lambda:self.ConstraintsWindow("Next","imageRegression"))
    self.Window2.TextClassification.clicked.connect(lambda:self.ConstraintsWindow("Next","textClassification"))
    self.Window2.TextRegression.clicked.connect(lambda:self.ConstraintsWindow("Next","textRegression"))
    self.Window2.DataClassification.clicked.connect(lambda:self.ConstraintsWindow("Next","dataClassification"))
    self.Window2.DataRegression.clicked.connect(lambda:self.ConstraintsWindow("Next","dataRegression"))

    
    self.Window2.Back.clicked.connect(self.MarcusWindow4)
    
    self.setCentralWidget(self.Window2)
    self.show()