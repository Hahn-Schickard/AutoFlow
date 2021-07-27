#PRUNING NEU

from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Model
import numpy as np
from tensorflow.keras.callbacks import EarlyStopping
import tensorflow as tf
import os

from GUI._Helper import ThresholdCallback


def get_layer_shape_dense(new_model_param,layer):	
    """	
    Gets the struture of the new generated model and return the shape of the current layer	
    	
    Args: 	
        new_model_param: The params of the new generated model	
        layer: the current layer we want the shape from	
            	
    Return: 	
        shape of the current layer	
    """	
    return new_model_param[layer][0].shape[1]	
    
    
def get_layer_shape_conv(new_model_param,layer):	
    """	
    Gets the struture of the new generated model and return the shape of the current layer	
    	
    Args: 	
        new_model_param: The params of the new generated model	
        layer: the current layer we want the shape from	
            	
    Return: 	
        shape of the current layer	
    """	
    return new_model_param[layer][0].shape[3]



def load_model_param(model):
    """
    Gets layer names, layer weights and output_shape of each layer from the given keras model.
    The weights of all layers are stored in layer_params. This array will be used to delete the neurons and reload
    the weights later
    The type of all layers are stored in layer_types to search for dense and conv layers.
    The output shape of each layer is also needed to set the right number of parameters in layers like max_pool
    
    Args: 
        model: Model which should be pruned
            
    Return: 
        layer_types (np.array): Type of all layers of the model	
        layer_params (np.array): All weight matrices of the model	
        layer_output_shape (list): Output shape of all layers of the model
    """
    
    layer_params = []
    layer_types = []
    layer_output_shape = []
    layer_bias = []

    for layer in model.layers:	
        layer_types.append(layer.__class__.__name__)	
        layer_params.append(layer.get_weights())	
        layer_output_shape.append(list(layer.output_shape))
        try:
            layer_bias.append(layer.use_bias)
        except:
            layer_bias.append(None)
        
    return np.array(layer_types), np.array(layer_params), layer_output_shape, layer_bias



def delete_dense_neuron(new_model_param, layer_types, layer_output_shape, layer_bias, layer, neuron):
    """
    Deletes a given neuron if the layer is a dense layer
    
    Args: 
        new_model_param: Stores the current weights of the model
        layer_types: If layer_types is dense, neuron will be removed
        layer_output_shape: Stores the current output shapes of all layers of the model
        layer: Integer of layer number (0,1,2, ...)
        neuron: Integer which says which neuron of the given layer (if dense) should be deleted
            
    Return: 
        new_model_param: New model params after deleting a neuron
        layer_output_shape: New output shapes of the model
    """
    
    "If the current layer is a dense layer, weights and the bias are removed for the given layer and neuron"
    if layer_types[layer] == "Dense":
        new_model_param[layer][0] = np.delete(new_model_param[layer][0], neuron, axis=1)   #weight
        if layer_bias[layer] == True:
            new_model_param[layer][1] = np.delete(new_model_param[layer][1], neuron, axis=0)   #Bias
        
        "The new output shape of the layer is restored"
        layer_output_shape[layer][1] = get_layer_shape_dense(new_model_param, layer)
        
        "Check if there is a dense layer after the current. The parameters of the next dense layer were connected"	
        "to the removed neuron and also have to be removed"	

        "If there is a layer with no parameters like max_pool between the current and the next dense layer"	
        "the output neurons are the same as those of the current dense layer" 
        
        for i in range(layer+1,len(new_model_param)):
            if layer_types[i] == "Dense":
                new_model_param[i][0] = np.delete(new_model_param[i][0], neuron, axis=0)   #Parameters also have to be deleted from the next weight matrix
                return new_model_param, layer_output_shape
            
            "If there is a layer with no parameters like max_pool between the current and the next dense layer"
            "the output neurons are the same as those of the current dense layer"            
            if np.array(new_model_param[i]).size == 0:
                layer_output_shape[i][1] = get_layer_shape_dense(new_model_param, layer)
            
    else:
        print("No dense layer")
        
    return new_model_param, layer_output_shape
    
def delete_filter(new_model_param, layer_types, layer_output_shape, layer_bias, layer, filter):
    """
    Deletes a given filter if the layer is a conv layer
    
    Args: 
        new_model_param: Stores the current weights of the model
        layer_types: If layer_types is Conv2D, filter will be removed
        layer_output_shape: Stores the current output shapes of all layers of the model
        layer: Integer of layer number
        filter: Integer which says which filter of the given layer (if conv) should be deleted
            
    Return: 
        new_model_param: New model params after deleting a filter
        layer_output_shape: New output shapes of the model
    """
    
    
    "If the current layer is a conv layer, weights and the bias are removed for the given layer and filter"
    if layer_types[layer] == "Conv2D":
        new_model_param[layer][0] = np.delete(new_model_param[layer][0], filter, axis=3)   #Delete Filter
        if layer_bias[layer] == True:
            new_model_param[layer][1] = np.delete(new_model_param[layer][1], filter, axis=0)   #Delete Bias
        
        "The new output shape of the layer is restored"
        layer_output_shape[layer][3] = get_layer_shape_conv(new_model_param, layer)
        
        "Check if there is a dense/conv layer after the current. The parameters of the next dense layer were connected"
        "to the removed neuron and also have to be removed"
        for dense_layer in range(layer+1,len(new_model_param)):
            
            if len(new_model_param[dense_layer]) != 0:
        
                if layer_types[dense_layer] == "Dense":
                    new_model_param[dense_layer][0] = np.delete(new_model_param[dense_layer][0], filter, axis=0)
                    return new_model_param, layer_output_shape
                if layer_bias[dense_layer] == True or layer_bias[dense_layer] == False:
                    new_model_param[dense_layer][0] = np.delete(new_model_param[dense_layer][0], filter, axis=2)
                    layer_output_shape[dense_layer][3] = get_layer_shape_conv(new_model_param, layer) 
                    if layer_types[dense_layer] == "Conv2D":
                        return new_model_param, layer_output_shape
                elif layer_bias[dense_layer] == None:
                    for i in range(0,len(new_model_param[dense_layer])):
                        new_model_param[dense_layer][i] = np.delete(new_model_param[dense_layer][i], filter, axis=0)
                    layer_output_shape[dense_layer][3] = get_layer_shape_conv(new_model_param, layer)
            
            

            else:
                if layer_types[dense_layer] == "Dense":
                    break
                elif layer_types[dense_layer] == "Flatten":
                    layer_output_shape[dense_layer][1] = np.prod(layer_output_shape[dense_layer-1][1:4])
                    for i in range(np.multiply(np.prod(layer_output_shape[dense_layer-1][1:3]),filter-1), np.multiply(np.prod(layer_output_shape[dense_layer-1][1:3]),filter)):
                        new_model_param[dense_layer+1][0] = np.delete(new_model_param[dense_layer+1][0], i, axis=0)
                    break
                else:
                    if len(layer_output_shape[dense_layer]) == 4:
                        layer_output_shape[dense_layer][3] = get_layer_shape_conv(new_model_param, layer)
                    elif len(layer_output_shape[dense_layer]) == 2:
                        layer_output_shape[dense_layer][1] = get_layer_shape_conv(new_model_param, layer)
            
    else:
        print("No conv layer")
    
    return new_model_param, layer_output_shape


def get_neurons_to_prune_l1(layer_params,prun_layer,prun_factor):
    """
    Calculate the neurons who get Pruned with the L1 Norm 
    
    Args:
        layer_params: Stores the current weights of the model
        prun_layer: Integer of layer number
        prun_factor: Integer which says how many percent of the dense neurons should be deleted    
            
    Return: 
        prune_neurons: get indizies of neurons to prune
        num_new_neuron: New shape of the weight Matrix
    """
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
    return prun_neurons,num_new_neurons


def get_neurons_to_prune_l2(layer_params,prun_layer,prun_factor):
    """
    Calculate the neurons who get Pruned with the L1 Norm 
    
    Args:
        layer_params: Stores the current weights of the model
        prun_layer: Integer of layer number
        prun_factor: Integer which says how many percent of the dense neurons should be deleted    
            
    Return: 
        prune_neurons: get indizies of neurons to prune
        num_new_neuron: New shape of the weight Matrix
    """    
    new_layer_param = layer_params[prun_layer]
    avg_neuron_w = []

    'Absolute average of the weights arriving at a neuron are written into an array'
    for i in range (0,new_layer_param[0].shape[-1]):
        avg_neuron_w.append(np.linalg.norm(new_layer_param[0][:,i])) 

    
    'Absolute average of the weights are sorted and a percantage of these which is given'
    'through the prune factor are stored in prune_neurons, these neurons will be pruned'
    prun_neurons = sorted(range(new_layer_param[0].shape[-1]), key=lambda k: avg_neuron_w[k])[:int((prun_factor*new_layer_param[0].shape[-1])/100)]
    prun_neurons = np.sort(prun_neurons)

    'The number of the new units of the dense layer are stored'
    num_new_neurons = new_layer_param[0].shape[-1] - len(prun_neurons)
    return prun_neurons,num_new_neurons




def prun_neurons_dense(layer_types, layer_params, layer_output_shape, layer_bias, prun_layer, prun_factor,metric):
    """
    Deletes neurons from the dense layer. The prun_factor is telling how much percent of the 
    neurons of the dense layer should be deleted.
    
    Args: 
        layer_types: If layer_types is dense neurons will be removed
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
    if layer_types[prun_layer] != "Dense":
        print("No dense layer!")
        return None, None
    
    if prun_factor > 0:
        'Load the weights of the dense layer and add an array where the' 
        'absolut average of the weights for each neurons will be stored'
        new_layer_param = layer_params[prun_layer]
        avg_neuron_w = []

        if metric == 'L1':
            prun_neurons,num_new_neurons=get_neurons_to_prune_l1(layer_params,prun_layer,prun_factor)
        elif metric == 'L2':
            prun_neurons,num_new_neurons=get_neurons_to_prune_l2(layer_params,prun_layer,prun_factor)
        else:
            prun_neurons,num_new_neurons=get_neurons_to_prune_l1(layer_params,prun_layer,prun_factor)

        '''
        'Absolute average of the weights arriving at a neuron are written into an array'
        for i in range (0,new_layer_param[0].shape[-1]):
            avg_neuron_w.append(np.average(np.abs(new_layer_param[0][:,i]))) 

        'Absolute average of the weights are sorted and a percantage of these which is given'
        'through the prune factor are stored in prune_neurons, these neurons will be pruned'
        prun_neurons = sorted(range(new_layer_param[0].shape[-1]), key=lambda k: avg_neuron_w[k])[:int((prun_factor*new_layer_param[0].shape[-1])/100)]
        prun_neurons = np.sort(prun_neurons)

        'The number of the new units of the dense layer are stored'
        num_new_neurons = new_layer_param[0].shape[-1] - len(prun_neurons)
        '''

        'Deleting the neurons, beginning with the neuron with the highest index'
        if len(prun_neurons) > 0:
            for i in range(len(prun_neurons)-1,-1,-1):
                new_model_param, layer_output_shape = delete_dense_neuron(layer_params, layer_types, layer_output_shape, layer_bias, prun_layer, prun_neurons[i])

        else:
            new_model_param = layer_params
            print("No neurons to prune increase prune factor for dense layers")
        
    else:
        new_model_param = layer_params
        num_new_neurons = layer_params[prun_layer][0].shape[-1]
        print("No pruning implemented for dense layers")
    
    return new_model_param, num_new_neurons, layer_output_shape

def get_filter_to_prune_avarage(layer_params,prun_layer,prun_factor):
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
    return prun_filter,num_new_filter
    
def get_filter_to_prune_L2(layer_params,prun_layer,prun_factor):
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
    return prun_filter,num_new_filter

    

def prun_filters_conv(layer_types, layer_params, layer_output_shape, layer_bias, prun_layer, prun_factor,metric='L1'):
    """
    Deletes filters from the conv layer. The prun_factor is telling how much percent of the 
    filters of the conv layer should be deleted.
    
    Args: 
        layer_types: If layer_types is Conv2D, filters will be removed
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
    if layer_types[prun_layer] != "Conv2D":
        print("No Conv layer!")
        return None, None
    if prun_factor > 0:
        if metric == 'L1':
            prun_filter,num_new_filter=get_filter_to_prune_avarage(layer_params,prun_layer,prun_factor)
        elif metric == 'L2':
            prun_filter,num_new_filter=get_filter_to_prune_L2(layer_params,prun_layer,prun_factor)
        else:
            prun_filter,num_new_filter=get_filter_to_prune_avarage(layer_params,prun_layer,prun_factor)
        
        'Deleting the filters, beginning with the filter with the highest index'
        if len(prun_filter) > 0:
            for i in range(len(prun_filter)-1,-1,-1):
                new_model_param, layer_output_shape = delete_filter(layer_params, layer_types, layer_output_shape, layer_bias, prun_layer, prun_filter[i])

        else:
            new_model_param = layer_params
            print("No filter to prune increase prune factor for conv layers")
        
    else:
        new_model_param = layer_params
        num_new_filter = layer_params[prun_layer][0].shape[-1]
        print("No pruning implemented for conv layers")
    
    return new_model_param, num_new_filter, layer_output_shape



def model_pruning(layer_types, layer_params, layer_output_shape, layer_bias, num_new_neurons, num_new_filters, prun_factor_dense, prun_factor_conv,metric):
    """
    Deletes neurons and filters from all dense and conv layers. The two prunfactors are 
    telling how much percent of the neurons and the filters should be deleted.
    
    Args: 
        layer_types: The types of all layers of the model
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
        if layer_types[i] == "Dense":
            layer_params, num_new_neurons[i], layer_output_shape = prun_neurons_dense(layer_types, layer_params, layer_output_shape, layer_bias, i, prun_factor_dense,metric)
        elif layer_types[i] == "Conv2D":
            layer_params, num_new_filters[i], layer_output_shape = prun_filters_conv(layer_types, layer_params, layer_output_shape, layer_bias, i, prun_factor_conv,metric)

        else:
            ("No pruning for this layer")
            
    # print("layer_output_shape")        
    # for i in range(0,len(layer_output_shape)):
    #     print(layer_types[i])
    #     print(layer_output_shape[i])
            
    return layer_params, num_new_neurons, num_new_filters, layer_output_shape



def build_pruned_model(model, new_model_param, layer_types, num_new_neurons, num_new_filters,comp):
    """
    The new number of neurons and filters are changed in the model config.
    Load the new weight matrices into the model.
    
    Args: 
        model: Model which should be pruned
        new_model_param: Stores the new weights of the model
        layer_types: The types of all layers of the model
        num_new_neurons: Number of neurons of the dense layers
        num_new_filters: Number of filters of the conv layers
        
    Return: 
        pruned_model: New model after pruning all dense and conv layers
    """
    
    model_config = model.get_config()

    
    '''
    For functional model first layer is the input layer.
    For sequential model the first layer is the layer after the input layer
    '''
    a=1
    if layer_types[0] == 'InputLayer':
        a=0
        
        
    for i in range(0,len(model_config['layers'])-3):
        if model_config['layers'][i+a]['class_name'] == "Dense": #i+1 because first layer of model is the inputlayer
            print("Dense")
            model_config['layers'][i+a]['config']['units'] = num_new_neurons[i]

        elif model_config['layers'][i+a]['class_name'] == "Conv2D":
            print("Conv2D")
            model_config['layers'][i+a]['config']['filters'] = num_new_filters[i]
            
        elif model_config['layers'][i+a]['class_name'] == "Reshape":
            temp_list = list(model_config['layers'][i+a]['config']['target_shape'])
            cur_layer=i
            cur_filters = num_new_filters[cur_layer]
            #Get number of filters of last Conv layer
            if cur_filters == 0:
                while cur_filters==0:
                    cur_layer-=1
                    cur_filters = num_new_filters[cur_layer]  
            temp_list[2] = cur_filters
            temp_tuple = tuple(temp_list)
            model_config['layers'][i+a]['config']['target_shape'] = temp_tuple

        else:
            print("No Dense or Conv2D")
            
    print("Before pruning:")        
    model.summary()
    
    # for i in range(0,len(new_model_param)):
    #     print(layer_types[i])
    #     print(np.asarray(new_model_param[i]).shape)
    
    if "Sequential" in str(model):
        pruned_model = Sequential.from_config(model_config)
    elif "Functional" in str(model):
        pruned_model = Model.from_config(model_config)
    
    print("After pruning:")
    pruned_model.summary()
    
    # print("new_model_param")
    for i in range(0,len(pruned_model.layers)):
        # print(layer_types[i])
        if len(new_model_param[i]) != 0:
            # print(np.asarray(new_model_param[i][0]).shape)
            # print(np.asarray(new_model_param[i]).shape)
            pruned_model.layers[i].set_weights(new_model_param[i])
        else:
            None
            # print("No weights to set!")
    
    pruned_model.compile(**comp)
    
    return pruned_model



def pruning(keras_model, x_train, y_train,comp,fit, prun_factor_dense=10, prun_factor_conv=10,metric='L1'):
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
    
    
    layer_types, layer_params, layer_output_shape, layer_bias = load_model_param(model)
    num_new_neurons = np.zeros(shape=len(layer_params), dtype=np.int16)
    num_new_filters = np.zeros(shape=len(layer_params), dtype=np.int16)

    layer_params, num_new_neurons, num_new_filters, layer_output_shape = model_pruning(layer_types, layer_params, layer_output_shape, layer_bias, num_new_neurons, num_new_filters, prun_factor_dense, prun_factor_conv,metric)

    print("Finish with pruning")

    pruned_model = build_pruned_model(model, layer_params, layer_types, num_new_neurons, num_new_filters,comp)

    #earlystopper = EarlyStopping(monitor='val_accuracy', min_delta= 1e-3, mode='min', verbose=1, patience=5, restore_best_weights=True)
    history = pruned_model.fit(x_train, y_train, **fit)
    
    return pruned_model


def pruning_for_acc(keras_model, x_train, x_val_y_train, comp, pruning_acc=None, max_acc_loss=5, num_classes=None, label_one_hot=None, data_loader_path=None):
    """
    A given keras model gets pruned. Either an accuracy value (in %) can be specified, which 
    the minimized model must still achieve. Or the maximum loss of accuracy (in %) that 
    the minimized model may experience. The model is reduced step by step until the 
    accuracy value is underrun or the accuracy loss is exceeded.
    
    Args: 
        keras_model:      Model which should be pruned
        x_train:          Training data to retrain the model after pruning
        x_val_y_train:    Labels of training data to retrain the model after pruning
        comp:             Compiler settings
        pruning_acc:      Integer which says which accuracy value (in %) should not be fall below. 
                          If pruning_acc is not defined, it is Baseline - 5%
        max_acc_loss:     Integer which says which accuracy loss (in %) should not be exceed
        num_classes:      Number of different classes of the model
        label_one_hot:    Boolean value if labels are one hot encoded or not
        data_loader_path: Boolean value if labels are one hot encoded or not 
        
    Return: 
        pruned_model:     New model after pruning
    """

    pruning_factor = 5
    last_pruning_step = None
    all_pruning_factors = [5]
    lowest_pruning_factor_not_working = 100
    original_model_acc = None
    req_acc = None

    if callable(getattr(keras_model, "predict", None)) :
        original_model = keras_model
    elif isinstance(keras_model, str) and ".h5" in keras_model:
        original_model = load_model(keras_model)
    else:
        print("No model given to prune")

    original_model.compile(**comp)

    if pruning_acc != None:
        req_acc = pruning_acc/100
    else:
        if os.path.isfile(data_loader_path):
            original_model_acc = original_model.evaluate(x_train,x_val_y_train)[-1]
        elif os.path.isdir(data_loader_path):
            original_model_acc = original_model.evaluate_generator(x_val_y_train)[-1]
        print(original_model_acc)
        req_acc = original_model_acc-(max_acc_loss/100)
     
    
    train_epochs = 10
    # early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
    threshold = ThresholdCallback(req_acc)
    callbacks=[threshold]#, early_stopping]
    
    
    
    
    while pruning_factor <= 95:
        
        print("Next pruning factors: " + str(pruning_factor))
        
        model = prune_model(original_model, prun_factor_dense=pruning_factor, prun_factor_conv=pruning_factor, metric='L1', comp=None, num_classes=num_classes, label_one_hot=label_one_hot)
        
        if os.path.isfile(data_loader_path):
            history = model.fit(x=x_train, y=x_val_y_train, batch_size=64, validation_split=0.2, epochs=train_epochs, callbacks=callbacks)
        elif os.path.isdir(data_loader_path):
            history = model.fit_generator(x_train, steps_per_epoch=len(x_train),
                validation_data=x_val_y_train, validation_steps=len(x_val_y_train), epochs=train_epochs, callbacks=callbacks)
             
        if history.history['val_accuracy'][-1] < req_acc:
            #Required accuracy is not reached
            if lowest_pruning_factor_not_working > pruning_factor:
                lowest_pruning_factor_not_working = pruning_factor

            if pruning_factor == 5:
                print("No pruning possible")
                return model

            if last_pruning_step == 2:
                print("Pruningfactor dense and conv: " + str(pruning_factor-last_pruning_step))
                return pruned_model
            elif last_pruning_step == 5:
                pruning_factor -= 3
                last_pruning_step = 2
            elif last_pruning_step == 10:
                pruning_factor -= 5
                last_pruning_step = 5
            elif last_pruning_step == 15:
                pruning_factor -= 5
                last_pruning_step = 10

        else:
            #Required accuracy is reached
            pruned_model = model
            #Set pruning factor for next pruning step   
            if len(history.history['val_accuracy']) <= int(0.3*train_epochs):
                pruning_factor += 15
                last_pruning_step = 15
            elif len(history.history['val_accuracy']) <= int(0.5*train_epochs):
                pruning_factor += 10
                last_pruning_step = 10
            elif len(history.history['val_accuracy']) <= int(0.7*train_epochs):
                pruning_factor += 5
                last_pruning_step = 5
            elif len(history.history['val_accuracy']) > int(0.7*train_epochs):
                pruning_factor += 2
                last_pruning_step = 2
                
                
        if lowest_pruning_factor_not_working < pruning_factor:
            #Check if pruning factor is higher than the lowest one which didn't work
            #and adjust the pruning factor if it's true
            if lowest_pruning_factor_not_working - (pruning_factor-last_pruning_step) <= 2:
                print("Pruningfactor dense and conv: " + str(pruning_factor-last_pruning_step))
                return pruned_model
            elif lowest_pruning_factor_not_working - (pruning_factor-last_pruning_step) <= 5:
                pruning_factor = (pruning_factor-last_pruning_step) + 2
                last_pruning_step = 2

        if all_pruning_factors.count(pruning_factor) >= 1:
            #Check if the pruning factor for next iteration was already applied
            if history.history['val_accuracy'][-1] < req_acc:
                #If required accuracy wasn't reached, the pruning factor is lowered in the step before.
                #If the new pruning factor was already applied, this is one which worked,
                #so you increase it a little step.
                if last_pruning_step == 2 or last_pruning_step == 5:
                    pruning_factor += 2
                    last_pruning_step = 2
                elif last_pruning_step == 10:
                    pruning_factor += 5
                    last_pruning_step = 5
                elif last_pruning_step == 15:
                    pruning_factor += 10
                    last_pruning_step = 10
            else:
                #If required accuracy was reached, the pruning factor is increased in the step before.
                #If the new pruning factor was already applied, this is one which didn't work,
                #so you lower it a little step.
                if last_pruning_step == 2 or last_pruning_step == 5:
                    pruning_factor -= 3
                    last_pruning_step = 2
                elif last_pruning_step == 10:
                    pruning_factor -= 5
                    last_pruning_step = 5
                elif last_pruning_step == 15:
                    pruning_factor -= 10
                    last_pruning_step = 10
                
        all_pruning_factors.append(pruning_factor)
        print("all_pruning_factors: " + str(all_pruning_factors))
        print("lowest_pruning_factor_not_working: " + str(lowest_pruning_factor_not_working))
        
        
    return pruned_model
    
    
def prune_model(keras_model, prun_factor_dense=10, prun_factor_conv=10, metric='L1', comp=None, num_classes=None, label_one_hot=None):
    """
    A given keras model get pruned. The factor for dense and conv says how many percent
    of the dense and conv layers should be deleted. After pruning the model will be
    retrained.
    
    Args: 
        keras_model:       Model which should be pruned
        prun_factor_dense: Integer which says how many percent of the neurons should be deleted
        prun_factor_conv:  Integer which says how many percent of the filters should be deleted
        metric:            Metric which should be used to prune the model
        comp:              Dictionary with compiler settings
        num_classes:       Number of different classes of the model
        label_one_hot:     Boolean value if labels are one hot encoded or not 
        
    Return: 
        pruned_model:      New model after pruning 
    """
    
    if callable(getattr(keras_model, "predict", None)) :
        model = keras_model
    elif isinstance(keras_model, str) and ".h5" in keras_model:
        model = load_model(keras_model)
    else:
        print("No model given to prune")

    if num_classes <= 2 and comp == None:
        comp = {
        "optimizer": 'adam',
        "loss": tf.keras.losses.BinaryCrossentropy(),
        "metrics": 'accuracy'}    
    elif num_classes > 3 and comp == None:
        if label_one_hot == True:
            comp = {
            "optimizer": 'adam',
            "loss": tf.keras.losses.CategoricalCrossentropy(),
            "metrics": 'accuracy'}  
        else:
            comp = {
            "optimizer": 'adam',
            "loss": tf.keras.losses.SparseCategoricalCrossentropy(),
            "metrics": 'accuracy'}
    
    
    layer_types, layer_params, layer_output_shape, layer_bias = load_model_param(model)
    num_new_neurons = np.zeros(shape=len(layer_params), dtype=np.int16)
    num_new_filters = np.zeros(shape=len(layer_params), dtype=np.int16)

    layer_params, num_new_neurons, num_new_filters, layer_output_shape = model_pruning(layer_types, layer_params, layer_output_shape, layer_bias, num_new_neurons, num_new_filters, prun_factor_dense, prun_factor_conv,metric)
    
    
    print("Finish with pruning")
    
    # for i in range(0,len(layer_params)):
    #     try:
    #         print(layer_types[i])
    #         print(np.asarray(layer_params[i][0]).shape)
    #     except:
    #         print("No Parameter in layer")

    pruned_model = build_pruned_model(model, layer_params, layer_types, num_new_neurons, num_new_filters, comp)
    
    print("Model built")
    
    return pruned_model