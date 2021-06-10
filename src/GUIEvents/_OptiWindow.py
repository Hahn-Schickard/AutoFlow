"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLData window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
from src.GUILayout.UIOptiWindow import *
        
def OptiWindow(self, n, target):
    
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

    self.Window3 = UIOptiWindow(self.FONT_STYLE, self)
    
    if "Pruning" in self.optimizations:
        self.Window3.Pruning.setChecked(True)
        self.set_pruning(self.Window3)
        self.Window3.Pruning_Dense.setText(str(self.prun_factor_dense))
        self.Window3.Pruning_Conv.setText(str(self.prun_factor_conv))
    if "Quantization" in self.optimizations:
        self.Window3.Quantization.setChecked(True)
        self.set_quantization(self.Window3)
        if self.quant_dtype != None:
            if "int8 with float fallback" in self.quant_dtype:
                self.Window3.quant_int_only.setChecked(False)  
                self.Window3.quant_int.setChecked(True)              
            elif "int8 only" in self.quant_dtype:
                self.Window3.quant_int_only.setChecked(True)  
                self.Window3.quant_int.setChecked(False) 
    """            
    if "Knowledge_Distillation" in self.optimizations:
        self.Window3.Dis.setChecked(True)
        self.set_knowledge_distillation(self.Window3)
        self.Window3.Dis_1.setText(str(self.Know_Dis_1))
        self.Window3.Dis_2.setText(str(self.Know_Dis_2))
    if "Huffman_Coding" in self.optimizations:
        self.Window3.Huf.setChecked(True)
        self.set_huffman_coding(self.Window3)
        self.Window3.Huf_1.setText(str(self.Huffman_1))
        self.Window3.Huf_2.setText(str(self.Huffman_2))
    """    
    self.Window3.Pruning.toggled.connect(lambda:self.set_pruning(self.Window3))
    self.Window3.Quantization.toggled.connect(lambda:self.set_quantization(self.Window3))
    #self.Window3.Dis.toggled.connect(lambda:self.set_knowledge_distillation(self.Window3))
    #self.Window3.Huf.toggled.connect(lambda:self.set_huffman_coding(self.Window3))
    
    self.Window3.quant_int.clicked.connect(lambda:self.set_quant_dtype("int8 with float fallback", self.Window3))
    self.Window3.quant_int_only.clicked.connect(lambda:self.set_quant_dtype("int8 only", self.Window3))
    
    self.Window3.Back.clicked.connect(lambda:self.TargetWindow("Back", self.Window3))
    self.Window3.Next.clicked.connect(lambda:self.LoadWindow("Next"))
    
    self.setCentralWidget(self.Window3)
    self.show()