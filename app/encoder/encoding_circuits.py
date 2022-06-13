import pennylane as qml
import numpy as np

def add_dummy_measurements_for_test(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        if test == True:
            return qml.expval(qml.PauliY(0))
    return inner

class EncodingCircuitsPennylane:
    def __init__(self, enc = None, qubit = None):
        self.choices = [1, 2, 3, 4, 5, 6]
        assert enc in self.choices
        self.enc = enc
        self.qubit = qubit
    
    def get_encoder(self, inputs):
        if self.enc == 1:
            return self.__encoder_1(inputs)   
        if self.enc == 2:
            return self.__encoder_2(inputs)
        if self.enc == 3:
            return self.__encoder_3(inputs)
        if self.enc == 4:
            return self.__encoder_4(inputs)
        if self.enc == 5:
            return self.__encoder_5(inputs)
        if self.enc == 6:
            return self.__encoder_6(inputs)

    def max_inputs_length(self):
        if self.enc == 1:
            return self.qubit 
        if self.enc == 2:
            return self.qubit * 2
        if self.enc == 3:
            return self.qubit * 3
        if self.enc == 4:
            return self.qubit * 4
        if self.enc == 5:
            return self.qubit
        if self.enc == 6:
            return self.qubit * 8
    
    @add_dummy_measurements_for_test
    def __encoder_1(self, inputs):
        assert len(inputs) <= self.max_inputs_length()
        encoding_gates = ['RZ']
        for qub in range(self.qubit):
            qml.Hadamard(wires = qub)
            if qub < len(inputs):
                exec(f'qml.{encoding_gates[0]}({inputs[qub]}, wires = {qub})')

    @add_dummy_measurements_for_test
    def __encoder_2(self, inputs):
        assert len(inputs) <= self.max_inputs_length()
        encoding_gates = ['RZ', 'RX']
        var_per_qubit = 2
        for qub in range(self.qubit):
            qml.Hadamard(wires = qub)
            for i in range(var_per_qubit):
                if (qub * var_per_qubit + i) < len(inputs):
                    exec(
                        f'qml.{encoding_gates[i]}({inputs[qub * var_per_qubit + i]}, wires = {qub})'
                    )

    @add_dummy_measurements_for_test
    def __encoder_3(self, inputs):
        assert len(inputs) <= self.max_inputs_length()
        encoding_gates = ['RZ', 'RX', 'RZ']
        var_per_qubit = 3
        for qub in range(self.qubit):
            qml.Hadamard(wires = qub)
            for i in range(var_per_qubit):
                if (qub * var_per_qubit + i) < len(inputs):
                    exec(
                        f'qml.{encoding_gates[i]}({inputs[qub * var_per_qubit + i]}, wires = {qub})'
                    )
    
    @add_dummy_measurements_for_test
    def __encoder_4(self, inputs):
        assert len(inputs) <= self.max_inputs_length()
        encoding_gates = ['RZ', 'RX', 'RZ', 'RX']
        var_per_qubit = 4
        for qub in range(self.qubit):
            qml.Hadamard(wires = qub)
            for i in range(var_per_qubit):
                if (qub * var_per_qubit + i) < len(inputs):
                    exec(
                        f'qml.{encoding_gates[i]}({inputs[qub * var_per_qubit + i]}, wires = {qub})'
                    )
    
    @add_dummy_measurements_for_test
    def __encoder_5(self, inputs):
        assert len(inputs) <= self.max_inputs_length()
        encoding_gates = ['RY']
        for qub in range(self.qubit):
            if qub < len(inputs):
                exec(f'qml.{encoding_gates[0]}({inputs[qub]}, wires = {qub})')
    
    @add_dummy_measurements_for_test
    def __encoder_6(self, inputs):
        assert len(inputs) <= self.max_inputs_length()
        encoding_gates = ['RZ', 'RX', 'RZ', 'RX', 'RZ', 'RX', 'RZ', 'RX']
        var_per_qubit = 8
        for qub in range(self.qubit):
            qml.Hadamard(wires = qub)
            for i in range(var_per_qubit):
                if (qub * var_per_qubit + i) < len(inputs):
                    exec(
                        f'qml.{encoding_gates[i]}({inputs[qub * var_per_qubit + i]}, wires = {qub})'
                    )

if __name__ == '__main__':
    test = True
    enc = EncodingCircuitsPennylane(enc = 4, qubit = 5)
    inputs_length = enc.max_inputs_length()
    inputs = np.random.random(inputs_length)
    dev = qml.device("default.qubit", wires = 10) #target pennylane device
    qnode = qml.QNode(enc.get_encoder, dev) #circuit
    qnode(inputs)
    print(qnode.draw())
else:
    test = False
