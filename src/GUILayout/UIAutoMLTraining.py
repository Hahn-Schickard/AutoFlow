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

from src.Threads.Loading_images_thread import * 
from src.Threads.Autokeras_thread import *


class UIAutoMLTraining(QWidget):
    """GUI window of AutoKeras training process.

	A info text is displayed which tells you to wait in this
    window until the training process is completed. During the 
    training, a loading animation runs. After it is finished,
    you get back to the start window.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, project_name, output_path, data_path, task, max_trials,
            max_epochs, max_size, num_channels, img_height, img_width, separator, decimal, csv_target_label, parent=None):
        super(UIAutoMLTraining, self).__init__(parent)
                
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE

        self.project_name = project_name
        self.output_path = output_path
        self.data_path = data_path
        self.task = task
        self.max_trials = max_trials
        self.max_epochs = max_epochs
        self.max_size = max_size
        self.num_channels = num_channels
        self.img_height = img_height
        self.img_width = img_width
        self.separator = separator
        self.decimal = decimal
        self.csv_target_label = csv_target_label
        
        self.label = QLabel("AutoML training")
        self.label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.load_png = QLabel(self)
        self.load_png.setFixedWidth(0.3*self.WINDOW_HEIGHT)
        self.load_png.setFixedHeight(0.3*self.WINDOW_HEIGHT)
        img = QPixmap(os.path.join('src','GUILayout','Images','GUI_loading_images', 'GUI_load_0.png'))
        self.load_png.setPixmap(img)
        self.load_png.setScaledContents(True)
        
        self.info = QLabel("Check if AutoKeras trains some models.\n"
                            "You stay in this window until the training is\n"
                            "finished. After the training is finished, you\n"
                            "automatically return to the start window.")
        self.info.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.info.setAlignment(Qt.AlignCenter)
        
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_train_step_5.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.load_png)
        self.horizontal_box[1].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addItem(QSpacerItem(self.WINDOW_WIDTH, 0.1*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addStretch()
        self.horizontal_box[3].addWidget(self.info)
        self.horizontal_box[3].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.step) 
        self.horizontal_box[4].addStretch()         
        self.horizontal_box[4].setAlignment(Qt.AlignBottom)
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)
        
        
        self.loading_images = Loading_images(self.load_png)
        
        self.autokeras = Autokeras(self.project_name, self.output_path, self.data_path, self.task, self.max_trials,
                                self.max_epochs, self.max_size, self.num_channels, self.img_height, self.img_width,
                                self.separator, self.decimal, self.csv_target_label)