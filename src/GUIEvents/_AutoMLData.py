"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLData window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  self.GUIStart.load_model.clicked.connect(self.AutoMLData)
"""

from src.GUILayout.AutoMLData import *
def AutoMLData(self):
        """Define Logic for the AutoMLData GUI

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
        
        self.AutoMLDataWindow = UIAutoMLData(self.FONT_STYLE, self)
        
        if self.output_path_ml != None:
            self.AutoMLDataWindow.Output_Pfad.setText(self.output_path_ml)
        
        if self.project_name != None:
            self.AutoMLDataWindow.Projekt_Name.setText(self.project_name)

        if self.data_loader_path_ml != None:
            self.AutoMLDataWindow.Daten_Pfad.setText(self.data_loader_path_ml)
        
        self.AutoMLDataWindow.Output_Pfad_Browse.clicked.connect(lambda:self.get_output_path_ml(self.AutoMLDataWindow))
        self.AutoMLDataWindow.Daten_einlesen_Browse.clicked.connect(lambda:self.get_data_loader_path_ml(self.AutoMLDataWindow))
        self.AutoMLDataWindow.Next.clicked.connect(lambda:self.TaskWindow("Next"))
        self.AutoMLDataWindow.Back.clicked.connect(self.GUIStart)
        
        self.setCentralWidget(self.AutoMLDataWindow)
        self.show()