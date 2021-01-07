import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Threads.Loading_images_thread import * 
from Threads.Create_project_thread import *
from Threads.Prune_model_thread import *



class UIAutoMLWindow(QWidget):
    def __init__(self, parent=None):
        super(UIAutoMLWindow, self).__init__(parent)
                
        self.label = QLabel("AutoML")
        self.label.setFont(QFont("AutoML", 12))
        self.label.setAlignment(Qt.AlignCenter)
        
        self.info = QLabel("Start the AutoML Process:")
        self.info.setFont(QFont("Start the AutoML Process:", 12))
        self.info.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel()
        self.Abstand.setFixedHeight(30)
        
        self.Abstand_v = QLabel()
        self.Abstand_v.setFixedHeight(160)
        
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar', 'GUI_step_6.png'))
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setFixedHeight(30)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.Finish = QPushButton("Finish", self)
        self.Finish.setFont(QFont("Finish", 12))
        self.Finish.setFixedWidth(125)
        self.Finish.setToolTip('...')
        self.Finish.setVisible(False)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(25, 25))
        self.Back.setFixedHeight(30)

        
        self.Start = QPushButton(self)
        self.Start.setIcon(QIcon(os.path.join('Images', 'start.png')))
        self.Start.setIconSize(QSize(160, 160))
        self.Start.setToolTip('...')
        self.Start.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.info)
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.Start)
        self.horizontal_box[1].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.Finish)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.Abstand_v)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.Schritt, 0, 1)
        sublayout.addWidget(self.Abstand, 0, 2)
        self.horizontal_box[4].addLayout(sublayout)
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)
        

        
       
      