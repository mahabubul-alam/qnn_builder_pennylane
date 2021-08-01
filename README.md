### QNN Builder (PennyLane)
You can build QNN models with various encoding methods, parametric layer architectures, and measurement operations using the python scripts in this repository. Supports for more encoding methods/parametric layers/measurements will be added in the future. For currently supported methods, please refer to:
* https://github.com/mahabubul-alam/qnn_builder_pennylane/blob/main/app/encoding_circuits.py
* https://github.com/mahabubul-alam/qnn_builder_pennylane/blob/main/app/parametric_circuits.py
* https://github.com/mahabubul-alam/qnn_builder_pennylane/blob/main/app/measurement_circuits.py

### How to Use

Please follow this example: https://github.com/mahabubul-alam/qnn_builder_pennylane/blob/main/variational_binary_classifier_example.py

```
python variational_binary_classifier_example.py
```

```
Epoch 1/3
29/29 [==============================] - 113s 4s/step - loss: 0.1693
Epoch 2/3
29/29 [==============================] - 115s 4s/step - loss: 0.0882
Epoch 3/3
29/29 [==============================] - 113s 4s/step - loss: 0.0671
```
