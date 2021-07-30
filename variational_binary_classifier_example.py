import numpy as np
from sklearn.datasets import load_breast_cancer
import torch
from app import qnn
import pennylane as qml
import torch.nn.functional as F

torch.manual_seed(42)
np.random.seed(42)

#load dataset
data = load_breast_cancer()
X = data.data
y = data.target
y_hot = F.one_hot(torch.tensor(y).to(torch.int64))

classes = 2
qubit = 8
layers = 2
enc = 4 
pqc = 1 
meas = 3
qnn = qnn.PennylaneQNNCircuit(enc = enc, qubit = qubit, layers = layers, pqc = pqc, meas = meas)

input_length = qnn.enc_builder.max_inputs_length()
weight_shape = qnn.pqc_builder.weigths_shape()
dev = qml.device("default.qubit", wires = qubit) #target pennylane device
qnode = qml.QNode(qnn.construct_qnn_circuit, dev) #circuit
qlayer = qml.qnn.TorchLayer(qnode, {"weights": weight_shape})
clayer = torch.nn.Linear(qubit, classes)
softmax = torch.nn.Softmax(dim=1)

model = torch.nn.Sequential(qlayer, clayer, softmax)
opt = torch.optim.SGD(model.parameters(), lr=0.5)
loss = torch.nn.MSELoss()


X = torch.tensor(X, requires_grad=True).float()
y_hot = y_hot.float()

batch_size = 30
batches = len(y)/30

data_loader = torch.utils.data.DataLoader(
    list(zip(X, y_hot)), batch_size=batch_size, shuffle=True, drop_last=True
)

epochs = 10

for epoch in range(epochs):

    running_loss = 0

    for xs, ys in data_loader:
        opt.zero_grad()

        loss_evaluated = loss(model(xs), ys)
        loss_evaluated.backward()

        opt.step()

        running_loss += loss_evaluated

    avg_loss = running_loss / batches
    print("Average loss over epoch {}: {:.4f}".format(epoch + 1, avg_loss))

y_pred = model(X)
predictions = torch.argmax(y_pred, axis=1).detach().numpy()

correct = [1 if p == p_true else 0 for p, p_true in zip(predictions, y)]
accuracy = sum(correct) / len(correct)
print(f"Accuracy: {accuracy * 100}%")
