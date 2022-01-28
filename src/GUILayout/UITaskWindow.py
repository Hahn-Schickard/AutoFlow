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
        self.label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel()
        self.Abstand.setFixedHeight(30)
        
        self.Abstand_v = QLabel()
        self.Abstand_v.setFixedHeight(120)
        
        self.Abstand_button = QLabel()
        self.Abstand_button.setFixedWidth(10)
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_step_3.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(25, 25))
        self.Back.setFixedHeight(30)        
        
        self.ImageClassification = QPushButton(self)
        self.ImageClassification.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'ImageCl.png')))
        self.ImageClassification.setIconSize(QSize(200, 250))
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
        self.ImageRegression.setIconSize(QSize(200, 250))
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
        self.TextClassification.setIconSize(QSize(200, 250))
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
        self.TextRegression.setIconSize(QSize(200, 250))
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
        self.DataClassification.setIconSize(QSize(200, 250))
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
        self.DataRegression.setIconSize(QSize(200, 250))
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
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addWidget(self.Abstand)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.Abstand_button)
        self.horizontal_box[2].addWidget(self.ImageClassification)
        self.horizontal_box[2].addWidget(self.Abstand_button)
        self.horizontal_box[2].addWidget(self.ImageRegression)
        self.horizontal_box[2].addWidget(self.Abstand_button)
        self.horizontal_box[2].addWidget(self.TextClassification)
        self.horizontal_box[2].addWidget(self.Abstand_button)
        
        #self.horizontal_box = []
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
        self.horizontal_box[5].addWidget(self.Abstand_v)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.step, 0, 1)
        sublayout.addWidget(self.Abstand, 0, 2)
        self.horizontal_box[6].addLayout(sublayout)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])

        self.setLayout(self.vertical_box)