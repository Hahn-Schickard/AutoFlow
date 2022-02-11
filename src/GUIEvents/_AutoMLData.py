''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLData window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  self.GUIStart.load_model.clicked.connect(self.AutoMLData)
"""


from src.GUILayout.UIAutoMLData import *

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
        
        self.AutoMLDataWindow = UIAutoMLData(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)
        
        if self.output_path_ml != None:
            self.AutoMLDataWindow.Output_Pfad.setText(self.output_path_ml)
        
        if self.project_name != None:
            self.AutoMLDataWindow.Projekt_Name.setText(self.project_name)

        if self.data_loader_path_ml != None:
            self.AutoMLDataWindow.Daten_Pfad.setText(self.data_loader_path_ml)
        
        self.AutoMLDataWindow.Output_Pfad_Browse.clicked.connect(lambda:self.get_output_path_ml(self.AutoMLDataWindow))
        self.AutoMLDataWindow.Daten_einlesen_Browse.clicked.connect(lambda:self.get_data_loader_path_ml(self.AutoMLDataWindow))
        self.AutoMLDataWindow.Next.clicked.connect(lambda:nextWindow(self,"Next"))
        self.AutoMLDataWindow.Back.clicked.connect(lambda:nextWindow(self,"Back"))
        
        self.setCentralWidget(self.AutoMLDataWindow)
        self.show()



def nextWindow(self,n):

    if n == "Back":
        self.GUIStart()

    elif n == "Next":
        self.project_name = self.AutoMLDataWindow.Projekt_Name.text()
        self.output_path_ml = self.AutoMLDataWindow.Output_Pfad.text()
        self.data_loader_path_ml = self.AutoMLDataWindow.Daten_Pfad.text()

        if self.project_name == "" or self.output_path_ml == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Please enter your data")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

        print(self.project_name)
        print(self.output_path_ml)
        print(self.data_loader_path_ml)
        self.TaskWindow()