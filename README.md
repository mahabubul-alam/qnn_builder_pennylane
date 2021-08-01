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

 0: ──H──RZ(0.49)───RX(0.896)──RZ(0.69)───┤ ⟨Z⟩ 
 1: ──H──RZ(0.298)──RX(0.774)──RZ(0.703)──┤ ⟨Z⟩
 2: ──H──RZ(0.328)──RX(0.956)──RZ(0.458)──┤ ⟨Z⟩
 3: ──H──RZ(0.877)──RX(0.44)───RZ(0.278)──┤ ⟨Z⟩
 
 0: ──H──RZ(0.547)───RX(0.338)──RZ(0.103)──RX(0.646)───RZ(0.174)──╭C──────────╭C──────────────────────╭RZ(0.0547)──╭RZ(0.399)───RX(0.736)──RZ(0.721)─────────────┤ ⟨Z⟩ 
 1: ──H──RZ(0.0768)──RX(0.356)──RZ(0.931)──RX(0.26)────RZ(0.552)──╰RZ(0.178)──│───────────╭C──────────╰C───────────│───────────╭RZ(0.576)──RX(0.499)──RZ(0.592)──┤ ⟨Z⟩
 2: ──H──RZ(0.177)───RX(0.542)──RZ(0.52)───RX(0.0842)──RZ(0.665)──────────────╰RZ(0.489)──╰RZ(0.359)───────────────╰C──────────╰C──────────RX(0.245)──RZ(0.772)──┤ ⟨Z⟩
 
 0: ──RY(0.737)──RY(0.762)───╭C──────────╭RX(0.316)───RY(0.18)───────────────╭C─────────────────────╭RX(0.844)──────────────────────────────────────╭┤ Probs 
 1: ──RY(0.649)──RY(0.178)───│───────────╰C──────────╭RX(0.645)───RY(0.36)───╰RX(0.148)─────────────│───────────────────────────────────╭C──────────├┤ Probs
 2: ──RY(0.871)──RY(0.0344)──│───────────────────────╰C──────────╭RX(0.318)───RY(0.216)─────────────│───────────────────────╭C──────────╰RX(0.263)──├┤ Probs
 3: ──RY(0.317)──RY(0.455)───│───────────────────────────────────╰C──────────╭RX(0.551)──RY(0.939)──│───────────╭C──────────╰RX(0.561)──────────────├┤ Probs
 4: ──RY(0.272)──RY(0.762)───╰RX(0.277)──────────────────────────────────────╰C──────────RY(0.363)──╰C──────────╰RX(0.228)──────────────────────────╰┤ Probs

```
