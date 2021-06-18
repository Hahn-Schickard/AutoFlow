"""This is a splittet method from the Mainwindow class which contain the logic for the StartWindow window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""


from src.GUILayout.UIStartWindow import *

def StartWindow(self):
    """Define Logic for the StartWindow GUI

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
    self.Window1 = UIStartWindow(self.FONT_STYLE, self)
    
    if self.output_path != None:
        self.Window1.Output_Pfad.setText(self.output_path)
    
    if self.project_name != None:
        self.Window1.Projekt_Name.setText(self.project_name)
    
    if self.model_path != None:
        self.Window1.Model_Pfad.setText(self.model_path)
    
    if self.data_loader_path != None:
        self.Window1.Daten_Pfad.setText(self.data_loader_path)

    
    self.Window1.Output_Pfad_Browse.clicked.connect(lambda:self.get_output_path(self.Window1))
    self.Window1.Modell_einlesen_Browse.clicked.connect(lambda:self.get_model_path(self.Window1))
    self.Window1.Daten_einlesen_Browse.clicked.connect(lambda:self.get_data_loader_path(self.Window1))
    
    self.Window1.Next.clicked.connect(lambda:self.TargetWindow("Next", self.Window1))
    self.Window1.Back.clicked.connect(self.GUIStart)
    
    self.setCentralWidget(self.Window1)
    self.show()