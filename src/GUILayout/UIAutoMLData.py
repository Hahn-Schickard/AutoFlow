import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UIAutoMLData(QWidget):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UIAutoMLData, self).__init__(parent)
        
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE
        
        self.Projekt_Name_label = QLabel("AutoML Projectname:")
        self.Projekt_Name_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        
        self.Daten_label = QLabel("Datascript:")
        self.Daten_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        
        self.Datapng = QLabel(self)
        self.Datapng.setFixedWidth(0.25*self.WINDOW_HEIGHT)
        self.Datapng.setFixedHeight(0.25*self.WINDOW_HEIGHT)
        Dataimg = QPixmap(os.path.join('src','GUILayout','Images','network.png'))
        self.Datapng.setPixmap(Dataimg)
        self.Datapng.setScaledContents(True)
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_step_2.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        
        self.Projekt_Name = QLineEdit()
        self.Projekt_Name.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.Projekt_Name.setFixedWidth(0.25*self.WINDOW_WIDTH)
        
        self.Model_Pfad = QLabel("")
        self.Model_Pfad.setFixedWidth(0.7*self.WINDOW_WIDTH)
        self.Model_Pfad.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.Model_Pfad.setAlignment(Qt.AlignCenter)
        
        self.Output_Pfad = QLabel("")
        self.Output_Pfad.setFixedWidth(0.7*self.WINDOW_WIDTH)
        self.Output_Pfad.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.Output_Pfad.setAlignment(Qt.AlignCenter)
        
        self.Daten_Pfad = QLabel("")
        self.Daten_Pfad.setFixedWidth(0.7*self.WINDOW_WIDTH)
        self.Daten_Pfad.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.Daten_Pfad.setAlignment(Qt.AlignCenter)
        
        self.Output_Pfad_Browse = QPushButton(" Output path... ", self)
        self.Output_Pfad_Browse.setToolTip('...')
        self.Output_Pfad_Browse.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.035*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""")
        
        self.Daten_einlesen_Browse = QPushButton(" Select Data... ", self)
        self.Daten_einlesen_Browse.setToolTip('...')
        self.Daten_einlesen_Browse.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.035*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 

        self.Next = QPushButton(self)
        self.Next.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'next_arrow.png')))
        self.Next.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.Next.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.Back.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].addWidget(self.Projekt_Name_label)
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addWidget(self.Projekt_Name)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addItem(QSpacerItem(0.03*self.WINDOW_WIDTH, 0.03*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.Output_Pfad)
        self.horizontal_box[3].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addWidget(self.Output_Pfad_Browse)
        self.horizontal_box[4].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addItem(QSpacerItem(0.03*self.WINDOW_WIDTH, 0.03*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addWidget(self.Daten_label)
        self.horizontal_box[6].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addWidget(self.Datapng)
        self.horizontal_box[7].addStretch()     
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[8].addStretch()
        self.horizontal_box[8].addWidget(self.Daten_Pfad)
        self.horizontal_box[8].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[9].addStretch()
        self.horizontal_box[9].addWidget(self.Daten_einlesen_Browse)
        self.horizontal_box[9].addStretch()
    
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[10].addItem(QSpacerItem(0.03*self.WINDOW_WIDTH, 0.03*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.step, 0, 1)
        sublayout.addWidget(self.Next, 0, 2, Qt.AlignRight)
        self.horizontal_box[11].addLayout(sublayout)
        self.horizontal_box[11].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)