"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLWindow window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
from src.GUILayout.UIAutoMLWindow import *

   
def AutoMLWindow(self, n):         
    """Define Logic for the AutoMLWindow GUI

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
    if n == "Next":
        self.max_epoch = self.Window4.epochs_factor.text()
        self.max_trials = self.Window4.max_trials_factor.text()
        self.max_size = self.Window4.max_size_factor.text()

    
    self.Window5 = UIAutoMLWindow(self.FONT_STYLE, self)
      
    self.Window5.Back.clicked.connect(lambda:self.SettingsWindow("Back"))
    self.Window5.Start.clicked.connect(lambda:self.ReturnWindow("Next"))
   
    self.Window5.Finish.clicked.connect(self.close)

    
    self.setCentralWidget(self.Window5)
    self.show()