import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.GUILayout.UIHelperWindow import *
        
def HelperWindow(self):        
    self.setFixedWidth(800)
    self.setFixedHeight(900)
    self.Window3a = UIHelperWindow(self.FONT_STYLE, self)
    
    
    
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
    
    
    self.Window3a.Back.clicked.connect(lambda:self.TargetWindow("Back", self.Window3a))
    self.Window3a.Next.clicked.connect(lambda:self.OptiWindow("Next","?"))
    
    self.setCentralWidget(self.Window3a)
    
    self.Dot = QLabel(self)
    Dotimg = QPixmap(os.path.join('src','GUILayout','Images', 'Dot.png'))
    self.Dot.setFixedSize(30, 30)
    self.Dot.setScaledContents(True)
    self.Dot.setPixmap(Dotimg)
    self.Dot.setVisible(False)
    
    
    self.show()