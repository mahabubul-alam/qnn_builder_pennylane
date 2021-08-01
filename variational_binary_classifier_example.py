from sklearn.datasets import load_breast_cancer
import app.qnn_builder as qnn_builder
import pennylane as qml
import tensorflow as tf
from sklearn.preprocessing import normalize

#load tabular dataset
data = load_breast_cancer()
X = data.data
X = normalize(X, axis = 0, norm = 'max')
y = data.target
y_hot = tf.one_hot(y, depth = 2)
features = X.shape[-1]
classes = max(y) + 1

#build qnn model
qubit = 8
layers = 2
enc = 4 
pqc = 12
meas = 3
qnn = qnn_builder.PennylaneQNNCircuit(enc = enc, qubit = qubit, layers = layers, pqc = pqc, meas = meas)

#check compatibility between the chosen model and the dataset
input_length = qnn.enc_builder.max_inputs_length()
assert features <= input_length

#build the quantum-classical hybrid learning model
weight_shape = qnn.pqc_builder.weigths_shape()
if isinstance(weight_shape[0], tuple):
    ql_weights_shape = {'weights0': weight_shape[0], 'weights1': weight_shape[1]}
else:
    ql_weights_shape = {'weights0': weight_shape, 'weights1': ()}
dev = qml.device("default.qubit", wires = qubit) #target pennylane device
qnode = qml.QNode(qnn.construct_qnn_circuit, dev) #circuit
qlayer = qml.qnn.KerasLayer(qnode, ql_weights_shape, output_dim = qubit)
clayer = tf.keras.layers.Dense(classes, activation = 'softmax')
model = tf.keras.models.Sequential([qlayer, clayer])
opt = tf.keras.optimizers.SGD(learning_rate = 0.5)
model.compile(opt, loss = 'mse')

#train the model
model.fit(X, y_hot, epochs = 3, batch_size = 20)