import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from UIWindows.UIReturnWindow import *



        
def ReturnWindow(self, n):         
    
    if n == "Next":
        self.start_autokeras()
  
    
    self.Window6 = UIReturnWindow(self.FONT_STYLE, self)
    
    self.Window6.Back.clicked.connect(lambda:self.AutoMLWindow("Back"))
    self.Window6.Load.clicked.connect(lambda:self.MarcusWindow1())         
   
    self.Window6.Finish.clicked.connect(self.close)
    

    self.setCentralWidget(self.Window6)
    self.show()