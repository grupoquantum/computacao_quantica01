from Neuraline.QuantumPhysics.quantum_computing import QuantumCircuit
from Neuraline.QuantumPhysics.quantum_computing import QUANTUM_COMPUTER
from os import system

while True:
    quantum_computing = QuantumCircuit(architecture=QUANTUM_COMPUTER)
    quantum_computing.setQubits(nqubits=1)

    system('clear') # para windows use system('cls')
    print('############### CALCULADORA QUÂNTICA ###############')
    print('Digite + para somar.')
    print('Digite - para subtrair.')
    print('Digite * para multiplicar.')
    print('Digite / para dividir.')
    print('Digite x para sair.')
    print('####################################################')

    option = input('Digite a sua opção e tecle enter: ').strip()
    if option in ['+', '-', '*', '/']:
        number1 = float(input('Digite o número 1 e tecle enter: '))
        number2 = float(input('Digite o número 2 e tecle enter: '))

        quantum_computing.addUnitaryGate(value=number1)

        if option == '+': quantum_computing.addSumBarrier()
        elif option == '-': quantum_computing.addSubtractionBarrier()
        elif option == '*': quantum_computing.addMultiplicationBarrier()
        elif option == '/': quantum_computing.addDivisionBarrier()

        quantum_computing.addUnitaryGate(value=number2)
        
        quantum_computing.measurement()
        result = quantum_computing.getResult()

        print(f'RESULTADO: {number1} {option} {number2} = {result}')
        print('####################################################')
        input('tecle enter para continuar...')
    else: break
print('####################################################')
print('(programa encerrado com sucesso)')
