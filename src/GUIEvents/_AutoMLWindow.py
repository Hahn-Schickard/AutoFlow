''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from src.GUILayout.UIAutoMLWindow import *

        
def AutoMLWindow(self):  
    """AutoKeras training process get started.

	The process of training models accoring the passed settings
	get started. You have to wait until the process is finished.
	After this you get back to the start window.
    """
    self.Window6 = UIAutoMLWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self.project_name, self.output_path, self.data_loader_path, self.max_trials, self.max_epochs, self.max_size, self.num_channels, self.img_height, self.img_width, self)

    # self.start_autokeras()
    self.Window6.autokeras.start()

    self.Window6.autokeras.request_signal.connect(lambda:nextWindow(self,"Next"))
    
    self.Window6.back.clicked.connect(lambda:nextWindow(self,"Back"))
    self.Window6.load.clicked.connect(lambda:nextWindow(self,"Next"))    

    self.setCentralWidget(self.Window6)
    self.show()


def nextWindow(self,n):
    """
    Defines which one is the next window to open.

    Args:
        n:  Go forward or go back
    """
    if n == "Back":
        self.SettingsWindow()

    elif n == "Next":
        self.GUIStart()