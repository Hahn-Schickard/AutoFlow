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
        
        if self.output_path != None:
            self.AutoMLDataWindow.output_path_label.setText(self.output_path_label)
        
        if self.project_name != None:
            self.AutoMLDataWindow.project_name.setText(self.project_name)

        if self.data_loader_path != None:
            self.AutoMLDataWindow.data_path.setText(self.data_loader_path)
        
        self.AutoMLDataWindow.output_path_browse.clicked.connect(lambda:self.get_output_path(self.AutoMLDataWindow))
        self.AutoMLDataWindow.select_data_browse.clicked.connect(lambda: self.get_data_loader(self.AutoMLDataWindow))
        self.AutoMLDataWindow.next.clicked.connect(lambda:nextWindow(self,"Next"))
        self.AutoMLDataWindow.back.clicked.connect(lambda:nextWindow(self,"Back"))
        
        self.setCentralWidget(self.AutoMLDataWindow)
        self.show()



def nextWindow(self,n):

    if n == "Back":
        self.GUIStart()

    elif n == "Next":
        self.project_name = self.AutoMLDataWindow.project_name.text()
        self.output_path_label = self.AutoMLDataWindow.output_path_label.text()
        self.data_loader_path = self.AutoMLDataWindow.data_path.text()

        if self.project_name == "" or self.output_path_label == "" or self.data_loader_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Please enter your data")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

        print(self.project_name)
        print(self.output_path_label)
        print(self.data_loader_path)
        self.TaskWindow()