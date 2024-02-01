#%% Import libraries
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from oracle import Oracle

#%% Task 1: Given a quantum circuit simulating Uf for a function f with one input,
#    generate the quantum circuit for Pf
def generate_Pf(n: int, circuit: QuantumCircuit) -> QuantumCircuit:
    # TODO
    pass

#%% Task 2: Implement the Deutsch-Jozsa algorithm 
#   for functions having single qubit as input
# Return the quantum circuit implementing the algorithm
def DeutschJozsa1(oracle: Oracle) -> QuantumCircuit:
    # TODO
    pass

#%% Task 3: Similar to the above case, implement the Deutsch-Jozsa algorithm
#   for functions with 7 bits as input
# Return the quantum circuit implementing the algorithm
def DeutschJozsa7(oracle: Oracle) -> QuantumCircuit:
    # TODO
    pass

#%% Main callback
if __name__ == "__main__":
    # Sample of how the test cases will be run
    
    # Test for 1-bit input function
    oracle = Oracle(1)
    oracle.set_Pf(generate_Pf)
    circuit = DeutschJozsa1(oracle)
    res = oracle.verify(circuit)
    print("Verification", res)

    # Test for 7-bits input function
    oracle = Oracle(7)
    oracle.set_Pf(generate_Pf)
    circuit = DeutschJozsa7(oracle)
    res = oracle.verify(circuit)
    print("Verification", res)

