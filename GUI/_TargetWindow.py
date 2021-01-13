import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from UIWindows.UITargetWindow import *

def TargetWindow(self, n):
    
    if n == "Next":
        
        self.project_name = self.Window1.Projekt_Name.text()
        self.output_path = self.Window1.Output_Pfad.text()
        self.model_path = self.Window1.Model_Pfad.text()
        self.data_loader_path = self.Window1.Daten_Pfad.text() 
            
    if self.project_name == "" or self.model_path == "" or self.output_path == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
         
        msg.setText("Please enter your data")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
        
        return
    
    if n == "Back":
        
        if "Pruning" in self.optimizations:
            self.prun_factor_dense = int(self.Window3.Pruning_Dense.text())
            self.prun_factor_conv = int(self.Window3.Pruning_Conv.text())
        if "Knowledge_Distillation" in self.optimizations:
            self.Know_Dis_1 = int(self.Window3.Dis_1.text())
            self.Know_Dis_2 = int(self.Window3.Dis_2.text())
        if "Huffman_Coding" in self.optimizations:
            self.Huffman_1 = int(self.Window3.Huf_1.text())
            self.Huffman_2 = int(self.Window3.Huf_2.text())

    print(self.model_path)
    print(self.data_loader_path)
    
    
    self.Window2 = UITargetWindow(self.FONT_STYLE, self)
    
    
    self.Window2.uC.clicked.connect(lambda:self.OptiWindow("Next","uC"))
    self.Window2.FPGA.clicked.connect(lambda:self.OptiWindow("Next","FPGA"))
    self.Window2.DK.clicked.connect(lambda:self.HelperWindow())
    
    self.Window2.Back.clicked.connect(self.StartWindow)
    
    self.setCentralWidget(self.Window2)
    self.show()