from qutip import Bloch, Qobj
import numpy as np
import matplotlib.pyplot as plt

# Initial state of control and target qubits
initial_vector_control = [0, 0, 1]  # Control qubit |0>
initial_vector_target = [0, 0, 1]  # Target qubit |0>

# Final state (control: unchanged, target: flipped if control is |1>)
final_vector_control = [0, 0, 1]  # Control qubit remains |0>
final_vector_target = [1, 0, 0]  # Target qubit flips to (|0⟩ + |1⟩)/sqrt(2)

# Initialise Bloch spheres
b_control = Bloch()
b_target = Bloch()

# Add initial and final states to the control qubit's Bloch sphere
b_control.add_vectors(initial_vector_control)  # Red: initial
b_control.add_vectors(final_vector_control)  # Green: final
b_control.vector_color = ['r', 'g']

# Add initial and final states to the target qubit's Bloch sphere
b_target.add_vectors(initial_vector_target)  # Red: initial
b_target.add_vectors(final_vector_target)  # Green: final
b_target.vector_color = ['r', 'g']

# Display Bloch spheres
b_control.show()
b_target.show()
plt.show()