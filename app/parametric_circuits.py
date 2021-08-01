import pennylane as qml
import numpy as np

def add_dummy_measurements_for_test(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        if test == True:
            return qml.expval(qml.PauliY(0))
    return inner

class ParametricCircuitsPennylane:
    def __init__(self, pqc = None, qubit = None, layers = None):
        self.choices = [1, 2]
        assert pqc in self.choices
        self.pqc = pqc
        self.qubit = qubit
        self.layers = layers
    
    def get_pqc(self, weights):
        if self.pqc == 1:
            return self.__pqc_1(weights)   
        if self.pqc == 2:
            return self.__pqc_2(weights)

    def weigths_shape(self):
        if self.pqc == 1:
            return (self.layers, self.qubit)
        if self.pqc == 2:
            return (self.layers, self.qubit)
    
    @add_dummy_measurements_for_test
    def __pqc_1(self, weights):
        assert weights.shape == self.weigths_shape()
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.CNOT(wires=[i, (i + 1) %self.qubit])
            for j in range(self.qubit):
                qml.RY(weights[l, j], wires = j % self.qubit)
    
    @add_dummy_measurements_for_test
    def __pqc_2(self, weights):
        assert weights.shape == self.find_weights_shape()
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.CZ(wires=[i, (i + 1) %self.qubit])
            for j in range(self.qubit):
                qml.RY(weights[l, j], wires = j % self.qubit)

if __name__ == '__main__':
    test = True
    pqc = ParametricCircuitsPennylane(pqc = 1, qubit = 2, layers = 3)
    weight_shape = pqc.weigths_shape()
    weights = np.random.random(weight_shape)
    dev = qml.device("default.qubit", wires = 10) #target pennylane device
    qnode = qml.QNode(pqc.get_pqc, dev) #circuit
    qnode(weights)
    print(qnode.draw())
else:
    test = False
