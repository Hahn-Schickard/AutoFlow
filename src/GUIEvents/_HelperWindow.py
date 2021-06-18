"""This is a splittet method from the Mainwindow class which contain the logic for the HelperWindow window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""


from src.GUILayout.UIHelperWindow import *
        
def HelperWindow(self):
    """Define Logic for the HelperWindow GUI

    Retrieves the parameter class and set the data path, project path and output path

    Args:
      self:
        self represents the instance of the class.
      parameter:
        A parameter class with all the parameter we change and need to start the project
      

    Returns:


    Raises:
      IOError: An error occurred accessing the parameterset.
    """        
    self.setFixedWidth(800)
    self.setFixedHeight(900)
    self.HelperWindow = UIHelperWindow(self.FONT_STYLE, self)
    
    
    
    self.HelperWindow.Forms.clicked.connect(self.Form_clicked)
    self.HelperWindow.Formm.clicked.connect(self.Form_clicked)
    self.HelperWindow.Forml.clicked.connect(self.Form_clicked)
    self.HelperWindow.Energies.clicked.connect(self.Form_clicked)
    self.HelperWindow.Energiem.clicked.connect(self.Form_clicked)
    self.HelperWindow.Energiel.clicked.connect(self.Form_clicked)
    self.HelperWindow.Flexs.clicked.connect(self.Form_clicked)
    self.HelperWindow.Flexm.clicked.connect(self.Form_clicked)
    self.HelperWindow.Flexl.clicked.connect(self.Form_clicked)
    self.HelperWindow.Preiss.clicked.connect(self.Form_clicked)
    self.HelperWindow.Preism.clicked.connect(self.Form_clicked)
    self.HelperWindow.Preisl.clicked.connect(self.Form_clicked)
    self.HelperWindow.Parameter.textChanged.connect(self.Form_clicked)
    self.HelperWindow.FPS.textChanged.connect(self.Form_clicked)
    
    
    self.HelperWindow.Back.clicked.connect(lambda:self.TargetWindow("Back", self.HelperWindow))
    self.HelperWindow.Next.clicked.connect(lambda:self.OptiWindow("Next","?"))
    
    self.setCentralWidget(self.HelperWindow)
    
    self.Dot = QLabel(self)
    Dotimg = QPixmap(os.path.join('src','GUILayout','Images', 'Dot.png'))
    self.Dot.setFixedSize(30, 30)
    self.Dot.setScaledContents(True)
    self.Dot.setPixmap(Dotimg)
    self.Dot.setVisible(False)
    
    
    self.show()