# Script to generate a balanced or constant function for the Deutsch-Josza algorithm
# For M1 devices, if you had a problem installing qiskit, try the following:
# 		pip install tweedledum==1.0.0 qiskit --compile --no-cache-dir

#%% Import libraries
from qiskit import QuantumCircuit
from qiskit import execute, Aer
import numpy as np

#%% Class for Quantum Oracle generating balanced or constant functions
class Oracle:
	def __init__(self, n: int):
		self.__n = n
		self.__Pf_counter = 0
		self.__constant = np.random.randint(2)
		self.__output = np.random.randint(2)
		self.__subset = np.random.randint(1, 2**self.__n)
		self.__uf = self.__Uf()
		self.__pf = None
	
	# Given a quantum circuit as input, the function appends the oracle Pf circuit to it
	def append_Pf_to(self, circuit: QuantumCircuit):
		self.__Pf_counter += 1
		if self.__pf == None:
			raise Exception("Pf circuit not set")
		try:
			circuit.compose(self.__pf, inplace = True)
		except:
			raise Exception("The input circuit should have n + 1 qubits")

	# Function to verify whether the oracle is balanced/constant:
	def verify(self, circuit: QuantumCircuit):
		if self.__Pf_counter > 1:
			raise Exception("Oracle used more than once")
		if circuit.num_qubits != self.__n + 1:
			raise Exception("The input circuit should have n + 1 qubits")
	
		measurement_circuit = QuantumCircuit(self.__n + 1, self.__n)
		measurement_circuit.compose(circuit, inplace = True)
		for i in range(self.__n):
			measurement_circuit.measure(i, i)
		simulator = Aer.get_backend('qasm_simulator')
		num_runs = 1
		job = execute(measurement_circuit, simulator, shots = num_runs)
		result = job.result()
		answer = result.get_counts()
		if '0'*self.__n in answer.keys() and answer['0'*self.__n] == num_runs and self.__constant == 1:
			return True
		if '0'*self.__n not in answer.keys() and self.__constant == 0:
			return True
		return False
	
	# Function to define the Pf equivalent of the Uf circuit
	def set_Pf(self, generate_Pf):
		try:
			self.__pf = generate_Pf(self.__n, self.__uf)
		except:
			raise Exception("There is an error with Pf circuit generation")

	
	# Function to create a quantum oracle circuit for balanced/constant functions
	def __Uf(self):
		function = QuantumCircuit(self.__n + 1)

		# Case for constant function
		if self.__constant:
			if self.__output:
				function.x(self.__n)

		# Case for balanced function
		else:
			# Add CNOT gates from each input bit to output register
			for i in range(self.__n):
				if self.__subset & (1 << i):
					function.cx(i, self.__n)
		return function
	
