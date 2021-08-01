import pennylane as qml
import numpy as np

if __name__ != '__main__':
    from . encoder.encoding_circuits import EncodingCircuitsPennylane
    from . pqc.parametric_circuits import ParametricCircuitsPennylane
    from . measurement.measurement_circuits import MeasurementCircuitsPennylane

class PennylaneQNNCircuit:
    def __init__(self, enc = 1, pqc = 1, meas = 1, layers = 1, qubit = 1):
        '''
        initialize variables
        '''
        self.enc = enc
        self.pqc = pqc
        self.meas = meas
        self.qubit = qubit
        self.layers = layers
        self.pqc_builder = ParametricCircuitsPennylane(pqc = self.pqc, qubit = self.qubit, layers = self.layers)
        self.enc_builder = EncodingCircuitsPennylane(enc = self.enc, qubit = self.qubit)
        self.meas_builder = MeasurementCircuitsPennylane(meas = self.meas, qubit = self.qubit)


    def construct_qnn_circuit(self, inputs, weights0, weights1 = 0):
        assert len(inputs) <= self.enc_builder.max_inputs_length()
        pqc_weights_shape = self.pqc_builder.weigths_shape()
        if isinstance(pqc_weights_shape[0], tuple):
            assert weights0.shape == pqc_weights_shape[0]
            assert weights1.shape == pqc_weights_shape[1]
        else:
            assert weights0.shape == pqc_weights_shape
        self.enc_builder.get_encoder(inputs)
        self.pqc_builder.get_pqc(weights0, weights1 = weights1)
        return self.meas_builder.get_meas()


if __name__ == '__main__':
    from encoder.encoding_circuits import EncodingCircuitsPennylane
    from pqc.parametric_circuits import ParametricCircuitsPennylane
    from measurement.measurement_circuits import MeasurementCircuitsPennylane

    qnn = PennylaneQNNCircuit(enc = 5, qubit = 5, layers = 2, pqc = 19, meas = 3)
    input_length = qnn.enc_builder.max_inputs_length()
    weight_shape = qnn.pqc_builder.weigths_shape()
    inputs = np.random.random(input_length)
    dev = qml.device("default.qubit", wires = 10) #target pennylane device
    qnode = qml.QNode(qnn.construct_qnn_circuit, dev) #circuit
    if isinstance(weight_shape[0], tuple):
        weights0 = np.random.random(weight_shape[0])
        weights1 = np.random.random(weight_shape[1])
        qnode(inputs, weights0, weights1)
    else:
        weights = np.random.random(weight_shape)
        qnode(inputs, weights)
    print(qnode.draw())
