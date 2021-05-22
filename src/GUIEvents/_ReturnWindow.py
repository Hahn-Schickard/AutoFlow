"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLData window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

from src.GUILayout.UIReturnWindow import *



        
def ReturnWindow(self, n):         
    
    if n == "Next":
        self.start_autokeras()
  
    
    self.Window6 = UIReturnWindow(self.FONT_STYLE, self)
    
    self.Window6.Back.clicked.connect(lambda:self.AutoMLWindow("Back"))
    self.Window6.Load.clicked.connect(lambda:self.MarcusWindow1())         
   
    self.Window6.Finish.clicked.connect(self.close)
    

    self.setCentralWidget(self.Window6)
    self.show()