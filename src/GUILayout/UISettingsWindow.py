''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UISettingsWindow(QWidget):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UISettingsWindow, self).__init__(parent)
        
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE
        
        self.label = QLabel("Settings")
        self.label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Epochs = QLabel("Epochs:")
        self.Epochs.setStyleSheet("font: " + str(int(0.030*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.Epochs.setFixedWidth(0.20*self.WINDOW_WIDTH)
        self.Epochs.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        # self.Epochs.setAlignment(Qt.AlignLeft)
        
        self.max_trials = QLabel("Max. Trials:")
        self.max_trials.setStyleSheet("font: " + str(int(0.030*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.max_trials.setFixedWidth(0.20*self.WINDOW_WIDTH)
        self.max_trials.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        # self.max_trials.setAlignment(Qt.AlignLeft)
        
        self.max_size = QLabel("Max. Model Size:")
        self.max_size.setStyleSheet("font: " + str(int(0.030*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.max_size.setFixedWidth(0.20*self.WINDOW_WIDTH)
        self.max_size.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        # self.max_size.setAlignment(Qt.AlignLeft)
        
        self.epochs_factor = QLineEdit(self)
        self.epochs_factor.setStyleSheet("font: " + str(int(0.030*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.epochs_factor.setFixedWidth(0.10*self.WINDOW_WIDTH)
        self.epochs_factor.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        self.max_trials_factor = QLineEdit(self)
        self.max_trials_factor.setStyleSheet("font: " + str(int(0.030*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.max_trials_factor.setFixedWidth(0.10*self.WINDOW_WIDTH)
        self.max_trials_factor.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        self.max_size_factor = QLineEdit(self)
        self.max_size_factor.setStyleSheet("font: " + str(int(0.030*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.max_size_factor.setFixedWidth(0.10*self.WINDOW_WIDTH)
        self.max_size_factor.setFixedHeight(0.05*self.WINDOW_HEIGHT)

        
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_step_5.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        
        self.back = QPushButton(self)
        self.back.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'back_arrow.png')))
        self.back.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.back.setFixedHeight(0.05*self.WINDOW_HEIGHT) 
        
        self.next = QPushButton(self)
        self.next.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'next_arrow.png')))
        self.next.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.next.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.Epochs)
        self.horizontal_box[1].addWidget(self.epochs_factor)
        self.horizontal_box[1].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addStretch()
        self.horizontal_box[2].addWidget(self.max_trials)
        self.horizontal_box[2].addWidget(self.max_trials_factor)
        self.horizontal_box[2].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addStretch()
        self.horizontal_box[3].addWidget(self.max_size)
        self.horizontal_box[3].addWidget(self.max_size_factor)
        self.horizontal_box[3].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addItem(QSpacerItem(0.09*self.WINDOW_WIDTH, 0.09*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addWidget(self.back)
        self.horizontal_box[5].addStretch()
        self.horizontal_box[5].addWidget(self.step)
        self.horizontal_box[5].addStretch()
        self.horizontal_box[5].addWidget(self.next)
        self.horizontal_box[5].setAlignment(Qt.AlignBottom)

        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)