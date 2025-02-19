from qutip import Bloch, basis
import matplotlib.pyplot as plt

# Define spin states
spin_up = basis(2, 0)  # |0⟩
spin_down = basis(2, 1)  # |1⟩

# Create superposition
alpha = 1 / (2 ** 0.5)
beta = 1 / (2 ** 0.5)
psi = alpha * spin_up + beta * spin_down

# Visualise on the Bloch Sphere
b = Bloch()
b.add_states(psi)
b.show()

# Prevent the graph from closing immediately
plt.show()