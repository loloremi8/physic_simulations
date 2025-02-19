from qutip import Bloch, Qobj
import numpy as np
import matplotlib.pyplot as plt

# Initial state of control and target qubits
initial_vector_control_1 = [0, 0, 1]  # Control qubit 1: |0>
initial_vector_control_2 = [0, 0, 1]  # Control qubit 2: |0>
initial_vector_target = [0, 0, 1]  # Target qubit: |0>

# Final state (target qubit flips to |1> if both controls are |1>)
final_vector_control_1 = [0, 0, 1]  # Control qubit 1 remains |0>
final_vector_control_2 = [0, 0, 1]  # Control qubit 2 remains |0>
final_vector_target = [0, 0, -1]  # Target qubit flips to |1>

# Initialise Bloch spheres
b_control_1 = Bloch()
b_control_2 = Bloch()
b_target = Bloch()

# Add initial and final states to each qubit's Bloch sphere
b_control_1.add_vectors(initial_vector_control_1)
b_control_1.add_vectors(final_vector_control_1)
b_control_1.vector_color = ['r', 'g']

b_control_2.add_vectors(initial_vector_control_2)
b_control_2.add_vectors(final_vector_control_2)
b_control_2.vector_color = ['r', 'g']

b_target.add_vectors(initial_vector_target)
b_target.add_vectors(final_vector_target)
b_target.vector_color = ['r', 'g']

# Display Bloch spheres
b_control_1.show()
b_control_2.show()
b_target.show()
plt.show()