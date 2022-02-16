''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.Threads.Autokeras_thread import *


class UIAutoMLWindow(QWidget):
    """GUI window of AutoKeras training process.

	A info text is displayed which tells you to wait in this
    window until the training process is completed. After it is
    finished, you get back to the start window.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, project_name, output_path, data_path, max_trials, max_epochs, max_size, num_channels, img_height, img_width, parent=None):
        super(UIAutoMLWindow, self).__init__(parent)
                
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE

        self.project_name = project_name
        self.output_path = output_path
        self.data_path = data_path
        self.max_trials = max_trials
        self.max_epochs = max_epochs
        self.max_size = max_size
        self.num_channels = num_channels
        self.img_height = img_height
        self.img_width = img_width
        
        self.label = QLabel("End")
        self.label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.info = QLabel("Check if AutoKeras trains some models.\n"
                            "Wait here until the training is finished.\n"
                            "After the training of the models is finished,\n"
                            "you can return to the start window\n"
                            "by pressing the right arrow button.")
        self.info.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.info.setAlignment(Qt.AlignCenter)
        
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_step_6.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        
        self.finish = QPushButton("Finish", self)
        self.finish.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.finish.setFixedWidth(125)
        self.finish.setToolTip('...')
        self.finish.setVisible(False)
        
        self.back = QPushButton(self)
        self.back.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'back_arrow.png')))
        self.back.setIconSize(QSize(25, 25))
        self.back.setFixedHeight(30)

        self.load = QPushButton(self)
        self.load.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'Next_arrow.png')))
        self.load.setIconSize(QSize(25, 25))
        self.load.setFixedHeight(30)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.info)
        self.horizontal_box[1].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addStretch()
        self.horizontal_box[2].addWidget(self.finish)
        self.horizontal_box[2].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.back)
        self.horizontal_box[3].addStretch()
        self.horizontal_box[3].addWidget(self.step) 
        self.horizontal_box[3].addStretch()         
        self.horizontal_box[3].addWidget(self.load)
        self.horizontal_box[3].setAlignment(Qt.AlignBottom)
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)
        
        
        self.autokeras = Autokeras(self.project_name, self.output_path, self.data_path, self.max_trials, self.max_epochs, self.max_size, self.num_channels, self.img_height, self.img_width)