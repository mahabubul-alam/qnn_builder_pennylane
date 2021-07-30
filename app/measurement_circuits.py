import pennylane as qml
import numpy as np


class MeasurementCircuitsPennylane:
    def __init__(self, meas = None, qubit = None, test = False):
        self.choices = [1, 2, 3, 4]
        assert meas in self.choices
        self.meas = meas
        self.qubit = qubit
        self.test = test
    
    def get_meas(self):
        if self.meas == 1:
            return self.__measurement_1()
        if self.meas == 2:
            return self.__measurement_2()
        if self.meas == 3:
            return self.__measurement_3()
        if self.meas == 4:
            return self.__measurement_4()
    
    @staticmethod
    def add_dummy_gate():
        qml.Hadamard(wires = 0)
    
    def __measurement_1(self):
        if self.test:
            self.add_dummy_gate()
        return [qml.expval(qml.PauliX(i)) for i in range(self.qubit)]
    
    def __measurement_2(self):
        if self.test:
            self.add_dummy_gate()
        return [qml.expval(qml.PauliY(i)) for i in range(self.qubit)]
    
    def __measurement_3(self):
        if self.test:
            self.add_dummy_gate()
        return [qml.expval(qml.PauliZ(i)) for i in range(self.qubit)]
    
    def __measurement_4(self):
        if self.test:
            self.add_dummy_gate()
        return qml.expval(qml.PauliZ(0))
        
if __name__ == '__main__':
    pqc = MeasurementCircuitsPennylane(meas = 3, qubit = 2, test = True)
    dev = qml.device("default.qubit", wires = 10) #target pennylane device
    qnode = qml.QNode(pqc.get_meas, dev) #circuit
    qnode()
    print(qnode.draw())
