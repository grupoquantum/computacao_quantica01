from Neuraline.QuantumPhysics.quantum_computing import QuantumCircuit
from Neuraline.QuantumPhysics.quantum_computing import QUANTUM_COMPUTER

quantum_computing  = QuantumCircuit(architecture=QUANTUM_COMPUTER)
quantum_computing.setQubits(nqubits=2)

x_training = [[1, 2], [3, 4], [5, 6], [7, 8]]
y_training = [[3, 30], [7, 70], [11, 110], [15, 150]]

for x in x_training: quantum_computing.addInputData(data=x)
for y in y_training: quantum_computing.addOutputData(data=y)

quantum_computing.addEncoderBarrierX()
quantum_computing.addDecoderBarrierY()

quantum_computing.showCircuit()

x_test = [[2, 3], [4, 5]]
y_test = []
for x in x_test:
    quantum_computing.measurement(repetitions=1024, data=x)
    y_test.append(quantum_computing.getResult())

print(f'Predição: {[[round(y[0]), round(y[1])] for y in y_test]}')
