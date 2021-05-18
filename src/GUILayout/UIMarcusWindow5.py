import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.Threads.Loading_images_thread import * 
from src.Threads.Create_project_thread import *
from src.Threads.Prune_model_thread import *



class UIMarcusWindow5(QWidget):
    def __init__(self, FONT_STYLE, parent=None):
        super(UIMarcusWindow5, self).__init__(parent)
        
        
        self.FONT_STYLE = FONT_STYLE        
        
        self.label = QLabel("Training")
        self.label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel()
        self.Abstand.setFixedHeight(30)
        
        self.Loadpng = QLabel(self)
        img = QPixmap(os.path.join('Images','GUI_loading_images', 'GUI_load_0.png'))
        self.Loadpng.setPixmap(img)
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar', 'GUI_step_3.png'))
        self.Schritt.setFixedHeight(30)
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.Finish = QPushButton("Finish", self)
        self.Finish.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Finish.setFixedWidth(125)
        self.Finish.setVisible(False)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(25, 25))
        self.Back.setFixedHeight(30)

        self.Load = QPushButton(self)
        self.Load.setIcon(QIcon(os.path.join('Images', 'load_arrow.png')))
        self.Load.setIconSize(QSize(25, 25))
        self.Load.setFixedHeight(30)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.Loadpng)
        self.horizontal_box[1].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.Finish)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.Back)        
        self.horizontal_box[3].addStretch()
        self.horizontal_box[3].addWidget(self.Schritt) 
        self.horizontal_box[3].addStretch()         
        self.horizontal_box[3].addWidget(self.Load)
        self.horizontal_box[3].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)