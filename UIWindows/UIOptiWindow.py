import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UIOptiWindow(QWidget):
    def __init__(self, parent=None):
        super(UIOptiWindow, self).__init__(parent)

        self.Font_size = 9
        
        self.label = QLabel("Optimization")
        self.label.setFont(QFont(FONT_TYPE, 12))
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel(self)
        self.Abstand.setFixedWidth(90)
        self.Abstand.setFixedHeight(30)
        
        self.Abstand_label = QLabel(self)
        self.Abstand_label.setFixedWidth(20)
        self.Abstand_label.setFixedHeight(30)
        
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
        
        self.Pruning = QPushButton(self)
        self.Pruning.setIcon(QIcon(os.path.join('Images', 'Pruning_Button.png')))
        self.Pruning.setIconSize(QSize(150, 150))
        self.Pruning.setCheckable(True)
        self.Pruning.setGeometry(120, 85, 170, 170)
        self.Pruning.setToolTip('...')
        self.Pruning.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        
        self.Quantization = QPushButton(self)
        self.Quantization.setIcon(QIcon(os.path.join('Images', 'Quantization_Button.png')))
        self.Quantization.setIconSize(QSize(150, 150))
        self.Quantization.setCheckable(True)
        self.Quantization.setGeometry(515, 85, 170, 170)
        self.Quantization.setToolTip('...')
        self.Quantization.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""") 
        """
        self.Dis = QPushButton(self)
        self.Dis.setIcon(QIcon(os.path.join('Images', 'MCU.png')))
        self.Dis.setIconSize(QSize(150, 150))
        self.Dis.setCheckable(True)
        self.Dis.setGeometry(120, 320, 170, 170)
        self.Dis.setToolTip('...')"""
        #self.Dis.setStyleSheet("""QToolTip { 
        #                   background-color : rgb(53, 53, 53);
        #                  color: white; 
        #                   border: black solid 1px
        #                   }
        #                   QPushButton::hover {
        #                   background-color : rgb(10, 100, 200)}""") 
        """
        self.Huf = QPushButton(self)
        self.Huf.setIcon(QIcon(os.path.join('Images', 'MCU.png')))
        self.Huf.setIconSize(QSize(150, 150))
        self.Huf.setCheckable(True)        
        self.Huf.setGeometry(515, 320, 170, 170)
        self.Huf.setToolTip('...')"""
        #self.Huf.setStyleSheet("""QToolTip { 
        #                   background-color : rgb(53, 53, 53);
        #                   color: white; 
        #                   border: black solid 1px
        #                   }
        #                   QPushButton::hover {
        #                   background-color : rgb(10, 100, 200)}""") 
        
        self.Pruning_Dense_label = QLabel("Pruningfactor\nDense layer", self)
        self.Pruning_Dense_label.setFont(QFont("Pruningfactor\nDense layer", self.Font_size))
        self.Pruning_Dense_label.setFixedWidth(90)
        self.Pruning_Dense_label.setFixedHeight(30)
        self.Pruning_Dense_label.setAlignment(Qt.AlignCenter)
        self.Pruning_Dense_label.setVisible(False)
        
        self.Pruning_Conv_label = QLabel("Pruningfactor\nConv layer", self)
        self.Pruning_Conv_label.setFont(QFont("Pruningfactor\nConv layer", self.Font_size))
        self.Pruning_Conv_label.setFixedWidth(90)
        self.Pruning_Conv_label.setFixedHeight(30)
        self.Pruning_Conv_label.setAlignment(Qt.AlignCenter)
        self.Pruning_Conv_label.setVisible(False)
        
        self.Pruning_Dense = QLineEdit(self)
        self.Pruning_Dense.setFont(QFont("Sans Serif", self.Font_size))
        self.Pruning_Dense.setFixedWidth(90)
        self.Pruning_Dense.setFixedHeight(30)
        self.Pruning_Dense.setVisible(False)

        self.Pruning_Conv = QLineEdit(self)
        self.Pruning_Conv.setFont(QFont("", self.Font_size))
        self.Pruning_Conv.setFixedWidth(90)
        self.Pruning_Conv.setFixedHeight(30)
        self.Pruning_Conv.setVisible(False)

        self.quant_float = QPushButton("float16", self)
        self.quant_float.setFont(QFont("float16", self.Font_size))
        self.quant_float.setFixedWidth(90)
        self.quant_float.setFixedHeight(30)
        self.quant_float.setCheckable(True)
        self.quant_float.setVisible(False)
        
        self.quant_int = QPushButton("int8", self)
        self.quant_int.setFont(QFont("int8", self.Font_size))
        self.quant_int.setFixedWidth(90)
        self.quant_int.setFixedHeight(30)
        self.quant_int.setCheckable(True)
        self.quant_int.setVisible(False)

        self.Dis_1_label = QLabel("Dis_1_label", self)
        self.Dis_1_label.setFont(QFont("Dis_1_label", self.Font_size))
        self.Dis_1_label.setFixedWidth(90)
        self.Dis_1_label.setFixedHeight(30)
        self.Dis_1_label.setAlignment(Qt.AlignCenter)
        self.Dis_1_label.setVisible(False)
        
        self.Dis_2_label = QLabel("Dis_2_label", self)
        self.Dis_2_label.setFont(QFont("Dis_2_label", self.Font_size))
        self.Dis_2_label.setFixedWidth(90)
        self.Dis_2_label.setFixedHeight(30)
        self.Dis_2_label.setAlignment(Qt.AlignCenter)
        self.Dis_2_label.setVisible(False)
        
        self.Dis_1 = QLineEdit(self)
        self.Dis_1.setFixedWidth(90)
        self.Dis_1.setFixedHeight(30)
        self.Dis_1.setVisible(False)

        self.Dis_2 = QLineEdit(self)
        self.Dis_2.setFixedWidth(90)
        self.Dis_2.setFixedHeight(30)
        self.Dis_2.setVisible(False)
        
        self.Huf_1_label = QLabel("Huf_1_label", self)
        self.Huf_1_label.setFont(QFont("Huf_1_label", self.Font_size))
        self.Huf_1_label.setFixedWidth(90)
        self.Huf_1_label.setFixedHeight(30)
        self.Huf_1_label.setAlignment(Qt.AlignCenter)
        self.Huf_1_label.setVisible(False)
        
        self.Huf_2_label = QLabel("Huf_2_label", self)
        self.Huf_2_label.setFont(QFont("Huf_2_label", self.Font_size))
        self.Huf_2_label.setFixedWidth(90)
        self.Huf_2_label.setFixedHeight(30)
        self.Huf_2_label.setAlignment(Qt.AlignCenter)
        self.Huf_2_label.setVisible(False)
        
        self.Huf_1 = QLineEdit(self)
        self.Huf_1.setFixedWidth(90)
        self.Huf_1.setFixedHeight(30)
        self.Huf_1.setVisible(False)

        self.Huf_2 = QLineEdit(self)
        self.Huf_2.setFixedWidth(90)
        self.Huf_2.setFixedHeight(30)
        self.Huf_2.setVisible(False)
        
        
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
        sublayout_oben.addWidget(self.Pruning_Dense_label, 1, 1, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 1, 2, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Pruning_Conv_label, 1, 3, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 4, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 5, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 6, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 1, 7, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 8, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 1, 9, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 2, 0, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Pruning_Dense, 2, 1, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 1, 2, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Pruning_Conv, 2, 3, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 2, 4, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand, 2, 5, Qt.AlignCenter)
        sublayout_oben.addWidget(self.quant_float, 2, 6, Qt.AlignCenter)
        sublayout_oben.addWidget(self.Abstand_label, 2, 7, Qt.AlignCenter)
        sublayout_oben.addWidget(self.quant_int, 2, 8, Qt.AlignCenter)
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
        """        
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
        sublayout_unten.addWidget(self.Dis_1_label, 1, 1, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand_label, 1, 2, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Dis_2_label, 1, 3, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 1, 4, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 1, 5, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Huf_1_label, 1, 6, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand_label, 1, 7, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Huf_2_label, 1, 8, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 1, 9, Qt.AlignCenter)        
        sublayout_unten.addWidget(self.Abstand, 2, 0, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Dis_1, 2, 1, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand_label, 2, 2, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Dis_2, 2, 3, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 2, 4, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 2, 5, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Huf_1, 2, 6, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand_label, 2, 7, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Huf_2, 2, 8, Qt.AlignCenter)
        sublayout_unten.addWidget(self.Abstand, 2, 9, Qt.AlignCenter)
                
        self.horizontal_box[4].addLayout(sublayout_unten)     
        """
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addWidget(self.Back)
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.Schritt)
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.Next)
        self.horizontal_box[4].setAlignment(Qt.AlignBottom)

        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)