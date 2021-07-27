"""This is a splittet method from the Mainwindow class which contain the logic for the GUIStart window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

from src.GUILayout.Start import *
def GUIStart(self):
        """Define Logic for the GUIStart GUI

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
        
        self.GUIStart1 = UIMarcusWindow1(self.FONT_STYLE, self)
        
        self.GUIStart1.load_model.clicked.connect(self.AutoMLData)
        self.GUIStart1.train_model.clicked.connect(self.StartWindow)
        
        self.setCentralWidget(self.GUIStart1)
        self.show()