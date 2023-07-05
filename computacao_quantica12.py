from Neuraline.QuantumPhysics.quantum_computing import QuantumCircuit
from Neuraline.QuantumPhysics.quantum_computing import QUANTUM_COMPUTER

quantum_computing = QuantumCircuit(architecture=QUANTUM_COMPUTER)
quantum_computing.setQubits(nqubits=2)

x_training = [[1, 2], [10, 20], [3, 4], [30, 40]]
y_training = [[0], [1], [0], [1]]

for x in x_training: quantum_computing.addInputData(data=x)
for y in y_training: quantum_computing.addOutputData(data=y)

quantum_computing.addEncoderBarrierX()
quantum_computing.addDecoderBarrierY()

quantum_computing.showCircuit()

x_test = [[2, 3], [20, 30], [4, 5], [40, 50]]
y_test = []
for x in x_test:
    quantum_computing.measurement(repetitions=1024, data=x)
    y_test.append(quantum_computing.getResult())

from math import trunc
print(f'Predição: {[[trunc(y[0])] for y in y_test]}')
