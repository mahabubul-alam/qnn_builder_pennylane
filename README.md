### QNN Builder (PennyLane)
You can build QNN models with various encoding methods, parametric layer architectures, and measurement operations using the python scripts in this repository. Supports for more encoding methods/parametric layers/measurements will be added in the future. For currently supported methods, please refer to:
* https://github.com/mahabubul-alam/qnn_builder_pennylane/blob/main/app/encoder/encoding_circuits.py
* https://github.com/mahabubul-alam/qnn_builder_pennylane/blob/main/app/pqc/parametric_circuits.py
* https://github.com/mahabubul-alam/qnn_builder_pennylane/blob/main/app/measurement/measurement_circuits.py

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

### Sample QNN Models

```
 0: ──H──RZ(0.987)──RX(0.338)──RZ(0.717)──╭C─────────╭RX(0.516)─────────────────────────┤ ⟨Z⟩ 
 1: ──H──RZ(0.966)──RX(0.814)──RZ(0.551)──│──────────╰C──────────╭RX(0.1)───────────────┤ ⟨Z⟩
 2: ──H──RZ(0.319)──RX(0.581)──RZ(0.042)──│──────────────────────╰C────────╭RX(0.0443)──┤ ⟨Z⟩
 3: ──H──RZ(0.313)──RX(0.319)──RZ(0.208)──╰RX(0.13)────────────────────────╰C───────────┤ ⟨Z⟩
```
