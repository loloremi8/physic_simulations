from qutip import Bloch, basis
import matplotlib.pyplot as plt

# Define spin states for each qubit
qubit_1 = basis(2, 0)  # |0⟩
qubit_2 = basis(2, 1)  # |1⟩
qubit_3 = (basis(2, 0) + basis(2, 1)).unit()  # Balanced superposition
qubit_4 = (basis(2, 0) - basis(2, 1)).unit()  # Anti-balanced superposition

# Initialise Bloch sphere
b = Bloch()

# Add states individually with custom colours
b.add_states(qubit_1)  # Qubit 1 (|0⟩)
b.point_color = ['r']  # Red

b.add_states(qubit_2)  # Qubit 2 (|1⟩)
b.point_color.append('g')  # Green

b.add_states(qubit_3)  # Qubit 3 (|0⟩ + |1⟩)/√2
b.point_color.append('b')  # Blue

b.add_states(qubit_4)  # Qubit 4 (|0⟩ - |1⟩)/√2
b.point_color.append('m')  # Magenta

# Draw the Bloch sphere
b.show()

# Prevent the graph from closing immediately
plt.show()