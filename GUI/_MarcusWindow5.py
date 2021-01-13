from UIWindows.UIMarcusWindow5 import *
def MarcusWindow5(self):
        
        self.Window1e = UIMarcusWindow5(self.FONT_STYLE, self)
        
        self.Window1e.Back.clicked.connect(self.MarcusWindow4)
        
        #self.Window1e.Load.clicked.connect(self.model_pruning)
        #self.Window1e.Load.clicked.connect(self.download)
        
        self.setCentralWidget(self.Window1e)
        self.show()