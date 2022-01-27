"""This is a splittet method from the Mainwindow class which contain the logic for the TargetWindow window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

from src.GUILayout.UITargetWindow import *

def TargetWindow(self, n, LastWindow):
    """Define Logic for the TargetWindow GUI

    Retrieves the parameter class and set the data path, project path and output path

    Args:
      self:
        self represents the instance of the class.
      parameter:
        A parameter class with all the parameter we change and need to start the project
      

    Returns:


    Raises:
      IOError: An error occurred accessing the parameterset.
    """
    
    if n == "Next":
        
        self.project_name = LastWindow.Projekt_Name.text()
        self.output_path = LastWindow.Output_Pfad.text()
        self.model_path = LastWindow.Model_Pfad.text()
        self.data_loader_path = LastWindow.Daten_Pfad.text() 
            
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
            try:                
                self.prun_factor_dense = int(LastWindow.Pruning_Dense.text())
                self.prun_factor_conv = int(LastWindow.Pruning_Conv.text())
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                 
                msg.setText("Please enter a number for pruning or disable it.")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return
            
        if "Knowledge_Distillation" in self.optimizations:
            try:                
                self.Know_Dis_1 = int(LastWindow.Dis_1.text())
                self.Know_Dis_2 = int(LastWindow.Dis_2.text())
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                 
                msg.setText("Please enter a number for Knowledge Distillation or disable it.")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return
        if "Huffman_Coding" in self.optimizations:
            try:                
                self.Huffman_1 = int(LastWindow.Huf_1.text())
                self.Huffman_2 = int(LastWindow.Huf_2.text())
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                 
                msg.setText("Please enter a number for Huffman Coding or disable it.")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return

    print(self.model_path)
    print(self.data_loader_path)
    
    
    self.Window2 = UITargetWindow(self.FONT_STYLE, self)
    
    
    self.Window2.uC.clicked.connect(lambda:self.OptiWindow("Next","uC"))
    self.Window2.FPGA.clicked.connect(lambda:self.OptiWindow("Next","FPGA"))
    # self.Window2.DK.clicked.connect(lambda:self.HelperWindow())
    
    self.Window2.Back.clicked.connect(self.StartWindow)
    
    self.setCentralWidget(self.Window2)
    self.show()