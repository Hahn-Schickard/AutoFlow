''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from src.GUILayout.UITargetWindow import *

def TargetWindow(self):
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
    
    self.Window2 = UITargetWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)
    
    self.Window2.uC.clicked.connect(lambda:nextWindow(self, "uC"))
    self.Window2.FPGA.clicked.connect(lambda:nextWindow(self, "FPGA"))
    self.Window2.EmbeddedPC.clicked.connect(lambda:nextWindow(self, "EmbeddedPC"))
    
    self.Window2.Back.clicked.connect(self.StartWindow)
    
    self.setCentralWidget(self.Window2)
    self.show()



def nextWindow(self, target):
    self.target = target
    
    if self.target == "uC" or self.target == "FPGA" or self.target == "EmbeddedPC":
        self.OptiWindow()