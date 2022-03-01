## Train a new model with AutoKeras

In the next window the model name, the output path and the data to train the neural network are passed.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_train_2.PNG" width="45%" height="45%">
</p>


In the next window, the task to be solved by the neural network can be selected. Four different tasks are available for selection: Image classification, Image regression, Data classification and Data regression.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_train_3.PNG" width="45%" height="45%">
</p>


Next, some parameters have to be passed to AutoKeras for automatic model generation. These are:
- The number of epochs each model should be trained.
- The number of different models that should be trained.
- The maximum size of the models. (If this parameter is 0, there is no limit to the size of the model).

If the data is passed in the form of images, the height and width of the images (number of pixels), as well as the number of color channels, have to be passed additionally. If everything is passed, the automatic model generation can be started.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_train_4.PNG" width="45%" height="45%">
</p>


In the last window of this part of the AutoFlow tool you have to wait until the automatic model generation is finished. Then you will be returned to the GUI start window.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_train_5.PNG" width="45%" height="45%">
</p>