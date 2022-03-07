import numpy as np
import tensorflow_model_optimization as tfmot


def tensorflow_pruning(model, comp, data, pruning_factor=0.50,
                       data_loader=False):
    """
    A passed model is pruned with TensorFlow's pruning. It should be noted that
    only the weights are removed and no reduction in the number of parameters
    can be achieved.

    Args:
        model:          Model which should be pruned
        comp:           Compiler settings
        data:           List containing the data for pruning. These can be
                        passed as data_loader or np.arrays.
                        data_loader:
                        data[0]-->training data, data[1]-->validation data.
                        np.array:
                        data[0]-->training data, data[1]-->training label
        pruning_factor: Integer which says how many percent of the neurons and
                        filters should be deleted
        data_loader:    Is the data from a path data loader or not (file)

    Return:
        pruned_model:     New model after pruning
    """
    print("TF pruning factor: {}, dtype: {}".format(pruning_factor,
                                                    type(pruning_factor)))
    print("TF pruning data_loader:", data_loader)

    prune_low_magnitude = tfmot.sparsity.keras.prune_low_magnitude

    # Compute end step to finish pruning after 20 epochs.
    batch_size = 128
    epochs = 20
    validation_split = 0.2  # 20% of training set will be used for validation.

    if data_loader:
        num_data = data[0].samples
    else:
        num_data = data[0].shape[0] * (1 - validation_split)

    end_step = np.ceil(num_data / batch_size).astype(np.int32) * epochs

    # Define model for pruning.
    pruning_params = {
        'pruning_schedule': tfmot.sparsity.keras.PolynomialDecay(
            initial_sparsity=0.05, final_sparsity=pruning_factor, begin_step=0,
            end_step=end_step)
    }

    model_for_pruning = prune_low_magnitude(model, **pruning_params)

    # prune_low_magnitude` requires a recompile.
    model_for_pruning.compile(**comp)

    model_for_pruning.summary()

    callbacks = [tfmot.sparsity.keras.UpdatePruningStep()]

    if data_loader:
        model_for_pruning.fit(data[0], steps_per_epoch=len(data[0]),
                              validation_data=data[1],
                              validation_steps=len(data[1]),
                              epochs=epochs, callbacks=callbacks)
    else:
        model_for_pruning.fit(data[0], data[1], batch_size=batch_size,
                              epochs=epochs, validation_split=validation_split,
                              callbacks=callbacks)

    pruned_model = tfmot.sparsity.keras.strip_pruning(model_for_pruning)
    pruned_model.summary()

    for i, w in enumerate(pruned_model.get_weights()):
        print(
            "{} -- Total:{}, Zeros: {:.2f}%".format(
                model.weights[i].name, w.size, np.sum(w == 0) / w.size * 100
            )
        )

    pruned_model.compile(**comp)

    if data_loader:
        print("Evaluation of TensorFlow pruned model:", pruned_model.evaluate(
            data[0]))
    else:
        print("Evaluation of TensorFlow pruned model:", pruned_model.evaluate(
            data[0], data[1]))

    return pruned_model
