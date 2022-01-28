import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UIConstraintsWindow(QWidget):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UIConstraintsWindow, self).__init__(parent)
        
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE
        
        self.label = QLabel("Constraints")
        self.label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel(self)
        self.Abstand.setFixedWidth(90)
        self.Abstand.setFixedHeight(30)
        
        self.Abstand_label = QLabel(self)
        self.Abstand_label.setFixedWidth(20)
        self.Abstand_label.setFixedHeight(30)
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_step_4.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(25, 25))
        self.Back.setFixedHeight(30)    
        
        self.Next = QPushButton(self)
        self.Next.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'next_arrow.png')))
        self.Next.setIconSize(QSize(25, 25))
        self.Next.setFixedHeight(30)    
        
        self.Params = QPushButton(self)
        self.Params.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'params.png')))
        self.Params.setIconSize(QSize(150, 150))
        self.Params.setCheckable(True)
        self.Params.setGeometry(120, 85, 170, 170)
        self.Params.setToolTip('...')
        self.Params.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        
        self.Floats = QPushButton(self)
        self.Floats.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'flops.png')))
        self.Floats.setIconSize(QSize(150, 150))
        self.Floats.setCheckable(True)
        self.Floats.setGeometry(515, 85, 170, 170)
        self.Floats.setToolTip('...')
        self.Floats.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        
        self.Complex = QPushButton(self)
        self.Complex.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'complex.png')))
        self.Complex.setIconSize(QSize(150, 150))
        self.Complex.setCheckable(True)
        self.Complex.setGeometry(120, 320, 170, 170)
        self.Complex.setToolTip('...')
        self.Complex.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        
        self.Params_label = QLabel("Faktor", self)
        self.Params_label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Params_label.setFixedWidth(90)
        self.Params_label.setFixedHeight(30)
        self.Params_label.setAlignment(Qt.AlignCenter)
        self.Params_label.setVisible(False)
        
        
        self.Params_factor = QLineEdit(self)
        self.Params_factor.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Params_factor.setFixedWidth(90)
        self.Params_factor.setFixedHeight(30)
        self.Params_factor.setVisible(False)


        self.Floats_label = QLabel("Faktor", self)
        self.Floats_label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Floats_label.setFixedWidth(90)
        self.Floats_label.setFixedHeight(30)
        self.Floats_label.setAlignment(Qt.AlignCenter)
        self.Floats_label.setVisible(False)
        
        self.Floats_factor = QLineEdit(self)
        self.Floats_factor.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Floats_factor.setFixedWidth(90)
        self.Floats_factor.setFixedHeight(30)
        self.Floats_factor.setVisible(False)

        self.Complex_label = QLabel("Faktor", self)
        self.Complex_label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Complex_label.setFixedWidth(90)
        self.Complex_label.setFixedHeight(30)
        self.Complex_label.setAlignment(Qt.AlignCenter)
        self.Complex_label.setVisible(False)
        
        self.Complex_factor = QLineEdit(self)
        self.Complex_factor.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Complex_factor.setFixedWidth(90)
        self.Complex_factor.setFixedHeight(30)
        self.Complex_factor.setVisible(False)
     

        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addWidget(self.Abstand)
        self.horizontal_box[1].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout_oben = QGridLayout()
        sublayout_oben.addWidget(self.Abstand, 0, 0, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 0, 1, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 0, 2, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 0, 3, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 0, 4, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 0, 5, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 0, 6, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 0, 7, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 0, 8, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 0, 9, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 0, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 1, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 1, 2, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 3, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 4, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 5, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 6, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 1, 7, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 8, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 9, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 2, 0, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Params_label, 2, 1, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 1, 2, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Params_factor, 2, 3, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 2, 4, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 2, 5, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Floats_label, 2, 6, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 2, 7, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Floats_factor, 2, 8, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 2, 9, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 3, 0, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 3, 1, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 3, 2, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 3, 3, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 3, 4, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 3, 5, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 3, 6, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 3, 7, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 3, 8, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 3, 9, Qt.AlignCenter)        
        self.horizontal_box[2].addLayout(sublayout_oben)
                
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.Abstand)
        self.horizontal_box[3].setAlignment(Qt.AlignTop)
                
        self.horizontal_box.append(QHBoxLayout())
        sublayout_unten = QGridLayout()        
        sublayout_unten.addWidget(self.Abstand, 0, 0, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 0, 1, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand_label, 0, 2, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 0, 3, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 0, 4, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 0, 5, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 0, 6, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand_label, 0, 7, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 0, 8, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 0, 9, Qt.AlignCenter)        
        sublayout_unten.addWidget(self.Abstand, 1, 0, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 1, 1, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand_label, 1, 2, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 1, 3, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 1, 4, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 1, 5, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 1, 6, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand_label, 1, 7, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 1, 8, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 1, 9, Qt.AlignCenter)        
        sublayout_unten.addWidget(self.Abstand, 2, 0, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Complex_label, 2, 1, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand_label, 2, 2, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Complex_factor, 2, 3, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 2, 4, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 2, 5, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 2, 6, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand_label, 2, 7, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 2, 8, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 2, 9, Qt.AlignCenter)
                
        self.horizontal_box[4].addLayout(sublayout_unten)     
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addWidget(self.Back)
        self.horizontal_box[5].addStretch()
        self.horizontal_box[5].addWidget(self.step)
        self.horizontal_box[5].addStretch()
        self.horizontal_box[5].addWidget(self.Next)
        self.horizontal_box[5].setAlignment(Qt.AlignBottom)

        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)