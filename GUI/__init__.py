import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    from ._MarcusWindow1 import MarcusWindow1
    from ._MarcusWindow2 import MarcusWindow2
    from ._MarcusWindow3 import MarcusWindow3
    from ._MarcusWindow4 import MarcusWindow4
    from ._MarcusWindow5 import MarcusWindow5
    from ._HelperWindow import HelperWindow
    from ._LoadWindow import LoadWindow
    from ._OptiWindow import OptiWindow
    #from ._RestrictionWindow import RestrictionWindow
    from ._SettingsWindow import SettingsWindow
    from ._StartWindow import StartWindow
    from ._TargetWindow import TargetWindow
    from ._TaskWindow import TaskWindow
    from ._ConstraintsWindow import ConstraintsWindow
    from ._ReturnWindow import ReturnWindow
    from ._AutoMLWindow import AutoMLWindow
    
    from ._AutoMLHelper import start_autokeras,get_output_path_ml,get_data_loader_path_ml,Form_clicked,update_draw
    
    
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.setWindowTitle("Neural Network on Microcontroller")
        self.setWindowIcon(QIcon(os.path.join('Images', 'Window_Icon_blue.png')))
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        
        self.FONT_STYLE = "Helvetica"

        self.X=0
        self.Y=0
        self.project_name = None
        self.output_path = None
        self.output_path_ml = None
        self.model_path = None
        self.data_loader_path = None
        self.data_loader_path_ml = None
        self.target = None
        self.optimizations = []
        self.constraints = []
        
        self.prun_factor_dense = None
        self.prun_factor_conv = None
        self.quant_dtype = None
        self.Know_Dis_1 = None
        self.Know_Dis_2 = None
        self.Huffman_1 = None
        self.Huffman_2 = None
        
        self.params_factor = 1
        self.floats_factor = 1
        self.complex_factor = 1
        self.max_size = 0
        self.max_trials = 10
        self.max_epoch = 20
        
        self.params_check = False
        self.floats_check = False
        self.complex_check = False
        
        self.MarcusWindow1()        
        

        
        
    def get_output_path(self, CurWindow):
        self.output_path = QFileDialog.getExistingDirectory(self, 'Select the output path', './')
        CurWindow.Output_Pfad.setText(self.output_path)
        print(CurWindow.Output_Pfad.text())
        
    
        
    def get_model_path(self, CurWindow):
        self.model_path = QFileDialog.getOpenFileName(self, 'Select your model', './')[0]
        CurWindow.Model_Pfad.setText(self.model_path)
        print(CurWindow.Model_Pfad.text())
        
      
    def get_data_loader_path(self, CurWindow):
        self.data_loader_path = QFileDialog.getOpenFileName(self, 'Select your data loader script', './')[0]
        CurWindow.Daten_Pfad.setText(self.data_loader_path)
        print(CurWindow.Daten_Pfad.text())
        
                
        
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
            
    def set_params(self):
        if self.Window3.Params.isChecked() == True:
            if not "Params" in self.constraints:
                self.constraints.append("Params") 
                print(self.constraints)
            if self.params_factor == None:
                self.Window3.Params_factor.setText("1")
            else:
                self.Window3.Params_factor.setText(str(self.params_factor))
            self.Window3.Params_factor.setVisible(True)
            self.Window3.Params_label.setVisible(True)
            
            self.Window3.Params.setIconSize(QSize(100, 100))
            self.Window3.Params.setGeometry(145, 85, 120, 120)
       
        else:
            if "Params" in self.constraints:
                self.constraints.remove("Params")
                print(self.constraints)
            self.params_factor = float(self.Window3.Params_factor.text())
            self.Window3.Params_factor.setVisible(False)
            self.Window3.Params_label.setVisible(False)
            
            self.Window3.Params.setIconSize(QSize(150, 150))
            self.Window3.Params.setGeometry(120, 85, 170, 170)
            
    def set_floats(self):
        if self.Window3.Floats.isChecked() == True:
            if not "Floats" in self.constraints:
                self.constraints.append("Floats") 
                print(self.constraints)
            if self.floats_factor == None:
                self.Window3.Floats_factor.setText("1")
            else:
                self.Window3.Floats_factor.setText(str(self.floats_factor))
            self.Window3.Floats_factor.setVisible(True)
            self.Window3.Floats_label.setVisible(True)
            
            self.Window3.Floats.setIconSize(QSize(100, 100))
            self.Window3.Floats.setGeometry(540, 85, 120, 120)
       
        else:
            if "Floats" in self.constraints:
                self.constraints.remove("Floats")
                print(self.constraints)
            self.floats_factor = float(self.Window3.Floats_factor.text())
            self.Window3.Floats_factor.setVisible(False)
            self.Window3.Floats_label.setVisible(False)
            
            self.Window3.Floats.setIconSize(QSize(150, 150))
            self.Window3.Floats.setGeometry(515, 85, 170, 170)
            
            
    def set_complex(self):
        if self.Window3.Complex.isChecked() == True:
            if not "Complex" in self.constraints:
                self.constraints.append("Complex") 
                print(self.constraints)
            if self.complex_factor == None:
                self.Window3.Complex_factor.setText("1")
            else:
                self.Window3.Complex_factor.setText(str(self.complex_factor))
            self.Window3.Complex_factor.setVisible(True)
            self.Window3.Complex_label.setVisible(True)
            
            self.Window3.Complex.setIconSize(QSize(100, 100))
            self.Window3.Complex.setGeometry(145, 320, 120, 120)
       
        else:
            if "Complex" in self.constraints:
                self.constraints.remove("Complex")
                print(self.constraints)
            self.complex_factor = float(self.Window3.Complex_factor.text())
            self.Window3.Complex_factor.setVisible(False)
            self.Window3.Complex_label.setVisible(False)
            
            self.Window3.Complex.setIconSize(QSize(150, 150))
            self.Window3.Complex.setGeometry(120, 320, 170, 170)
            
            
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
                
        if "FPGA" in self.target:
            try:
                self.Window5.prune_model.stop_thread()
                print("To FPGA start")
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
            