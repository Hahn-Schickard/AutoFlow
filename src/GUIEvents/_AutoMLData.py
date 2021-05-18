from src.GUILayout.AutoMLData import *
def AutoMLData(self):
        
        self.Window1d = UIMarcusWindow4(self.FONT_STYLE, self)
        
        if self.output_path_ml != None:
            self.Window1d.Output_Pfad.setText(self.output_path_ml)
        
        if self.project_name != None:
            self.Window1d.Projekt_Name.setText(self.project_name)

        if self.data_loader_path_ml != None:
            self.Window1d.Daten_Pfad.setText(self.data_loader_path_ml)
        
        self.Window1d.Output_Pfad_Browse.clicked.connect(lambda:self.get_output_path_ml(self.Window1d))
        self.Window1d.Daten_einlesen_Browse.clicked.connect(lambda:self.get_data_loader_path_ml(self.Window1d))
        self.Window1d.Next.clicked.connect(lambda:self.TaskWindow("Next"))
        self.Window1d.Back.clicked.connect(self.GUIStart)
        
        self.setCentralWidget(self.Window1d)
        self.show()