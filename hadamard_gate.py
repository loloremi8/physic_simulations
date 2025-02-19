from qutip import Bloch, Qobj
import numpy as np
import matplotlib.pyplot as plt

# Initial state (|0>)
initial_vector = [0, 0, 1]  # Bloch vector for |0⟩

# Final state after Hadamard (superposition: (|0⟩ + |1⟩)/sqrt(2))
final_vector = [1, 0, 0]  # Bloch vector for (|0⟩ + |1⟩)/sqrt(2)

# Initialise Bloch sphere
b = Bloch()

# Add initial and final states
b.add_vectors(initial_vector)  # Red: initial
b.add_vectors(final_vector)  # Green: final

# Set colours for vectors
b.vector_color = ['r', 'g']

# Display Bloch sphere
b.show()
plt.show()