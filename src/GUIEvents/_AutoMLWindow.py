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
    self.Window6 = UIAutoMLWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self.project_name,
                            self.output_path, self.data_loader_path, self.max_trials, self.max_epochs,
                            self.max_size, self.num_channels, self.img_height, self.img_width, 
                            self.separator, self.decimal, self.csv_target_label, self)

    self.Window6.loading_images.start()
    self.Window6.autokeras.start()

    self.Window6.autokeras.request_signal.connect(lambda:nextWindow(self))
    print("AuotKeras finished")  

    self.setCentralWidget(self.Window6)
    self.show()


def nextWindow(self):
    """
    After AutoKeras training is finished, stop the
    the two threads and return to the start window
    of the GUI.
    """
    self.Window6.autokeras.stop_thread()
    self.Window6.loading_images.stop_thread()
    self.GUIStart()