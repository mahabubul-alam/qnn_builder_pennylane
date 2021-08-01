import pennylane as qml

def add_dummy_gates_for_test(func):
    def inner(*args, **kwargs):
        if test == True:
            qml.Hadamard(wires = 0)
        return func(*args, **kwargs)
    return inner

class MeasurementCircuitsPennylane:
    def __init__(self, meas = None, qubit = None):
        self.choices = [1, 2, 3, 4, 5]
        assert meas in self.choices
        self.meas = meas
        self.qubit = qubit
    
    def get_meas(self):
        if self.meas == 1:
            return self.__measurement_1()
        if self.meas == 2:
            return self.__measurement_2()
        if self.meas == 3:
            return self.__measurement_3()
        if self.meas == 4:
            return self.__measurement_4()
        if self.meas == 5:
            return self.__measurement_5()
    
    def output_dim(self):
        if self.meas == 1:
            return self.qubit
        if self.meas == 2:
            return self.qubit
        if self.meas == 3:
            return self.qubit
        if self.meas == 4:
            return 1
        if self.meas == 5:
            return 2**self.qubit

    @add_dummy_gates_for_test
    def __measurement_1(self):
        return [qml.expval(qml.PauliX(i)) for i in range(self.qubit)]
    
    @add_dummy_gates_for_test
    def __measurement_2(self):
        return [qml.expval(qml.PauliY(i)) for i in range(self.qubit)]
    
    @add_dummy_gates_for_test
    def __measurement_3(self):
        return [qml.expval(qml.PauliZ(i)) for i in range(self.qubit)]
    
    @add_dummy_gates_for_test
    def __measurement_4(self):
        return qml.expval(qml.PauliZ(0))
    
    @add_dummy_gates_for_test
    def __measurement_5(self):
        return qml.probs(wires=range(self.qubit))

if __name__ == '__main__':
    test = True
    pqc = MeasurementCircuitsPennylane(meas = 3, qubit = 2)
    dev = qml.device("default.qubit", wires = 10) #target pennylane device
    qnode = qml.QNode(pqc.get_meas, dev) #circuit
    qnode()
    print(qnode.draw())
else:
    test = False
