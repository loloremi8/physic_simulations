from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy

# Function to add QFT gates to a quantum circuit
def qft(circuit, n):
    """Apply QFT on the first n qubits in the circuit."""
    for qubit in range(n):
        circuit.h(qubit)
        for other_qubit in range(qubit + 1, n):
            angle = 2 * numpy.pi / (2 ** (other_qubit - qubit + 1))
            circuit.cp(angle, other_qubit, qubit)
    # Reverse qubit order for conventional QFT output
    for i in range(n // 2):
        circuit.swap(i, n - i - 1)
    return circuit

# Create a quantum circuit with 3 qubits
n_qubits = 3
qc = QuantumCircuit(n_qubits)

# Initialise the state (e.g., |001>)
qc.x(0)  # Set the least significant bit to 1

# Apply the QFT
qft(qc, n_qubits)

# Add measurement gates
qc.measure_all()

# Visualise the circuit
print("Quantum Fourier Transform Circuit:")
qc.draw(output='mpl')
plt.show()

# Simulate the QFT circuit
simulator = AerSimulator()
qc_transpiled = transpile(qc, simulator)  # Transpile circuit for the simulator
result = simulator.run(qc_transpiled, shots=1024).result()

# Get and plot the output
counts = result.get_counts(qc)
plot_histogram(counts)
plt.show()