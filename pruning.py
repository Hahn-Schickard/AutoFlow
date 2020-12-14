from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense, Dropout, Flatten, Activation
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import backend as K
import tensorflow as tf
import numpy as np
from tensorflow.keras.callbacks import EarlyStopping

import tempfile


def load_model_param(model):
    """
    The weights of all layers are stored in layer_params. This array will be used to delete the neurons and reload
    the weights later
    The names of all layers are stored to search for dense and conv layers
    The output shape of each layer is also needed to set the right number of parameters in layers like max_pool
    
    Args: 
        model: Model which should be pruned
            
    Return: 
        layer_name: Names of all layers of the model
        layer_params: All weight matrices of the model
        layer_output_shape: Output shape of all layers of the model
    """
    
    layer_params = []
    layer_names = []
    layer_output_shape = []

    for i in range(0,len(model.layers)):
        layer_names.append(model.layers[i].name)
        layer_params.append(model.layers[i].get_weights())
        layer_output_shape.append(list(model.layers[i].output_shape))
        
    return np.array(layer_names), np.array(layer_params), layer_output_shape



def delete_dense_neuron(new_model_param, layer_name, layer_output_shape, layer, neuron):
    """
    Deletes a given neuron if the layer is a dense layer
    
    Args: 
        new_model_param: Stores the current weights of the model
        layer_name: If layer_name is dense neuron will be removed
        layer_output_shape: Stores the current output shapes of all layers of the model
        layer: Integer of layer number
        neuron: Integer which says which neuron of the given layer (if dense) should be deleted
            
    Return: 
        new_model_param: New model params after deleting a neuron
        layer_output_shape: New output shapes of the model
    """
    
    "If the current layer is a dense layer, weights and the bias are removed for the given layer and neuron"
    if "dense" in layer_name[layer]:
        new_model_param[layer][0] = np.delete(new_model_param[layer][0], neuron, axis=1)   #Gewicht
        new_model_param[layer][1] = np.delete(new_model_param[layer][1], neuron, axis=0)   #Bias
        
        "The new output shape of the layer is restored"
        layer_output_shape[layer][1] = new_model_param[layer][0].shape[1]
        
        "Check if there is a dense layer after the current. The parameters of the next dense layer have connected"
        "to the removed neuron have also to be removed"
        for i in range(layer+1,len(new_model_param)):
            if "dense" in layer_name[i]:
                new_model_param[i][0] = np.delete(new_model_param[i][0], neuron, axis=0)   #Parameter müssen auch aus nächster Gewichtsmatrix gelöscht werden
                return new_model_param, layer_output_shape
            
            "If there is a layer with no parameters like max_pool between the current and the next dense layer"
            "the output neurons are same as these of the current dense layer"            
            if np.array(new_model_param[i]).size == 0:
                layer_output_shape[i][1] = new_model_param[layer][0].shape[1]
            
    else:
        print("No dense layer")
        
    return new_model_param, layer_output_shape
    
def delete_filter(new_model_param, layer_name, layer_output_shape, layer, filter):
    """
    Deletes a given filter if the layer is a conv layer
    
    Args: 
        new_model_param: Stores the current weights of the model
        layer_name: If layer_name is conv neuron will be removed
        layer_output_shape: Stores the current output shapes of all layers of the model
        layer: Integer of layer number
        filter: Integer which says which filter of the given layer (if conv) should be deleted
            
    Return: 
        new_model_param: New model params after deleting a filter
        layer_output_shape: New output shapes of the model
    """
    
    if "conv" in layer_name[layer]:
        new_model_param[layer][0] = np.delete(new_model_param[layer][0], filter, axis=3)   #Filter
        new_model_param[layer][1] = np.delete(new_model_param[layer][1], filter, axis=0)   #Bias
        
        layer_output_shape[layer][3] = new_model_param[layer][0].shape[3]
        
        for i in range(layer+1,len(new_model_param)):
            
            if "conv" in layer_name[i]:
                new_model_param[i][0] = np.delete(new_model_param[i][0], filter, axis=2)
                return new_model_param, layer_output_shape
            
            elif "dense" in layer_name[i]:
                for j in range(0,layer_output_shape[i-2][1]*layer_output_shape[i-2][2]):   #layer before is flatten, we need output shape before layer flatten
                    new_model_param[i][0] = np.delete(new_model_param[i][0], filter, axis=0)
                return new_model_param, layer_output_shape
            
            elif np.array(new_model_param[i]).size == 0:
                for j in range(i+1,len(new_model_param)):
                    if "conv" in layer_name[j]: 
                        layer_output_shape[i][3] = new_model_param[layer][0].shape[3]
                    elif "flatten" in layer_name[j]:
                        layer_output_shape[i][3] = new_model_param[layer][0].shape[3]
                        layer_output_shape[j][1] = layer_output_shape[i][1] * layer_output_shape[i][2] * layer_output_shape[i][3]
    
    else:
        print("No conv layer")
    
    return new_model_param, layer_output_shape



def prun_neurons_dense(layer_names, layer_params, layer_output_shape, prun_layer, prun_factor):
    """
    Deletes neurons from the dense layer. The prun_factor is telling how much percent of the 
    neurons of the dense layer should be deleted.
    
    Args: 
        layer_names: If layer_name is dense neurons will be removed
        layer_params: Stores the current weights of the model
        layer_output_shape: Stores the current output shapes of all layers of the model
        prun_layer: Integer of layer number
        prun_factor: Integer which says how many percent of the dense neurons should be deleted
        
    Return: 
        new_model_param: New model params after deleting the neurons
        num_new_neurons: New number of neurons of the dense layers
        layer_output_shape: New output shapes of the model
    """
    
    'Check if layer to prune is a Dense layer'
    if not "dense" in layer_names[prun_layer]:
        print("No dense layer!")
        return None, None
    
    if prun_factor > 0:
        'Load the weights of the dense layer and add a array where the' 
        'absolut average of the weights for each neurons will be stored'
        new_layer_param = layer_params[prun_layer]
        avg_neuron_w = []

        'Absolute average of the weights arriving at a neuron are written into an array'
        for i in range (0,new_layer_param[0].shape[-1]):
            avg_neuron_w.append(np.average(np.abs(new_layer_param[0][:,i]))) 

        'Absolute average of the weights are sorted and a percantage of these which is given'
        'through the prune factor are stored in prune_neurons, these neurons will be pruned'
        prun_neurons = sorted(range(new_layer_param[0].shape[-1]), key=lambda k: avg_neuron_w[k])[:int((prun_factor*new_layer_param[0].shape[-1])/100)]
        prun_neurons = np.sort(prun_neurons)

        'The number of the new units of the dense layer are stored'
        num_new_neurons = new_layer_param[0].shape[-1] - len(prun_neurons)

        'Deleting the neurons, beginning with the neuron with the highest index'
        if len(prun_neurons) > 0:
            for i in range(len(prun_neurons)-1,-1,-1):
                new_model_param, layer_output_shape = delete_dense_neuron(layer_params, layer_names, layer_output_shape, prun_layer, prun_neurons[i])

        else:
            new_model_param = layer_params
            print("No neurons to prune increase prune factor for dense layers")
        
    else:
        new_model_param = layer_params
        num_new_neurons = layer_params[prun_layer][0].shape[-1]
        print("No pruning implemented for dense layers")
    
    return new_model_param, num_new_neurons, layer_output_shape



def prun_filters_conv(layer_names, layer_params, layer_output_shape, prun_layer, prun_factor):
    """
    Deletes filters from the conv layer. The prun_factor is telling how much percent of the 
    filters of the conv layer should be deleted.
    
    Args: 
        layer_names: If layer_name is conv, filters will be removed
        layer_params: Stores the current weights of the model
        layer_output_shape: Stores the current output shapes of all layers of the model
        prun_layer: Integer of layer number
        prun_factor: Integer which says how many percent of the filters should be deleted
        
    Return: 
        new_model_param: New model params after deleting the filters
        num_new_filters: New number of filters of the conv layers
        layer_output_shape: New output shapes of the model
    """
    
    'Check if layer to prune is a Conv layer'
    if not "conv" in layer_names[prun_layer]:
        print("No Conv layer!")
        return None, None
    
    if prun_factor > 0:
        'Load the filters of the conv layer and add a array where the' 
        'absolut average filter values will be stored'
        filters = layer_params[prun_layer]
        avg_filter_w = []

        'Absolute average of the filter values are written into an array'
        for i in range (0,filters[0].shape[-1]):
            avg_filter_w.append(np.average(np.abs(filters[0][:,:,:,i])))

        'Absolute average of the filter values are sorted and a percantage of these which is given'
        'through the prune factor are stored in prune_filters, these filters will be pruned'
        prun_filter = sorted(range(filters[0].shape[-1]), key=lambda k: avg_filter_w[k])[:int((prun_factor*filters[0].shape[-1])/100)]
        prun_filter = np.sort(prun_filter)

        'The number of the new filters of the conv layer are stored'
        num_new_filter = filters[0].shape[-1] - len(prun_filter)

        'Deleting the filters, beginning with the filter with the highest index'
        if len(prun_filter) > 0:
            for i in range(len(prun_filter)-1,-1,-1):
                new_model_param, layer_output_shape = delete_filter(layer_params, layer_names, layer_output_shape, prun_layer, prun_filter[i])

        else:
            new_model_param = layer_params
            print("No filter to prune increase prune factor for conv layers")
        
    else:
        new_model_param = layer_params
        num_new_filter = layer_params[prun_layer][0].shape[-1]
        print("No pruning implemented for conv layers")
    
    return new_model_param, num_new_filter, layer_output_shape



def model_pruning(layer_names, layer_params, layer_output_shape, num_new_neurons, num_new_filters, prun_factor_dense, prun_factor_conv):
    """
    Deletes neurons and filters from all dense and conv layers. The two prunfactors are 
    telling how much percent of the neurons and the filters should be deleted.
    
    Args: 
        layer_names: The names of all layers of the model
        layer_params: Stores the current weights of the model
        layer_output_shape: Stores the current output shapes of all layers of the model
        num_new_neurons: Number of neurons of the dense layers
        num_new_filters: Number of filters of the conv layers
        prun_factor_dense: Integer which says how many percent of the neurons should be deleted
        prun_factor_conv: Integer which says how many percent of the filters should be deleted
        
    Return: 
        layer_params: New model params after deleting the neurons and filters
        num_new_neurons: New number of filters of the dense layers
        num_new_filters: New number of filters of the conv layers
        layer_output_shape: New output shapes of the model after deleting neurons and filters
    """
    
    for i in range(0,len(layer_params)-2):
        if "dense" in layer_names[i]:
            layer_params, num_new_neurons[i], layer_output_shape = prun_neurons_dense(layer_names, layer_params, layer_output_shape, i, prun_factor_dense)

        elif "conv" in layer_names[i]:
            layer_params, num_new_filters[i], layer_output_shape = prun_filters_conv(layer_names, layer_params, layer_output_shape, i, prun_factor_conv)

        else:
            ("No pruning for this layer")
            
    return layer_params, num_new_neurons, num_new_filters, layer_output_shape



def build_pruned_model(pruned_model, new_model_param, layer_names, num_new_neurons, num_new_filters):
    """
    The new number of neurons and filters are changed in the model config.
    Load the new weight matrices into the model.
    
    Args: 
        pruned_model: Model which should be pruned
        new_model_param: Stores the new weights of the model
        layer_names: The names of all layers of the model
        num_new_neurons: Number of neurons of the dense layers
        num_new_filters: Number of filters of the conv layers
        
    Return: 
        pruned_model: New model after pruning all dense and conv layers
    """
    
    model_config = pruned_model.get_config()
    
    for i in range(0,len(model_config['layers'])-2):
        if "dense" in model_config['layers'][i]['config']['name']:
            model_config['layers'][i]['config']['units'] = num_new_neurons[i]

        elif "conv" in model_config['layers'][i]['config']['name']:
            model_config['layers'][i]['config']['filters'] = num_new_filters[i]

        else:
            print("No dense or conv")
            
    print("Before pruning:")        
    pruned_model.summary()
    
    pruned_model = Sequential.from_config(model_config)
    
    print("After pruning:")
    pruned_model.summary()
    
    pruned_model.compile(optimizer='adam', metrics=['accuracy'], loss='categorical_crossentropy')
    
    
    for i in range(0,len(pruned_model.layers)):
        if 'conv' in layer_names[i] or 'dense' in layer_names[i]:
            pruned_model.layers[i].set_weights(new_model_param[i])
    
    return pruned_model



def pruning(keras_model, x_train, y_train, prun_factor_dense=10, prun_factor_conv=10):
    """
    A given keras model get pruned. The factor for dense and conv says how many percent
    of the dense and conv layers should be deleted. After pruning the model will be
    retrained.
    
    Args: 
        keras_model: Model which should be pruned
        x_train: Training data to retrain the model after pruning
        y_train: Labels of training data to retrain the model after pruning
        prun_factor_dense: Integer which says how many percent of the neurons should be deleted
        prun_factor_conv: Integer which says how many percent of the filters should be deleted
        
    Return: 
        pruned_model: New model after pruning and retraining
    """
    
    if callable(getattr(keras_model, "predict", None)) :
        model = keras_model
    elif isinstance(keras_model, str) and ".h5" in keras_model:
        model = load_model(keras_model)
    else:
        print("No model given to prune")
    
    
    layer_names, layer_params, layer_output_shape = load_model_param(model)
    num_new_neurons = np.zeros(shape=len(layer_params), dtype=np.int16)
    num_new_filters = np.zeros(shape=len(layer_params), dtype=np.int16)

    layer_params, num_new_neurons, num_new_filters, layer_output_shape = model_pruning(layer_names, layer_params, layer_output_shape, num_new_neurons, num_new_filters, prun_factor_dense, prun_factor_conv)

    print("Finish with pruning")

    pruned_model = build_pruned_model(model, layer_params, layer_names, num_new_neurons, num_new_filters)

    earlystopper = EarlyStopping(monitor='val_accuracy', min_delta= 1e-3, mode='min', verbose=1, patience=5, restore_best_weights=True)
    history = pruned_model.fit(x_train, y_train, validation_split=0.2, epochs=1, batch_size=256, callbacks=[earlystopper])
    
    return pruned_model


def pruning_for_acc(keras_model, x_train, y_train, x_test, y_test, pruning_acc=None, max_acc_loss=1):
    """
    A given keras model get pruned. Either an accuracy value (in %) can be specified, which 
    the minimized model must still achieve. Or the maximum loss of accuracy (in %) that 
    the minimized model may experience. The model is reduced step by step until the 
    accuracy value is underrun or the accuracy loss is exceeded.
    
    Args: 
        keras_model: Model which should be pruned
        x_train: Training data to retrain the model after pruning
        y_train: Labels of training data to retrain the model after pruning
        x_test: Test data for evaluation of the minimized model
        y_test: Labels of test data for evaluation of the minimized model
        pruning_acc: Integer which says which accuracy value (in %) should not be fall below
        max_acc_loss: Integer which says which accuracy loss (in %) should not be exceed 
        
    Return: 
        pruned_model: New model after pruning and retraining
    """
    
    original_model = load_model(keras_model)
    original_model.compile(optimizer='adam', metrics=['accuracy'], loss='categorical_crossentropy')
    original_model_acc = original_model.evaluate(x_test,y_test)[-1]
    
    for i in range(5,100,5):
        model = pruning(original_model, x_train, y_train, prun_factor_dense=i, prun_factor_conv=i)
        
        if pruning_acc != None:
            if model.evaluate(x_test,y_test)[-1] < pruning_acc:
                print(i-5)
                if i == 5:
                    pruned_model = model
                return pruned_model
            pruned_model = model
            
        else:
            if model.evaluate(x_test,y_test)[-1] < (original_model_acc-(max_acc_loss/100)):
                print(i-5)
                return pruned_model
            pruned_model = model
    
    return pruned_model