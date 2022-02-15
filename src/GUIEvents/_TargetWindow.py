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
    
    self.Window2.uC.clicked.connect(lambda:nextWindow(self, "Next", "uC"))
    self.Window2.FPGA.clicked.connect(lambda:nextWindow(self, "Next", "FPGA"))
    self.Window2.EmbeddedPC.clicked.connect(lambda:nextWindow(self, "Next", "EmbeddedPC"))
    
    self.Window2.back.clicked.connect(lambda:nextWindow(self, "Back", None))
    
    self.setCentralWidget(self.Window2)
    self.show()



def nextWindow(self, n, target):
    """
    Defines which one is the next window to open.

    Args:
        n:      Go forward or go back
        target: Target to execute the neural network
    """
    if n == "Back":
      self.StartWindow()
    
    elif n == "Next":
      self.target = target
      print(self.target)
      
      if self.target == "uC" or self.target == "FPGA" or self.target == "EmbeddedPC":
          self.OptiWindow()