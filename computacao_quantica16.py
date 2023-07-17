from Neuraline.QuantumPhysics.quantum_computing import QuantumCircuit
from Neuraline.QuantumPhysics.quantum_computing import QUANTUM_COMPUTER

quantum_computing  = QuantumCircuit(architecture=QUANTUM_COMPUTER)
quantum_computing.setQubits(nqubits=2)

x_training = [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400], [2, 3, 4, 5], [20, 30, 40, 50], [200, 300, 400, 500]]

for x in x_training: quantum_computing.addInputData(data=x)

quantum_computing.addEncoderBarrierX()
quantum_computing.addQuantumTunnelingBarrier()
quantum_computing.addQuantumTunnelingBarrier()
quantum_computing.addDecoderBarrierY()

quantum_computing.showCircuit()

quantum_computing.measurement(repetitions=1024)
groups = quantum_computing.getResult()

for i, cluster in enumerate(groups): print(f'cluster {i+1}: {cluster}')
