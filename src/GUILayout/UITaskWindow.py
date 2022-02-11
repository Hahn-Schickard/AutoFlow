''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UITaskWindow(QWidget):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UITaskWindow, self).__init__(parent)
        
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE
        
        self.label = QLabel("Choose your Task")
        self.label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        
        self.Abstand_button = QLabel()
        self.Abstand_button.setFixedWidth(0.02*self.WINDOW_HEIGHT)
        self.Abstand_button.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_step_3.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.Back.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        self.ImageClassification = QPushButton(self)
        self.ImageClassification.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'ImageCl.png')))
        self.ImageClassification.setIconSize(QSize(0.25*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.ImageClassification.setToolTip('...')
        self.ImageClassification.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        
        self.ImageRegression = QPushButton(self)
        self.ImageRegression.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'ImageRE.png')))
        self.ImageRegression.setIconSize(QSize(0.25*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.ImageRegression.setToolTip('...')
        self.ImageRegression.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        
    
        self.TextClassification = QPushButton(self)
        self.TextClassification.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'TextCI.png')))
        self.TextClassification.setIconSize(QSize(0.25*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.TextClassification.setToolTip('...')
        self.TextClassification.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        
        
        self.TextRegression = QPushButton(self)
        self.TextRegression.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'TextRE.png')))
        self.TextRegression.setIconSize(QSize(0.25*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.TextRegression.setToolTip('...')
        self.TextRegression.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        
        self.DataClassification = QPushButton(self)
        self.DataClassification.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'DataCI.png')))
        self.DataClassification.setIconSize(QSize(0.25*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.DataClassification.setToolTip('...')
        self.DataClassification.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        
        self.DataRegression = QPushButton(self)
        self.DataRegression.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'DataRE.png')))
        self.DataRegression.setIconSize(QSize(0.25*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.DataRegression.setToolTip('...')
        self.DataRegression.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addItem(QSpacerItem(0.1*self.WINDOW_WIDTH, 0.1*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.Abstand_button)
        self.horizontal_box[2].addWidget(self.ImageClassification)
        self.horizontal_box[2].addWidget(self.Abstand_button)
        self.horizontal_box[2].addWidget(self.ImageRegression)
        self.horizontal_box[2].addWidget(self.Abstand_button)
        self.horizontal_box[2].addWidget(self.TextClassification)
        self.horizontal_box[2].addWidget(self.Abstand_button)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.label)
        self.horizontal_box[3].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addWidget(self.Abstand_button)
        self.horizontal_box[4].addWidget(self.TextRegression)
        self.horizontal_box[4].addWidget(self.Abstand_button)
        self.horizontal_box[4].addWidget(self.DataClassification)
        self.horizontal_box[4].addWidget(self.Abstand_button)
        self.horizontal_box[4].addWidget(self.DataRegression)
        self.horizontal_box[4].addWidget(self.Abstand_button)
        
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addItem(QSpacerItem(0.15*self.WINDOW_WIDTH, 0.15*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.step, 0, 1, Qt.AlignCenter)
        sublayout.addWidget(self.Abstand_button, 0, 2, Qt.AlignRight)
        self.horizontal_box[6].addLayout(sublayout)
        self.horizontal_box[6].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])

        self.setLayout(self.vertical_box)