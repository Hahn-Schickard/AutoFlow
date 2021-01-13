from UIWindows.UIMarcusWindow2 import *
def MarcusWindow2(self):
        
        self.Window1b = UIMarcusWindow2(self.FONT_STYLE, self)
        
        self.Window1b.uC.clicked.connect(self.StartWindow)
        self.Window1b.FPGA.clicked.connect(self.MarcusWindow3)
        self.Window1b.Back.clicked.connect(self.MarcusWindow1)
        
        self.setCentralWidget(self.Window1b)
        self.show()