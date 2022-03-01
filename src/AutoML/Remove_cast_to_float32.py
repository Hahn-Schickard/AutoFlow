import sys

# The file path of the environment used is passed to the function.
# Example path: C:/Users/.../Anaconda3/envs/AutoFlow
def replace_string(path):
    # creating a variable and storing the text
    # that we want to search
    search_text = 'keras_layers.CastToFloat32()(input_node)'
    
    # creating a variable and storing the text
    # that we want to add
    replace_text = 'input_node #' + search_text
    
    # Opening our text file in read only
    # mode using the open() function
    with open(path + '/Lib/site-packages/autokeras/nodes.py', 'r') as f:
    
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
    with open(path + '/Lib/site-packages/autokeras/nodes.py', 'w') as f:
    
        # Writing the replaced data in our
        # text file
        f.write(data)
    
    # Printing Text replaced
    print('Text replaced')


if __name__ == '__main__':
    replace_string(sys.argv[1])