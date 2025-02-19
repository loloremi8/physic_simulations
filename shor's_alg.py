import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# Function to calculate modular exponentiation results
def modular_exponentiation_table(N, g, max_exponent):
    """Generate modular exponentiation table up to a given exponent."""
    table = []
    for x in range(1, max_exponent + 1):  # Loop through exponents up to max_exponent
        result = g**x
        remainder = result % N
        table.append((x, result, result // N, remainder))
    return table

# Function to render the table
def render_table(N, a, max_exponent):
    """Render modular exponentiation table separately with dynamic column widths."""
    table = modular_exponentiation_table(N, g, max_exponent)
    
    # Create figure for the table
    fig, ax_table = plt.subplots(figsize=(8, 10))  # Initial figure size
    ax_table.axis('off')  # Turn off the axis

    col_labels = [r"$g^x$", "Result", r"$g^x / N$", "Remainder"]
    cell_text = [[f"${row[0]}$", row[1], row[2], row[3]] for row in table]
    
    # Calculate the maximum text width in each column
    col_widths = [
        max(len(str(item)) for item in [col_label] + [row[idx] for row in table]) * 0.15
        for idx, col_label in enumerate(col_labels)
    ]
    
    # Adjust the figure size dynamically based on column widths
    total_width = sum(col_widths) + 1  # Add padding for better appearance
    fig.set_size_inches(total_width, 10)

    # Create the table
    table_plot = ax_table.table(
        cellText=cell_text, 
        colLabels=col_labels, 
        loc='center', 
        cellLoc='center',
        colWidths=[width / total_width for width in col_widths]  # Normalize column widths
    )
    
    # Adjust font size and scale
    table_plot.auto_set_font_size(False)
    table_plot.set_fontsize(10)
    table_plot.scale(1.1, 1.3)  # Scale slightly for better readability
    
    # Title and layout adjustments
    plt.title(f"Modular Exponentiation Table for $N = {N}, g = {g}, x = 1$ to $x = {max_exponent}$", fontsize=12)
    plt.tight_layout()
    plt.show()

# Function to render the period bar graph
def render_graph(N, g, max_exponent):
    """Render modular exponentiation period graph separately."""
    table = modular_exponentiation_table(N, g, max_exponent)
    x_vals = [row[0] for row in table]  # Exponents
    remainders = [row[3] for row in table]  # Remainders

    # Create figure for the bar graph
    fig, ax_graph = plt.subplots(figsize=(8, 4))
    bar_colors = plt.cm.viridis(np.array(remainders) / N)  # Color based on normalized remainder
    ax_graph.bar(x_vals, remainders, color=bar_colors)
    
    # Set labels and title
    ax_graph.set_xticks(x_vals)
    ax_graph.set_xlabel("Exponent (x)", fontsize=12)
    ax_graph.set_ylabel("Remainder (mod N)", fontsize=12)
    ax_graph.set_title(f"Period Graph: $N = {N}, g = {g}, up _ to _ x = {max_exponent}$", fontsize=14)
    
    # Show the bar graph
    plt.tight_layout()
    plt.show()

# Main logic
if __name__ == "__main__":
    print("Modular Exponentiation Visualiser")
    N = int(input("Enter the value of N (modulus): "))
    g = int(input("Enter the value of g (base): "))
    max_exponent = int(input("Enter the maximum value of x (exponent): "))
    
    # Render the table and graph separately
    render_table(N, g, max_exponent)
    render_graph(N, g, max_exponent)