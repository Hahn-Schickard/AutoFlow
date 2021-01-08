import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UISettingsWindow(QWidget):
    def __init__(self, FONT_STYLE, parent=None):
        super(UISettingsWindow, self).__init__(parent)
        
        self.FONT_STYLE = FONT_STYLE        
        
        self.label = QLabel("Settings")
        self.label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Epochs = QLabel("Epochs:")
        self.Epochs.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Epochs.setFixedWidth(120)
        self.Epochs.setFixedHeight(30)
        self.Epochs.setAlignment(Qt.AlignLeft)
        
        self.max_trials = QLabel("Max. Trials:")
        self.max_trials.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.max_trials.setFixedWidth(120)
        self.max_trials.setFixedHeight(30)
        self.max_trials.setAlignment(Qt.AlignLeft)
        
        
        self.max_size = QLabel("Max. Model Size:")
        self.max_size.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.max_size.setFixedWidth(120)
        self.max_size.setFixedHeight(30)
        self.max_size.setAlignment(Qt.AlignLeft)
        
        
        self.Abstand = QLabel(self)
        self.Abstand.setFixedWidth(90)
        self.Abstand.setFixedHeight(30)
        
        self.epochs_factor = QLineEdit(self)
        self.epochs_factor.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.epochs_factor.setFixedWidth(90)
        self.epochs_factor.setFixedHeight(30)
        
        self.max_trials_factor = QLineEdit(self)
        self.max_trials_factor.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.max_trials_factor.setFixedWidth(90)
        self.max_trials_factor.setFixedHeight(30)
        
        self.max_size_factor = QLineEdit(self)
        self.max_size_factor.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.max_size_factor.setFixedWidth(90)
        self.max_size_factor.setFixedHeight(30)

        
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar', 'GUI_step_5.png'))
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setFixedHeight(30)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(25, 25))
        self.Back.setFixedHeight(30)    
        
        self.Next = QPushButton(self)
        self.Next.setIcon(QIcon(os.path.join('Images', 'next_arrow.png')))
        self.Next.setIconSize(QSize(25, 25))
        self.Next.setFixedHeight(30)    
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addWidget(self.Epochs)
        self.horizontal_box[1].addWidget(self.epochs_factor)
        #self.horizontal_box[1].addWidget(self.Abstand)
        #self.horizontal_box[1].addWidget(self.Abstand)
        #self.horizontal_box[1].setAlignment(Qt.AlignLeft)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.max_trials)
        self.horizontal_box[2].addWidget(self.max_trials_factor)
        #self.horizontal_box[2].addWidget(self.Abstand)
        #self.horizontal_box[2].addWidget(self.Abstand)
        #self.horizontal_box[2].setAlignment(Qt.AlignLeft)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.max_size)
        self.horizontal_box[3].addWidget(self.max_size_factor)
        #self.horizontal_box[3].addWidget(self.Abstand)
        #self.horizontal_box[3].addWidget(self.Abstand)
        #self.horizontal_box[3].setAlignment(Qt.AlignLeft)
        
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addWidget(self.Abstand)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addWidget(self.Back)
        self.horizontal_box[5].addStretch()
        self.horizontal_box[5].addWidget(self.Schritt)
        self.horizontal_box[5].addStretch()
        self.horizontal_box[5].addWidget(self.Next)
        self.horizontal_box[5].setAlignment(Qt.AlignBottom)

        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)