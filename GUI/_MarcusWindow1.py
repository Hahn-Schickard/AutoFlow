from UIWindows.UIMarcusWindow1 import *
def MarcusWindow1(self):
        
        self.Window1a = UIMarcusWindow1(self.FONT_STYLE, self)
        
        self.Window1a.load_model.clicked.connect(self.MarcusWindow4)
        self.Window1a.train_model.clicked.connect(self.MarcusWindow2)
        
        self.setCentralWidget(self.Window1a)
        self.show()