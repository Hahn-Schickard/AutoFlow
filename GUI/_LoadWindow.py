import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UILoadWindow import *


def LoadWindow(self, n):  

    if n == "Next":
        if "Pruning" in self.optimizations:
            try:
                if int(self.Window3.Pruning_Dense.text()) < 5 or int(self.Window3.Pruning_Dense.text()) > 95  or int(self.Window3.Pruning_Conv.text()) < 5  or int(self.Window3.Pruning_Conv.text()) > 95:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                     
                    msg.setText("Enter prunefactors between 5 and 95")
                    msg.setWindowTitle("Warning")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
                    return
                
                self.prun_factor_dense = int(self.Window3.Pruning_Dense.text())
                self.prun_factor_conv = int(self.Window3.Pruning_Conv.text())
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                 
                msg.setText("Please enter a number")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return
        
        if "Quantization" in self.optimizations and self.quant_dtype == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("Enter a dtype for quantization")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return
                
        if self.optimizations and self.data_loader_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("Please enter a data loader at the start window")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return        
    
    
        if "Quantization" in self.optimizations:
            if self.Window3.quant_int.isChecked():
                self.quant_dtype = "int"
            elif self.Window3.quant_float.isChecked():
                self.quant_dtype = "float"
            else:
                print("No datatype for quantization is selected")
        if "Knowledge_Distillation" in self.optimizations:
            self.Know_Dis_1 = int(self.Window3.Dis_1.text())
            self.Know_Dis_2 = int(self.Window3.Dis_2.text())
        if "Huffman_Coding" in self.optimizations:
            self.Huffman_1 = int(self.Window3.Huf_1.text())
            self.Huffman_2 = int(self.Window3.Huf_2.text())
        print(self.prun_factor_dense, self.prun_factor_conv)
        print(self.quant_dtype)
        print(self.Know_Dis_1, self.Know_Dis_2)
        print(self.Huffman_1, self.Huffman_2)
        
        if self.optimizations and self.data_loader_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("Please enter a data loader at the start window")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            
            return       
    
    self.Window5 = UILoadWindow(self.FONT_STYLE, self.model_path, self.project_name, self.output_path, self.data_loader_path, self.prun_factor_dense, self.prun_factor_conv, self.optimizations,self.target, self)
    
    #self.Window5.Back.clicked.connect(lambda:self.RestrictionWindow("Back"))
    self.Window5.Back.clicked.connect(lambda:self.OptiWindow("Back", self.target))
    
    self.Window5.Load.clicked.connect(self.model_pruning)
    self.Window5.Load.clicked.connect(self.download)
    
    #self.Window5.prune_model.request_signal.connect(self.download)
    self.Window5.conv_build_load.request_signal.connect(self.terminate_thread)
    
    self.Window5.Finish.clicked.connect(self.close)
    
    self.setCentralWidget(self.Window5)
    self.show()