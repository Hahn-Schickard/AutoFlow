import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Threads.Loading_images_thread import * 
from Threads.Create_project_thread import *
from Threads.Prune_model_thread import *



class UIReturnWindow(QWidget):
    def __init__(self, parent=None):
        super(UIReturnWindow, self).__init__(parent)
                
        self.label = QLabel("End")
        self.label.setFont(QFont("End", 12))
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel()
        self.Abstand.setFixedHeight(100)
        
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar', 'GUI_step_7.png'))
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setFixedHeight(30)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.Finish = QPushButton("Finish", self)
        self.Finish.setFont(QFont("Finish", 12))
        self.Finish.setFixedWidth(125)
        self.Finish.setVisible(False)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(25, 25))
        self.Back.setFixedHeight(30)

        self.Load = QPushButton(self)
        self.Load.setIcon(QIcon(os.path.join('Images', 'Next_arrow.png')))
        self.Load.setIconSize(QSize(25, 25))
        self.Load.setFixedHeight(30)
        
        self.info1 = QLabel("Check if the Process is running.")
        self.info1.setFont(QFont("Check if the Process is running.", 12))
        self.info1.setAlignment(Qt.AlignCenter)
        
        self.info2 = QLabel("Return to Start Screen by pressing the right arrow button.")
        self.info2.setFont(QFont("Return to Start Screen by pressing the right arrow button.", 12))
        self.info2.setAlignment(Qt.AlignCenter)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addWidget(self.Abstand)
        self.horizontal_box[1].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.info1)
        self.horizontal_box[2].addStretch()

        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.info2)
        self.horizontal_box[3].addStretch()

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addWidget(self.Abstand)
        self.horizontal_box[4].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addWidget(self.Finish)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[6].addWidget(self.Back)
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addWidget(self.Schritt) 
        self.horizontal_box[6].addStretch()         
        self.horizontal_box[6].addWidget(self.Load)
        self.horizontal_box[6].setAlignment(Qt.AlignBottom)
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)
        
        
       
      