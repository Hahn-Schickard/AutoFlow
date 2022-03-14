'''Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: GPL-3.0
============================================================================'''

import numpy as np
from tensorflow.keras.datasets import mnist


def get_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0

    x_train = np.expand_dims(x_train, 3)
    x_test = np.expand_dims(x_test, 3)

    return x_train, y_train, x_test, y_test
