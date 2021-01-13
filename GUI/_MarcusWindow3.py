from UIWindows.UIMarcusWindow3 import *
def MarcusWindow3(self):
        
        self.Window1c = UIMarcusWindow3(self.FONT_STYLE, self)
        
        if self.output_path != None:
            self.Window1c.Output_Pfad.setText(self.output_path)
        
        if self.project_name != None:
            self.Window1c.Projekt_Name.setText(self.project_name)
        
        if self.model_path != None:
            self.Window1c.Model_Pfad.setText(self.model_path)
        
        if self.data_loader_path != None:
            self.Window1c.Daten_Pfad.setText(self.data_loader_path)

        print(self.model_path)
        
        self.Window1c.Output_Pfad_Browse.clicked.connect(lambda:self.get_output_path(self.Window1c))
        self.Window1c.Modell_einlesen_Browse.clicked.connect(lambda:self.get_model_path(self.Window1c))
        self.Window1c.Next.clicked.connect(lambda:self.TargetWindow("Next"))
        self.Window1c.Back.clicked.connect(self.MarcusWindow2)
        
        self.setCentralWidget(self.Window1c)
        self.show()