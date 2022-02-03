''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UITargetWindow(QWidget):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UITargetWindow, self).__init__(parent)
        
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE    
        
        self.label = QLabel("Choose your target")
        self.label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)

        self.uC = QPushButton(self)
        self.uC.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'MCU.png')))
        self.uC.setIconSize(QSize(0.2*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.uC.setToolTip('...')
        self.uC.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""")
        self.uC.setFixedHeight(0.35*self.WINDOW_HEIGHT)
        self.uC.setFixedWidth(0.35*self.WINDOW_WIDTH)
        
        self.FPGA = QPushButton(self)
        self.FPGA.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'FPGA.png')))
        self.FPGA.setIconSize(QSize(0.2*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.FPGA.setToolTip('...')
        self.FPGA.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""")
        self.FPGA.setFixedHeight(0.35*self.WINDOW_HEIGHT)
        self.FPGA.setFixedWidth(0.35*self.WINDOW_WIDTH)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.Back.setFixedHeight(0.05*self.WINDOW_HEIGHT)

        self.step = QLabel(self)
        self.step.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_step_4.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        
        self.placeholder_button = QLabel()
        self.placeholder_button.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addItem(QSpacerItem(self.WINDOW_WIDTH, 0.1*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addItem(QSpacerItem(0.02*self.WINDOW_WIDTH, 0.02*self.WINDOW_HEIGHT))
        self.horizontal_box[2].addWidget(self.uC)
        self.horizontal_box[2].addItem(QSpacerItem(0.02*self.WINDOW_WIDTH, 0.02*self.WINDOW_HEIGHT))
        self.horizontal_box[2].addWidget(self.FPGA)
        self.horizontal_box[2].addItem(QSpacerItem(0.02*self.WINDOW_WIDTH, 0.02*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addItem(QSpacerItem(self.WINDOW_WIDTH, 0.25*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.step, 0, 1, Qt.AlignCenter)
        sublayout.addWidget(self.placeholder_button, 0, 2, Qt.AlignRight)
        self.horizontal_box[4].addLayout(sublayout)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])

        self.setLayout(self.vertical_box)