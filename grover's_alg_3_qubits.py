from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import MCXGate
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Define the Oracle
def grover_oracle(circuit, marked_state):
    """
    Oracle flips the phase of the marked state.
    - `marked_state`: integer representing the state to mark (e.g., 5 for |101⟩)
    """
    n_qubits = circuit.num_qubits
    binary_state = format(marked_state, f'0{n_qubits}b')
    
    # Apply X gates to qubits where the marked state has '0'
    for i, bit in enumerate(binary_state[::-1]):
        if bit == '0':
            circuit.x(i)
    
    # Multi-controlled Z (equivalent to flipping the marked state's phase)
    mcx = MCXGate(n_qubits - 1)  # Create multi-controlled-X gate
    circuit.append(mcx, list(range(n_qubits)))  # Apply to all qubits
    
    # Undo X gates
    for i, bit in enumerate(binary_state[::-1]):
        if bit == '0':
            circuit.x(i)

# Define the Diffusion Operator
def grover_diffusion(circuit):
    """
    Diffusion operator amplifies the marked state's amplitude.
    """
    n_qubits = circuit.num_qubits
    circuit.h(range(n_qubits))
    circuit.x(range(n_qubits))
    mcx = MCXGate(n_qubits - 1)  # Multi-controlled-X gate for diffusion
    circuit.append(mcx, list(range(n_qubits)))
    circuit.x(range(n_qubits))
    circuit.h(range(n_qubits))

# Create a Grover's Algorithm Circuit
n_qubits = 3
marked_state = 5  # Example: Marking state |101⟩

# Create the circuit
grover_circuit = QuantumCircuit(n_qubits)

# Step 1: Initialise the superposition
grover_circuit.h(range(n_qubits))

# Step 2: Apply the Oracle and Diffusion Operator
grover_oracle(grover_circuit, marked_state)
grover_diffusion(grover_circuit)

# Step 3: Measure all qubits
grover_circuit.measure_all()

# Visualise the Circuit
print("Grover's Algorithm Circuit:")
grover_circuit.draw(output='mpl')
plt.show()

# Simulate the Circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(grover_circuit, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()

# Get the Results
counts = result.get_counts()
print("Measurement Results:", counts)

# Plot the Histogram
plot_histogram(counts)
plt.show()