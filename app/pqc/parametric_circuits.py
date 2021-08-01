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
        self.choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        assert pqc in self.choices
        self.pqc = pqc
        self.qubit = qubit
        self.layers = layers
    
    def get_pqc(self, weights0, weights1):
        if self.pqc == 1:
            return self.__pqc_1(weights0)
        if self.pqc == 2:
            return self.__pqc_2(weights0)
        if self.pqc == 3:
            return self.__pqc_3(weights0, weights1)
        if self.pqc == 4:
            return self.__pqc_4(weights0, weights1)
        if self.pqc == 5:
            return self.__pqc_5(weights0, weights1)
        if self.pqc == 6:
            return self.__pqc_6(weights0, weights1)
        if self.pqc == 7:
            return self.__pqc_7(weights0, weights1)
        if self.pqc == 8:
            return self.__pqc_8(weights0, weights1)
        if self.pqc == 9:
            return self.__pqc_9(weights0)
        if self.pqc == 10:
            return self.__pqc_10(weights0)
        if self.pqc == 11:
            return self.__pqc_11(weights0, weights1)
        if self.pqc == 12:
            return self.__pqc_12(weights0, weights1)
        if self.pqc == 13:
            return self.__pqc_13(weights0, weights1)
        if self.pqc == 14:
            return self.__pqc_14(weights0, weights1)
        if self.pqc == 15:
            return self.__pqc_15(weights0)
        if self.pqc == 16:
            return self.__pqc_16(weights0, weights1)
        if self.pqc == 17:
            return self.__pqc_17(weights0, weights1)
        if self.pqc == 18:
            return self.__pqc_18(weights0)
        if self.pqc == 19:
            return self.__pqc_19(weights0)



    def weigths_shape(self):
        if self.pqc == 1:
            return (self.layers, self.qubit, 2)
        if self.pqc == 2:
            return (self.layers, self.qubit, 2)
        if self.pqc == 3:
            return ((self.layers, self.qubit, 2), (self.layers, self.qubit - 1))
        if self.pqc == 4:
            return ((self.layers, self.qubit, 2), (self.layers, self.qubit - 1))
        if self.pqc == 5:
            return ((self.layers, self.qubit, 4), (self.layers, self.qubit, self.qubit - 1))
        if self.pqc == 6:
            return ((self.layers, self.qubit, 4), (self.layers, self.qubit, self.qubit - 1))
        if self.pqc == 7:
            return ((self.layers, self.qubit, 4), (self.layers, self.qubit - 1))
        if self.pqc == 8:
            return ((self.layers, self.qubit, 4), (self.layers, self.qubit - 1))
        if self.pqc == 9:
            return (self.layers, self.qubit)
        if self.pqc == 10:
            return (self.layers, self.qubit, 2)
        if self.pqc == 11:
            assert self.qubit > 1
            return ((self.layers, self.qubit, 2), (self.layers, (self.qubit - 1) if self.qubit % 2 == 1 else self.qubit - 2, 4))
        if self.pqc == 12:
            assert self.qubit > 1
            return ((self.layers, self.qubit, 2), (self.layers, (self.qubit - 1) if self.qubit % 2 == 1 else self.qubit - 2, 4))
        if self.pqc == 13:
            return ((self.layers, self.qubit, 2), (self.layers, self.qubit, 2))
        if self.pqc == 14:
            return ((self.layers, self.qubit, 2), (self.layers, self.qubit, 2))
        if self.pqc == 15:
            return (self.layers, self.qubit, 2)
        if self.pqc == 16:
            return ((self.layers, self.qubit, 2), (self.layers, self.qubit - 1))
        if self.pqc == 17:
            return ((self.layers, self.qubit, 2), (self.layers, self.qubit - 1))
        if self.pqc == 18:
            return (self.layers, self.qubit, 3)
        if self.pqc == 19:
            return (self.layers, self.qubit, 3)


    @add_dummy_measurements_for_test
    def __pqc_1(self, weights):
        assert weights.shape == self.weigths_shape()
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights[l, i, 0], wires = i)
                qml.RZ(weights[l, i, 1], wires = i)
    
    @add_dummy_measurements_for_test
    def __pqc_2(self, weights):
        assert weights.shape == self.weigths_shape()
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights[l, i, 0], wires = i)
                qml.RZ(weights[l, i, 1], wires = i)
            for i in range(self.qubit - 1):
                qml.CNOT(wires=[i, (i + 1)])

    @add_dummy_measurements_for_test
    def __pqc_3(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 0], wires = i)
                qml.RZ(weights0[l, i, 1], wires = i)
            for i in range(self.qubit - 1):
                qml.CRZ(weights1[l, i], wires = [i, (i + 1)])
    
    @add_dummy_measurements_for_test
    def __pqc_4(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 0], wires = i)
                qml.RZ(weights0[l, i, 1], wires = i)
            for i in range(self.qubit - 1):
                qml.CRX(weights1[l, i], wires = [i, (i + 1)])

    @add_dummy_measurements_for_test
    def __pqc_5(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 0], wires = i)
                qml.RZ(weights0[l, i, 1], wires = i)
            for i in range(self.qubit):
                for j in range(self.qubit - 1):
                    qml.CRZ(weights1[l, i, j], wires = [i, (i + j + 1)%self.qubit])            
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 2], wires = i)
                qml.RZ(weights0[l, i, 3], wires = i)
    
    @add_dummy_measurements_for_test
    def __pqc_6(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 0], wires = i)
                qml.RZ(weights0[l, i, 1], wires = i)
            for i in range(self.qubit):
                for j in range(self.qubit - 1):
                    qml.CRX(weights1[l, i, j], wires = [i, (i + j + 1)%self.qubit])            
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 2], wires = i)
                qml.RZ(weights0[l, i, 3], wires = i)
    
    @add_dummy_measurements_for_test
    def __pqc_7(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 0], wires = i)
                qml.RZ(weights0[l, i, 1], wires = i)
            j = 0
            for i in range(0, self.qubit - 1, 2):
                qml.CRZ(weights1[l, j], wires = [i, (i+1)])
                j += 1             
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 2], wires = i)
                qml.RZ(weights0[l, i, 3], wires = i)
            for i in range(1, self.qubit - 1, 2):
                qml.CRZ(weights1[l, j], wires = [i, (i+1)])
                j += 1
    
    @add_dummy_measurements_for_test
    def __pqc_8(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 0], wires = i)
                qml.RZ(weights0[l, i, 1], wires = i)
            j = 0
            for i in range(0, self.qubit - 1, 2):
                qml.CRX(weights1[l, j], wires = [i, (i+1)])
                j += 1             
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 2], wires = i)
                qml.RZ(weights0[l, i, 3], wires = i)
            for i in range(1, self.qubit - 1, 2):
                qml.CRX(weights1[l, j], wires = [i, (i+1)])
                j += 1
    
    @add_dummy_measurements_for_test
    def __pqc_9(self, weights):
        assert weights.shape == self.weigths_shape()
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.Hadamard(wires = i)
            for i in range(self.qubit - 1):
                qml.CZ(wires=[i, (i + 1)])
            for i in range(self.qubit):
                qml.RX(weights[l, i], wires = i)
    
    @add_dummy_measurements_for_test
    def __pqc_10(self, weights):
        assert weights.shape == self.weigths_shape()
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RY(weights[l, i, 0], wires = i)
            for i in range(self.qubit):
                qml.CZ(wires=[i, (i + 1)%self.qubit])
            for i in range(self.qubit):
                qml.RY(weights[l, i, 1], wires = i)
    
    @add_dummy_measurements_for_test
    def __pqc_11(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RY(weights0[l, i, 0], wires = i)
                qml.RZ(weights0[l, i, 1], wires = i)
            for i in range(0, self.qubit - 1, 2):
                qml.CNOT(wires=[i, (i + 1)])
            for j, i in enumerate(range(1, self.qubit - 1, 2)):
                qml.RY(weights1[l, j, 0], wires = i)
                qml.RZ(weights1[l, j, 1], wires = i)
                qml.RY(weights1[l, j, 2], wires = i+1)
                qml.RZ(weights1[l, j, 3], wires = i+1)
            for i in range(1, self.qubit - 1, 2):
                qml.CNOT(wires=[i, (i + 1)])
    
    @add_dummy_measurements_for_test
    def __pqc_12(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RY(weights0[l, i, 0], wires = i)
                qml.RZ(weights0[l, i, 1], wires = i)
            for i in range(0, self.qubit - 1, 2):
                qml.CZ(wires=[i, (i + 1)])
            for j, i in enumerate(range(1, self.qubit - 1, 2)):
                qml.RY(weights1[l, j, 0], wires = i)
                qml.RZ(weights1[l, j, 1], wires = i)
                qml.RY(weights1[l, j, 2], wires = i+1)
                qml.RZ(weights1[l, j, 3], wires = i+1)
            for i in range(1, self.qubit - 1, 2):
                qml.CZ(wires=[i, (i + 1)])
    
    @add_dummy_measurements_for_test
    def __pqc_13(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RY(weights0[l, i, 0], wires = i)
            for i in range(0, self.qubit):
                qml.CRZ(weights1[l, i, 0], wires = [i, (i + self.qubit - 1) % self.qubit])
            for i in range(self.qubit):
                qml.RY(weights0[l, i, 1], wires = i)
            temp = list(range(self.qubit))[1:]
            temp.reverse()
            temp.insert(0,0)
            controls = temp.copy()
            temp = list(range(self.qubit))[2:]
            temp.reverse()
            temp.insert(0, 0)
            temp.insert(0, 1)
            targets = temp.copy()
            for i, control in enumerate(controls):
                qml.CRZ(weights1[l, i, 1], wires = [control, targets[i]])
    
    @add_dummy_measurements_for_test
    def __pqc_14(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RY(weights0[l, i, 0], wires = i)
            for i in range(0, self.qubit):
                qml.CRX(weights1[l, i, 0], wires = [i, (i + self.qubit - 1) % self.qubit])
            for i in range(self.qubit):
                qml.RY(weights0[l, i, 1], wires = i)
            temp = list(range(self.qubit))[1:]
            temp.reverse()
            temp.insert(0,0)
            controls = temp.copy()
            temp = list(range(self.qubit))[2:]
            temp.reverse()
            temp.insert(0, 0)
            temp.insert(0, 1)
            targets = temp.copy()
            for i, control in enumerate(controls):
                qml.CRX(weights1[l, i, 1], wires = [control, targets[i]])
    
    @add_dummy_measurements_for_test
    def __pqc_15(self, weights):
        assert weights.shape == self.weigths_shape()
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RY(weights[l, i, 0], wires = i)
            for i in range(0, self.qubit):
                qml.CNOT(wires = [i, (i + self.qubit - 1) % self.qubit])
            for i in range(self.qubit):
                qml.RY(weights[l, i, 1], wires = i)
            temp = list(range(self.qubit))[1:]
            temp.reverse()
            temp.insert(0,0)
            controls = temp.copy()
            temp = list(range(self.qubit))[2:]
            temp.reverse()
            temp.insert(0, 0)
            temp.insert(0, 1)
            targets = temp.copy()
            for i, control in enumerate(controls):
                qml.CNOT(wires = [control, targets[i]])
    
    @add_dummy_measurements_for_test
    def __pqc_16(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 0], wires = i)
                qml.RZ(weights0[l, i, 1], wires = i)
            for i in range(0, self.qubit - 1, 2):
                qml.CRZ(weights1[l, i], wires = [i, (i + 1)])
            for i in range(1, self.qubit - 1, 2):
                qml.CRZ(weights1[l, i], wires = [i, (i + 1)])
    
    @add_dummy_measurements_for_test
    def __pqc_17(self, weights0, weights1):
        assert weights0.shape == self.weigths_shape()[0]
        assert weights1.shape == self.weigths_shape()[1]
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights0[l, i, 0], wires = i)
                qml.RZ(weights0[l, i, 1], wires = i)
            for i in range(0, self.qubit - 1, 2):
                qml.CRX(weights1[l, i], wires = [i, (i + 1)])
            for i in range(1, self.qubit - 1, 2):
                qml.CRX(weights1[l, i], wires = [i, (i + 1)])

    @add_dummy_measurements_for_test
    def __pqc_18(self, weights):
        assert weights.shape == self.weigths_shape()
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights[l, i, 0], wires = i)
                qml.RZ(weights[l, i, 1], wires = i)
            for i in range(0, self.qubit):
                qml.CRZ(weights[l, i, 2], wires = [i, (i + self.qubit - 1) % self.qubit])
    
    @add_dummy_measurements_for_test
    def __pqc_19(self, weights):
        assert weights.shape == self.weigths_shape()
        for l in range(self.layers):
            for i in range(self.qubit):
                qml.RX(weights[l, i, 0], wires = i)
                qml.RZ(weights[l, i, 1], wires = i)
            for i in range(0, self.qubit):
                qml.CRX(weights[l, i, 2], wires = [i, (i + self.qubit - 1) % self.qubit])    

if __name__ == '__main__':
    test = True
    pqc = ParametricCircuitsPennylane(pqc = 19, qubit = 7, layers = 1)
    dev = qml.device("default.qubit", wires = 10) #target pennylane device
    qnode = qml.QNode(pqc.get_pqc, dev) #circuit
    weight_shape = pqc.weigths_shape()
    if isinstance(weight_shape[0], tuple):
        weights0 = np.random.random(weight_shape[0])
        weights1 = np.random.random(weight_shape[1])
        qnode(weights0, weights1)
    else:
        weights = np.random.random(weight_shape)
        qnode(weights)
    print(qnode.draw())
else:
    test = False
