from Neuraline.QuantumPhysics.quantum_computing import CircuitSimulator # importação da classe
quantum_computing = CircuitSimulator() # instanciação do objeto da classe importada

result = quantum_computing.runQuantumCircuit( # execução da simulação física
    nqubits=3, # número de qubits na vertical
    nmoments=10 # número de momentuns na horizontal
)
print(result) # exibição do resultado booleano de retorno