import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UIHelperWindow(QWidget):
    def __init__(self, FONT_STYLE, parent=None):
        super(UIHelperWindow, self).__init__(parent)
        
        
        self.FONT_STYLE = FONT_STYLE        
        
        self.Parameter = QLineEdit()
        self.Parameter.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Parameter.setFixedWidth(200)
        
        self.ParameterL = QLabel("Parameter")
        self.ParameterL.setStyleSheet("font: 12pt " + FONT_STYLE)

        self.FPS = QLineEdit()
        self.FPS.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.FPS.setFixedWidth(200)
        
        self.FPSL = QLabel("FPS")
        self.FPSL.setStyleSheet("font: 12pt " + FONT_STYLE)
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_step_4.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        
        self.Bauform = QLabel("Bauform")
        self.Bauform.setStyleSheet("font: 12pt " + FONT_STYLE)
        
        self.Forms = QPushButton(" small ", self)
        self.Forms.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Forms.setCheckable(True) 
        self.Formm = QPushButton(" medium ", self)
        self.Formm.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Formm.setCheckable(True)
        self.Forml = QPushButton(" large ", self)
        self.Forml.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Forml.setCheckable(True)

        self.Flexibilitat = QLabel("Flexibilität")
        self.Flexibilitat.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Flexibilitat.setAlignment(Qt.AlignCenter)
        
        self.Flexs = QPushButton(" small ", self)
        self.Flexs.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Flexs.setCheckable(True) 
        self.Flexm = QPushButton(" medium ", self)
        self.Flexm.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Flexm.setCheckable(True) 
        self.Flexl = QPushButton(" large ", self)
        self.Flexl.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Flexl.setCheckable(True) 
        
        self.Energieverbrauch = QLabel("Energieverbrauch")
        self.Energieverbrauch.setStyleSheet("font: 12pt " + FONT_STYLE)
        
        self.Energies = QPushButton(" small ", self)
        self.Energies.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Energies.setCheckable(True)
        self.Energiem = QPushButton(" medium ", self)
        self.Energiem.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Energiem.setCheckable(True)
        self.Energiel = QPushButton(" large ", self)
        self.Energiel.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Energiel.setCheckable(True)
        
        self.Preis = QLabel("Preis")
        self.Preis.setStyleSheet("font: 12pt " + FONT_STYLE)
        
        self.Preiss = QPushButton(" small ", self)
        self.Preiss.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Preiss.setCheckable(True)
        self.Preism = QPushButton(" medium ", self)
        self.Preism.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Preism.setCheckable(True)
        self.Preisl = QPushButton(" large ", self)
        self.Preisl.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Preisl.setCheckable(True)
        
        self.Loadpng = QLabel(self)
        img = QPixmap(os.path.join('src','GUILayout','Images', 'Helper.png'))
        self.Loadpng.setPixmap(img)
        
        self.Abstand = QLabel()
        self.Abstand.setFixedHeight(30)
        
        self.back = QPushButton(self)
        self.back.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'back_arrow.png')))
        self.back.setIconSize(QSize(25, 25))
        self.back.setFixedHeight(30)
        
        self.next = QPushButton(self)
        self.next.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'next_arrow.png')))
        self.next.setIconSize(QSize(25, 25))
        self.next.setFixedHeight(30)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].addWidget(self.ParameterL)
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].addWidget(self.FPSL)
        self.horizontal_box[0].addStretch()

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.Parameter)
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.FPS)
        self.horizontal_box[1].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.Abstand)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addStretch()
        self.horizontal_box[3].addWidget(self.Bauform)
        self.horizontal_box[3].addStretch()
        self.horizontal_box[3].addStretch()
        self.horizontal_box[3].addWidget(self.Preis)
        self.horizontal_box[3].addStretch()

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.Forms)
        self.horizontal_box[4].addWidget(self.Formm)
        self.horizontal_box[4].addWidget(self.Forml)
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.Preiss)
        self.horizontal_box[4].addWidget(self.Preism)
        self.horizontal_box[4].addWidget(self.Preisl)
        self.horizontal_box[4].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addWidget(self.Abstand)
    
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addWidget(self.Flexibilitat)
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addWidget(self.Energieverbrauch)
        self.horizontal_box[6].addStretch()

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addWidget(self.Flexs)
        self.horizontal_box[7].addWidget(self.Flexm)
        self.horizontal_box[7].addWidget(self.Flexl)
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addWidget(self.Energies)
        self.horizontal_box[7].addWidget(self.Energiem)
        self.horizontal_box[7].addWidget(self.Energiel)
        self.horizontal_box[7].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[8].addStretch()
        self.horizontal_box[8].addWidget(self.Loadpng)
        self.horizontal_box[8].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[9].addWidget(self.Abstand)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[10].addWidget(self.back)
        self.horizontal_box[10].addStretch() 
        self.horizontal_box[10].addWidget(self.step)
        self.horizontal_box[10].addStretch()
        self.horizontal_box[10].addWidget(self.next)
        self.horizontal_box[10].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)