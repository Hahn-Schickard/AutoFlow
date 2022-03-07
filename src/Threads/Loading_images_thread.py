'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

import time
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class LoadingImages(QThread):
    """Loading screen thread.

    Attributes:
        load_png:     The image which is represented on the "create_project"
        loading_img: The different images representing the loadingscreen
    """

    def __init__(self, load_png):
        QThread.__init__(self)
        self.load_png = load_png
        self.loading_img = 0

    def run(self):
        """Activates the thread

        Changes the image of the loading screen every 0.75 seconds.
        """

        while(self.isRunning()):

            if self.loading_img < 15:
                self.loading_img += 1
            else:
                self.loading_img = 1

            time.sleep(0.75)

            self.load_png.setPixmap(QPixmap(os.path.join(
                'src', 'gui_layout', 'images', 'gui_loading_images',
                'GUI_load_' + str(self.loading_img) + '.png')))

    def stop_thread(self):
        """Ends the thread
        """
        self.terminate()
