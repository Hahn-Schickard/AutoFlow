import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from UIWindows.UIHelperWindow import *
from UIWindows.UILoadWindow import *
from UIWindows.UIOptiWindow import *
from UIWindows.UIRestrictionWindow import *
from UIWindows.UIStartWindow import *
from UIWindows.UITargetWindow import *
from UIWindows.UIMarcusWindow1 import *
from UIWindows.UIMarcusWindow2 import *
from UIWindows.UIMarcusWindow3 import *
from UIWindows.UIMarcusWindow4 import *
from UIWindows.UIMarcusWindow5 import *


from Threads.Loading_images_thread import *
from Threads.Create_project_thread import *
from Threads.Prune_model_thread import *



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.setWindowTitle("Neural Network on Microcontroller")
        self.setWindowIcon(QIcon(os.path.join('Images', 'Window_Icon_blue.png')))
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        
        self.X=0
        self.Y=0
        self.project_name = None
        self.output_path = None
        self.model_path = None
        self.data_loader_path = None
        self.target = None
        self.optimizations = []
        
        self.prun_factor_dense = None
        self.prun_factor_conv = None
        self.quant_dtype = None
        self.Know_Dis_1 = None
        self.Know_Dis_2 = None
        self.Huffman_1 = None
        self.Huffman_2 = None
        
        self.MarcusWindow1()
    
    def MarcusWindow1(self):
        
        self.Window1a = UIMarcusWindow1(self)
        
        self.Window1a.load_model.clicked.connect(self.MarcusWindow4)
        self.Window1a.train_model.clicked.connect(self.MarcusWindow2)
        
        self.setCentralWidget(self.Window1a)
        self.show()

    
    def MarcusWindow2(self):
        
        self.Window1b = UIMarcusWindow2(self)
        
        self.Window1b.uC.clicked.connect(self.StartWindow)
        self.Window1b.FPGA.clicked.connect(self.MarcusWindow3)
        self.Window1b.Back.clicked.connect(self.MarcusWindow1)
        
        self.setCentralWidget(self.Window1b)
        self.show()
        
        
    def MarcusWindow3(self):
        
        self.Window1c = UIMarcusWindow3(self)
        
        if self.output_path != None:
            self.Window1c.Output_Pfad.setText(self.output_path)
        
        if self.project_name != None:
            self.Window1c.Projekt_Name.setText(self.project_name)
        
        if self.model_path != None:
            self.Window1c.Model_Pfad.setText(self.model_path)
        
        if self.data_loader_path != None:
            self.Window1c.Daten_Pfad.setText(self.data_loader_path)

        print(self.model_path)
        
        self.Window1c.Output_Pfad_Browse.clicked.connect(self.get_output_path)
        self.Window1c.Modell_einlesen_Browse.clicked.connect(self.get_model_path)
        self.Window1c.Daten_einlesen_Browse.clicked.connect(self.get_data_loader_path)
        self.Window1c.Next.clicked.connect(lambda:self.TargetWindow("Next"))
        self.Window1c.Back.clicked.connect(self.MarcusWindow2)
        
        self.setCentralWidget(self.Window1c)
        self.show()
        
        
    def MarcusWindow4(self):
        
        self.Window1d = UIMarcusWindow4(self)
        
        if self.output_path != None:
            self.Window1d.Output_Pfad.setText(self.output_path)
        
        if self.project_name != None:
            self.Window1d.Projekt_Name.setText(self.project_name)
        
        if self.model_path != None:
            self.Window1d.Model_Pfad.setText(self.model_path)
        
        if self.data_loader_path != None:
            self.Window1d.Daten_Pfad.setText(self.data_loader_path)

        print(self.model_path)
        
        self.Window1d.Output_Pfad_Browse.clicked.connect(self.get_output_path)
        self.Window1d.Modell_einlesen_Browse.clicked.connect(self.get_model_path)
        self.Window1d.Daten_einlesen_Browse.clicked.connect(self.get_data_loader_path)
        self.Window1d.Next.clicked.connect(self.MarcusWindow5)
        self.Window1d.Back.clicked.connect(self.MarcusWindow1)
        
        self.setCentralWidget(self.Window1d)
        self.show()
        
    
    def MarcusWindow5(self):
        
        self.Window1e = UIMarcusWindow5(self)
        
        self.Window1e.Back.clicked.connect(self.MarcusWindow4)
        
        #self.Window1e.Load.clicked.connect(self.model_pruning)
        #self.Window1e.Load.clicked.connect(self.download)
        
        self.setCentralWidget(self.Window1e)
        self.show()


    def StartWindow(self):
        self.Window1 = UIStartWindow(self)
        
        if self.output_path != None:
            self.Window1.Output_Pfad.setText(self.output_path)
        
        if self.project_name != None:
            self.Window1.Projekt_Name.setText(self.project_name)
        
        if self.model_path != None:
            self.Window1.Model_Pfad.setText(self.model_path)
        
        if self.data_loader_path != None:
            self.Window1.Daten_Pfad.setText(self.data_loader_path)

        
        self.Window1.Output_Pfad_Browse.clicked.connect(self.get_output_path)
        self.Window1.Modell_einlesen_Browse.clicked.connect(self.get_model_path)
        self.Window1.Daten_einlesen_Browse.clicked.connect(self.get_data_loader_path)
        
        self.Window1.Next.clicked.connect(lambda:self.TargetWindow("Next"))
        self.Window1.Back.clicked.connect(self.MarcusWindow2)
        
        self.setCentralWidget(self.Window1)
        self.show()
        
        
    def TargetWindow(self, n):
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        
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
        
        
        self.Window2 = UITargetWindow(self)
        
        
        self.Window2.uC.clicked.connect(lambda:self.OptiWindow("Next","uC"))
        self.Window2.FPGA.clicked.connect(lambda:self.OptiWindow("Next","FPGA"))
        self.Window2.DK.clicked.connect(lambda:self.HelperWindow())
        
        self.Window2.Back.clicked.connect(self.StartWindow)
        
        self.setCentralWidget(self.Window2)
        self.show()
            
        
    def HelperWindow(self):        
        self.setFixedWidth(800)
        self.setFixedHeight(900)
        self.Window3a = UIHelperWindow(self)
        
        
        
        self.Window3a.Forms.clicked.connect(self.Form_clicked)
        self.Window3a.Formm.clicked.connect(self.Form_clicked)
        self.Window3a.Forml.clicked.connect(self.Form_clicked)
        self.Window3a.Energies.clicked.connect(self.Form_clicked)
        self.Window3a.Energiem.clicked.connect(self.Form_clicked)
        self.Window3a.Energiel.clicked.connect(self.Form_clicked)
        self.Window3a.Flexs.clicked.connect(self.Form_clicked)
        self.Window3a.Flexm.clicked.connect(self.Form_clicked)
        self.Window3a.Flexl.clicked.connect(self.Form_clicked)
        self.Window3a.Preiss.clicked.connect(self.Form_clicked)
        self.Window3a.Preism.clicked.connect(self.Form_clicked)
        self.Window3a.Preisl.clicked.connect(self.Form_clicked)
        self.Window3a.Parameter.textChanged.connect(self.Form_clicked)
        self.Window3a.FPS.textChanged.connect(self.Form_clicked)
        
        
        self.Window3a.Back.clicked.connect(lambda:self.TargetWindow("Back"))
        self.Window3a.Next.clicked.connect(lambda:self.OptiWindow("Next","?"))
        
        self.setCentralWidget(self.Window3a)
        
        self.Dot = QLabel(self)
        Dotimg = QPixmap(os.path.join('Images', 'Dot.png'))
        self.Dot.setFixedSize(30, 30)
        self.Dot.setScaledContents(True)
        self.Dot.setPixmap(Dotimg)
        self.Dot.setVisible(False)
        
        
        self.show()
        
        
    def OptiWindow(self, n, target):
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        
        if n == "Next":
            self.target = target
            print(self.target)
            
            if self.target == "?":
                self.Dot.setVisible(False)
            if self.target == None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                 
                msg.setText("Please choose a target")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                
                return

        self.Window3 = UIOptiWindow(self)
        
        if "Pruning" in self.optimizations:
            self.Window3.Pruning.setChecked(True)
            self.set_pruning()
            self.Window3.Pruning_Dense.setText(str(self.prun_factor_dense))
            self.Window3.Pruning_Conv.setText(str(self.prun_factor_conv))
        if "Quantization" in self.optimizations:
            self.Window3.Quantization.setChecked(True)
            self.set_quantization()
            if self.quant_dtype != None:
                if "float" in self.quant_dtype:
                    self.Window3.quant_int.setChecked(False)  
                    self.Window3.quant_float.setChecked(True)              
                elif "int" in self.quant_dtype:
                    self.Window3.quant_int.setChecked(True)  
                    self.Window3.quant_float.setChecked(False) 
        if "Knowledge_Distillation" in self.optimizations:
            self.Window3.Dis.setChecked(True)
            self.set_knowledge_distillation()
            self.Window3.Dis_1.setText(str(self.Know_Dis_1))
            self.Window3.Dis_2.setText(str(self.Know_Dis_2))
        if "Huffman_Coding" in self.optimizations:
            self.Window3.Huf.setChecked(True)
            self.set_huffman_coding()
            self.Window3.Huf_1.setText(str(self.Huffman_1))
            self.Window3.Huf_2.setText(str(self.Huffman_2))
            
        self.Window3.Pruning.toggled.connect(self.set_pruning)
        self.Window3.Quantization.toggled.connect(self.set_quantization)
        self.Window3.Dis.toggled.connect(self.set_knowledge_distillation)
        self.Window3.Huf.toggled.connect(self.set_huffman_coding)
        
        self.Window3.quant_float.clicked.connect(lambda:self.set_quant_dtype("float"))
        self.Window3.quant_int.clicked.connect(lambda:self.set_quant_dtype("int"))
        
        self.Window3.Back.clicked.connect(lambda:self.TargetWindow("Back"))
        self.Window3.Next.clicked.connect(lambda:self.RestrictionWindow("Next"))
        
        self.setCentralWidget(self.Window3)
        self.show()
        
        
    def RestrictionWindow(self, n):            
        
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

        self.Window4 = UIRestrictionWindow(self)
        
        self.Window4.Back.clicked.connect(lambda:self.OptiWindow("Back", self.target))
        self.Window4.Next.clicked.connect(self.LoadWindow)
        
        self.setCentralWidget(self.Window4)
        self.show()
        
        
    def LoadWindow(self):         
        
        self.Window5 = UILoadWindow(self.model_path, self.project_name, self.output_path, self.data_loader_path, self.prun_factor_dense, self.prun_factor_conv, self.optimizations, self)
        
        self.Window5.Back.clicked.connect(lambda:self.RestrictionWindow("Back"))
        
        self.Window5.Load.clicked.connect(self.model_pruning)
        self.Window5.Load.clicked.connect(self.download)
        
        #self.Window5.prune_model.request_signal.connect(self.download)
        self.Window5.conv_build_load.request_signal.connect(self.terminate_thread)
        
        self.Window5.Finish.clicked.connect(self.close)
        
        print("LUL")
        print(self.Window5.Load.height())
        
        self.setCentralWidget(self.Window5)
        self.show()
            
        
        
        
        
    def get_output_path(self):
        self.output_path = QFileDialog.getExistingDirectory(self, 'Select the output path', './')
        self.Window1.Output_Pfad.setText(self.output_path)
        print(self.Window1.Output_Pfad.text())
        
        
        
    def get_model_path(self):
        self.model_path = QFileDialog.getOpenFileName(self, 'Select your model', './')[0]
        self.Window1.Model_Pfad.setText(self.model_path)
        print(self.Window1.Model_Pfad.text())
        
      
      
    def get_data_loader_path(self):
        self.data_loader_path = QFileDialog.getOpenFileName(self, 'Select your data loader script', './')[0]
        self.Window1.Daten_Pfad.setText(self.data_loader_path)
        print(self.Window1.Daten_Pfad.text())
        
        
    def set_pruning(self):
        if self.Window3.Pruning.isChecked() == True:
            if not "Pruning" in self.optimizations:
                self.optimizations.append("Pruning") 
                print(self.optimizations)
            if self.prun_factor_dense == None and self.prun_factor_conv == None:
                self.Window3.Pruning_Dense.setText("10")
                self.Window3.Pruning_Conv.setText("10")
            else:
                self.Window3.Pruning_Dense.setText(str(self.prun_factor_dense))
                self.Window3.Pruning_Conv.setText(str(self.prun_factor_conv))
            self.Window3.Pruning_Dense.setVisible(True)
            self.Window3.Pruning_Conv.setVisible(True)
            self.Window3.Pruning_Conv_label.setVisible(True)
            self.Window3.Pruning_Dense_label.setVisible(True)
            
            self.Window3.Pruning.setIconSize(QSize(100, 100))
            self.Window3.Pruning.setGeometry(145, 85, 120, 120)
       
        else:
            if "Pruning" in self.optimizations:
                self.optimizations.remove("Pruning")
                print(self.optimizations)
            self.prun_factor_dense = int(self.Window3.Pruning_Dense.text())
            self.prun_factor_conv = int(self.Window3.Pruning_Conv.text())
            self.Window3.Pruning_Dense.setVisible(False)
            self.Window3.Pruning_Conv.setVisible(False)
            self.Window3.Pruning_Conv_label.setVisible(False)
            self.Window3.Pruning_Dense_label.setVisible(False)
            
            self.Window3.Pruning.setIconSize(QSize(150, 150))
            self.Window3.Pruning.setGeometry(120, 85, 170, 170)
            
            
    def set_quantization(self):
        if self.Window3.Quantization.isChecked() == True:
            if not "Quantization" in self.optimizations:
                self.optimizations.append("Quantization") 
                print(self.optimizations) 
            if self.quant_dtype != None:
                if "float" in self.quant_dtype:
                    self.Window3.quant_int.setChecked(False)  
                    self.Window3.quant_float.setChecked(True)              
                elif "int" in self.quant_dtype:
                    self.Window3.quant_int.setChecked(True)  
                    self.Window3.quant_float.setChecked(False)   
            self.Window3.quant_float.setVisible(True)
            self.Window3.quant_int.setVisible(True)
            
            self.Window3.Quantization.setIconSize(QSize(100, 100))
            self.Window3.Quantization.setGeometry(540, 85, 120, 120)
            
        else:
            if "Quantization" in self.optimizations:
                self.optimizations.remove("Quantization") 
                print(self.optimizations)
            self.Window3.quant_float.setChecked(False)
            self.Window3.quant_int.setChecked(False)
            self.Window3.quant_float.setVisible(False)
            self.Window3.quant_int.setVisible(False)
            
            self.Window3.Quantization.setIconSize(QSize(150, 150))
            self.Window3.Quantization.setGeometry(515, 85, 170, 170)
            
            
    def set_quant_dtype(self, dtype):
        if "float" in dtype:
            self.Window3.quant_int.setChecked(False)
            if self.Window3.quant_float.isChecked() == False:
                self.quant_dtype = None
            else:
                self.quant_dtype = dtype
        elif "int" in dtype:
            self.Window3.quant_float.setChecked(False)
            if self.Window3.quant_int.isChecked() == False:
                self.quant_dtype = None
            else:
                self.quant_dtype = dtype
        
        
            
    def set_knowledge_distillation(self):
        if self.Window3.Dis.isChecked() == True:
            if not "Knowledge_Distillation" in self.optimizations:
                self.optimizations.append("Knowledge_Distillation")   
                print(self.optimizations)           
            self.Window3.Dis_1.setText("10")
            self.Window3.Dis_2.setText("10")           
            self.Window3.Dis_1.setVisible(True)
            self.Window3.Dis_2.setVisible(True)
            self.Window3.Dis_1_label.setVisible(True)
            self.Window3.Dis_2_label.setVisible(True)
            
            self.Window3.Dis.setIconSize(QSize(100, 100))
            self.Window3.Dis.setGeometry(145, 320, 120, 120)
            
        else:
            if "Knowledge_Distillation" in self.optimizations:
                self.optimizations.remove("Knowledge_Distillation") 
                print(self.optimizations)
            self.Window3.Dis_1.setVisible(False)
            self.Window3.Dis_2.setVisible(False)
            self.Window3.Dis_1_label.setVisible(False)
            self.Window3.Dis_2_label.setVisible(False)
            
            self.Window3.Dis.setIconSize(QSize(150, 150))
            self.Window3.Dis.setGeometry(120, 320, 170, 170)
            
            
    def set_huffman_coding(self):
        if self.Window3.Huf.isChecked() == True:
            if not "Huffman_Coding" in self.optimizations:
                self.optimizations.append("Huffman_Coding")  
                print(self.optimizations)   
            self.Window3.Huf_1.setText("10")
            self.Window3.Huf_2.setText("10")
            self.Window3.Huf_1.setVisible(True)
            self.Window3.Huf_2.setVisible(True)
            self.Window3.Huf_1_label.setVisible(True)
            self.Window3.Huf_2_label.setVisible(True)
            
            self.Window3.Huf.setIconSize(QSize(100, 100))
            self.Window3.Huf.setGeometry(540, 320, 120, 120)
            
        else:
            if "Huffman_Coding" in self.optimizations:
                self.optimizations.remove("Huffman_Coding") 
                print(self.optimizations)
            self.Window3.Huf_1.setVisible(False)
            self.Window3.Huf_2.setVisible(False)
            self.Window3.Huf_1_label.setVisible(False)
            self.Window3.Huf_2_label.setVisible(False)
            
            self.Window3.Huf.setIconSize(QSize(150, 150))
            self.Window3.Huf.setGeometry(515, 320, 170, 170)
            
        
        
    def Form_clicked(self):
        self.X=0
        self.Y=0
        
        self.Dot.setVisible(True)
        if self.Window3a.Parameter.text() == "":
            Parameter=0
            
        else:
            Parameter = self.Window3a.Parameter.text()
            Parameter=int(Parameter)
        
        if self.Window3a.FPS.text() == "":
            FPS=0
            
        else:
            FPS = self.Window3a.FPS.text()
            FPS=int(FPS)
            
        FLOPs=Parameter*FPS
        print(FLOPs)
        
        if FLOPs < 10000000000:
            self.Y+=100
        if FLOPs > 100000000000:
            self.Y-=100
        
        if self.Window3a.Forms.isChecked():  
            self.Y+=100
            
        if self.Window3a.Forml.isChecked():  
            self.Y+=-100
               
        if self.Window3a.Flexs.isChecked():  
            self.X+=200
            
        if self.Window3a.Flexl.isChecked():  
            self.X+=-200
   
        if self.Window3a.Energies.isChecked():  
            self.Y+=50
            self.X+=50

        if self.Window3a.Energiel.isChecked():  
            self.Y+=-50
            self.X+=-50
            
        if self.Window3a.Preiss.isChecked():  
            self.Y+=50
            self.X+=50

        if self.Window3a.Preisl.isChecked():  
            self.Y+=-50
            self.X+=-50
                
        if self.Window3a.Preism.isChecked():  
            if self.X > 0:
                self.X-=25
            if self.X < 0:
                self.X+=25
            if self.Y > 0:
                self.Y-=25
            if self.Y < 0:
                self.Y+=25
                
        if self.Window3a.Energiem.isChecked():  
            if self.X > 0:
                self.X-=25
            if self.X < 0:
                self.X+=25
            if self.Y > 0:
                self.Y-=25
            if self.Y < 0:
                self.Y+=25
                
        if self.Window3a.Formm.isChecked():  
            if self.Y > 0:
                self.Y-=25
            if self.Y < 0:
                self.Y+=25
                
        if self.Window3a.Flexm.isChecked():
            if self.X > 0:
                self.X-=100     
            if self.X < 0:
                self.X+=100
                
        print('vor:')        
        print('y')
        print(self.Y)
        print('x')
        print(self.X)
        
        
        if self.Y > 200:
            self.Y=200
        if self.Y < -200:
            self.Y=-200
            
        if self.X > 200:
            self.X=200
        if self.X < -200:
            self.X=-200
            
                
        if self.X > 0:
            self.X=self.X-((math.sqrt(self.Y*self.Y))*0.5)
        if self.X < 0:
            self.X=self.X+((math.sqrt(self.Y*self.Y))*0.5)
        
        
        
        print('y')
        print(self.Y)
        print('x')
        print(self.X)    
        
        
        self.update_draw(self.X,self.Y)
        
#11Tflops
#1GF
        
        
    def update_draw(self,x,y):
        x=390+x
        y=540+y
        
        self.Dot.move(x,y)
        
        
        
        
    def get_optimization(self, button):
        
        if button.text() == "Pruning":
            if button.isChecked() == True:
                if not "Pruning" in self.optimizations:
                    self.optimizations.append(button.text())
                #print(button.text()+" is selected")
            else:
                if "Pruning" in self.optimizations:
                    self.optimizations.remove(button.text())
                #print(button.text()+" is deselected")
                
        if button.text() == "Quantization":
            if button.isChecked() == True:
                if not "Quantization" in self.optimizations:
                    self.optimizations.append(button.text())
                #print(button.text()+" is selected")
            else:
                if "Quantization" in self.optimizations:
                    self.optimizations.remove(button.text())
                #print(button.text()+" is deselected")
        
        print(self.optimizations)
        
        
    def set_optimizations(self, optimizations):
        if "Pruning" in optimizations:
            self.Window3.b[0].setChecked(True)
            
        if "Quantization" in optimizations:
            self.Window3.b[1].setChecked(True)
    
    
    def model_pruning(self):
        self.Window5.Back.setVisible(False)
        self.Window5.Load.setVisible(False)
        
        self.Window5.loading_images.start()
        #self.Window5.prune_model.start()        
    
            
    def download(self):
        
        if "uC" in self.target:
            try:
                self.Window5.prune_model.stop_thread()
                print("To uC start")
                self.Window5.conv_build_load.start()
            except:
                print("Error")
                
    def terminate_thread(self):
        
        if "uC" in self.target:
            try:
                print("uC stop")
                self.Window5.loading_images.stop_thread()
                self.Window5.conv_build_load.stop_thread()
                self.Window5.Finish.setVisible(True)
                self.Window5.Loadpng.setPixmap(QPixmap(os.path.join('Images','GUI_loading_images', 'GUI_load_finish.png')))
            except:
                print("Error")
    
            
            
            
            
    def optimization_before_load(self):
        if "Pruning" in self.optimizations:
            
            sys.path.append(self.data_loader_path)
            datascript = __import__(os.path.splitext(os.path.basename(self.data_loader_path))[0])
            
            x_train, y_train, x_test, y_test = get_data()
            pruned_model = pruning(self.model_path, x_train, y_train, prun_factor_dense, prun_factor_conv)
            
    #def closeEvent(self, event):
    #    msg = "Do you want to exit the application?"
    #    reply = QMessageBox.question(self, 'Message', msg, QMessageBox.Yes, QMessageBox.No)
            
     
        
    

app = QApplication(sys.argv)




# Force the style to be the same on all OSs:
app.setStyle("Fusion")

# Now use a palette to switch to dark colors:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)

app.setStyleSheet("QPushButton:pressed { background-color: rgb(10, 100, 200) }" "QPushButton:checked { background-color: rgb(10, 100, 200) }" "QPushButton::hover { background-color : rgb(10, 100, 200)}" )

w = MainWindow()
w.show()
#w.setFixedSize(w.size())
sys.exit(app.exec_())
