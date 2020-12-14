import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UIHelperWindow(QWidget):
    def __init__(self, parent=None):
        super(UIHelperWindow, self).__init__(parent)
        
        
        self.Parameter = QLineEdit()
        self.Parameter.setFixedWidth(200)
        
        self.ParameterL = QLabel("Parameter")
        self.ParameterL.setFont(QFont("Parameter", 12))
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar', 'GUI_step_4.png'))
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setFixedHeight(30)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.FPS = QLineEdit()
        self.FPS.setFixedWidth(200)
        
        self.FPSL = QLabel("FPS")
        self.FPSL.setFont(QFont("FPS", 12))
                
        self.Bauform = QLabel("Bauform")
        self.Bauform.setFont(QFont("Bauform", 12))
        
        self.Forms = QPushButton(" small ", self)
        self.Forms.setFont(QFont(" small ", 12))
        self.Forms.setCheckable(True) 
        self.Formm = QPushButton(" medium ", self)
        self.Formm.setFont(QFont(" medium ", 12))
        self.Formm.setCheckable(True)
        self.Forml = QPushButton(" large ", self)
        self.Forml.setFont(QFont(" large ", 12))
        self.Forml.setCheckable(True)

        self.Flexibilitat = QLabel("Flexibilität")
        self.Flexibilitat.setFont(QFont("Flexibilität", 12))
        self.Flexibilitat.setAlignment(Qt.AlignCenter)
        
        self.Flexs = QPushButton(" small ", self)
        self.Flexs.setFont(QFont(" small ", 12))
        self.Flexs.setCheckable(True) 
        self.Flexm = QPushButton(" medium ", self)
        self.Flexm.setFont(QFont(" medium ", 12))
        self.Flexm.setCheckable(True) 
        self.Flexl = QPushButton(" large ", self)
        self.Flexl.setFont(QFont(" large ", 12))
        self.Flexl.setCheckable(True) 
        
        self.Energieverbrauch = QLabel("Energieverbrauch")
        self.Energieverbrauch.setFont(QFont("Energieverbrauch", 12))
        
        self.Energies = QPushButton(" small ", self)
        self.Energies.setFont(QFont(" small ", 12))
        self.Energies.setCheckable(True)
        self.Energiem = QPushButton(" medium ", self)
        self.Energiem.setFont(QFont(" medium ", 12))
        self.Energiem.setCheckable(True)
        self.Energiel = QPushButton(" large ", self)
        self.Energiel.setFont(QFont(" large ", 12))
        self.Energiel.setCheckable(True)
        
        self.Preis = QLabel("Preis")
        self.Preis.setFont(QFont("Preis", 12))
        
        self.Preiss = QPushButton(" small ", self)
        self.Preiss.setFont(QFont(" small ", 12))
        self.Preiss.setCheckable(True)
        self.Preism = QPushButton(" medium ", self)
        self.Preism.setFont(QFont(" medium ", 12))
        self.Preism.setCheckable(True)
        self.Preisl = QPushButton(" large ", self)
        self.Preisl.setFont(QFont(" large ", 12))
        self.Preisl.setCheckable(True)
        
        self.Loadpng = QLabel(self)
        img = QPixmap(os.path.join('Images', 'Helper.png'))
        self.Loadpng.setPixmap(img)
        
        self.Abstand = QLabel()
        self.Abstand.setFixedHeight(30)
        
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
        self.horizontal_box[10].addWidget(self.Back)
        self.horizontal_box[10].addStretch() 
        self.horizontal_box[10].addWidget(self.Schritt)
        self.horizontal_box[10].addStretch()
        self.horizontal_box[10].addWidget(self.Next)
        self.horizontal_box[10].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)