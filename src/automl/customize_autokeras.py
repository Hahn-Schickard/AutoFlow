'''Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: GPL-3.0
============================================================================'''

"""To ensure that AutoKeras works without errors, this script is executed.
It causes no CastToFloat32 layer to be added to the AutoKeras models. This
would generate an error later when converting the models to TensorFlow Lite.

Typical usage example:
win   - python Remove_cast_to_float32.py C:/Users/.../Anaconda3/envs/AutoFlow
linux - python Remove_cast_to_float32.py .../anaconda3/envs/AutoFlow
"""

import sys


def replace_string(path):
    """
    In "autokeras/nodes.py" a code line get changed. As a result, no
    CastToFloat32 layers will be added to the AutoKeras models.

    Args:
        path:   Path to used anaconda environment
    """
    # creating a variable and storing the text
    # that we want to search
    search_text = 'keras_layers.CastToFloat32()(input_node)'

    # creating a variable and storing the text
    # that we want to add
    replace_text = 'input_node #' + search_text

    if 'linux' in sys.platform:
        file_path = '/lib/python3.8/site-packages/autokeras/nodes.py'
    else:
        file_path = '/Lib/site-packages/autokeras/nodes.py'

    # Opening our text file in read only
    # mode using the open() function
    with open(path + file_path, 'r') as f:

        # Reading the content of the file
        # using the read() function and storing
        # them in a new variable
        data = f.read()

        # Searching and replacing the text
        # using the replace() function
        # if text is not replaced yet
        if replace_text in data:
            return
        else:
            data = data.replace(search_text, replace_text)

    # Opening our text file in write only
    # mode to write the replaced content
    with open(path + file_path, 'w') as f:

        # Writing the replaced data in our
        # text file
        f.write(data)

    # Printing Text replaced
    print('Text replaced')


if __name__ == '__main__':
    replace_string(sys.argv[1])
