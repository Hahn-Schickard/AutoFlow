
def start_autokeras(self):
    if "Params" in self.constraints:
        self.params_check = True;

    if "Floats" in self.constraints:
        self.floats_check = True;

    if "Complex" in self.constraints:
        self.complex_check = True;
        
    if self.target == "imageClassification":
        os.system(f"start /B start cmd.exe @cmd /k python autoML/ImageClassifier.py --ProjectName={self.project_name} --OutputPath={self.output_path_ml} --DataPath={self.data_loader_path_ml} --ParamConstraint={self.params_check} --ParamFactor={self.params_factor} --FlopConstraint={self.floats_check} --FlopFactor={self.floats_factor} --ComplexConstraint={self.complex_check} --ComplexFactor={self.complex_factor} --MaxSize={self.max_size} --MaxTrials={self.max_trials} --MaxEpochs={self.max_epoch}")

    if self.target == "imageRegression":
        os.system(f"start /B start cmd.exe @cmd /k python autoML/ImageRegressor.py --ProjectName={self.project_name} --OutputPath={self.output_path_ml} --DataPath={self.data_loader_path_ml} --ParamConstraint={self.params_check} --ParamFactor={self.params_factor} --FlopConstraint={self.floats_check} --FlopFactor={self.floats_factor} --ComplexConstraint={self.complex_check} --ComplexFactor={self.complex_factor} --MaxSize={self.max_size} --MaxTrials={self.max_trials} --MaxEpochs={self.max_epoch}")

def get_output_path_ml(self, CurWindow):
    self.output_path_ml = QFileDialog.getExistingDirectory(self, 'Select the output path', './')
    CurWindow.Output_Pfad.setText(self.output_path_ml)
    print(CurWindow.Output_Pfad.text())

    

    
    
def get_data_loader_path_ml(self, CurWindow):
    self.data_loader_path_ml = QFileDialog.getOpenFileName(self, 'Select your data loader script', './')[0]
    CurWindow.Daten_Pfad.setText(self.data_loader_path_ml)
    print(CurWindow.Daten_Pfad.text())
            
        
        
def Form_clicked(self):
    self.X=0
    self.Y=0
    
    self.Dot.setVisible(True)
    if self.Window3a.Parameter.text() == "":
        Parameter=0
        
    else:
        Parameter = self.Window3a.Parameter.text()
        print(type(Parameter))
        try:
            Parameter=int(Parameter)
        except ValueError:
            self.Window3a.Parameter.setText(Parameter[:-1])
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            
            msg.setText("Please enter a number not a character.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return
    
    if self.Window3a.FPS.text() == "":
        FPS=0
        
    else:
        FPS = self.Window3a.FPS.text()
        try:
            FPS=int(FPS)
        except ValueError:
            self.Window3a.FPS.setText(FPS[:-1])
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            
            msg.setText("Please enter a number not a character.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return
        
    FLOPs=Parameter*FPS
    print(FLOPs)
    
    if FLOPs < 10000000000:
        self.Y+=100
    if FLOPs > 100000000000:
        self.Y-=100
    
    if self.Window3a.Forms.isChecked():  
        self.Y+=100
        
    if self.Window3a.Forml.isChecked():  
        self.Y+=-100
           
    if self.Window3a.Flexs.isChecked():  
        self.X+=200
        
    if self.Window3a.Flexl.isChecked():  
        self.X+=-200
   
    if self.Window3a.Energies.isChecked():  
        self.Y+=50
        self.X+=50

    if self.Window3a.Energiel.isChecked():  
        self.Y+=-50
        self.X+=-50
        
    if self.Window3a.Preiss.isChecked():  
        self.Y+=50
        self.X+=50

    if self.Window3a.Preisl.isChecked():  
        self.Y+=-50
        self.X+=-50
            
    if self.Window3a.Preism.isChecked():  
        if self.X > 0:
            self.X-=25
        if self.X < 0:
            self.X+=25
        if self.Y > 0:
            self.Y-=25
        if self.Y < 0:
            self.Y+=25
            
    if self.Window3a.Energiem.isChecked():  
        if self.X > 0:
            self.X-=25
        if self.X < 0:
            self.X+=25
        if self.Y > 0:
            self.Y-=25
        if self.Y < 0:
            self.Y+=25
            
    if self.Window3a.Formm.isChecked():  
        if self.Y > 0:
            self.Y-=25
        if self.Y < 0:
            self.Y+=25
            
    if self.Window3a.Flexm.isChecked():
        if self.X > 0:
            self.X-=100     
        if self.X < 0:
            self.X+=100
            
    print('vor:')        
    print('y')
    print(self.Y)
    print('x')
    print(self.X)
    
    
    if self.Y > 200:
        self.Y=200
    if self.Y < -200:
        self.Y=-200
        
    if self.X > 200:
        self.X=200
    if self.X < -200:
        self.X=-200
        
            
    if self.X > 0:
        self.X=self.X-((math.sqrt(self.Y*self.Y))*0.5)
    if self.X < 0:
        self.X=self.X+((math.sqrt(self.Y*self.Y))*0.5)
    
    
    
    print('y')
    print(self.Y)
    print('x')
    print(self.X)    
    
    
    self.update_draw(self.X,self.Y)
    
#11Tflops
#1GF
        
        
def update_draw(self,x,y):
    x=390+x
    y=540+y
    
    self.Dot.move(x,y)
                