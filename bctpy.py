import matplotlib.pyplot as plt
import numpy as np

# Metrics for comparison
metrics = ['Data Privacy', 'Model Accuracy', 'Computational Efficiency', 'Security', 'Scalability']
diln_scores = [0.85, 0.92, 0.78, 0.88, 0.85]  # Placeholder scores for DILN framework
centralized_scores = [0.70, 0.85, 0.65, 0.70, 0.75]  # Placeholder scores for centralized approach
blockchain_scores = [0.75, 0.80, 0.70, 0.90, 0.65]  # Placeholder scores for blockchain solution

# Number of metrics
num_metrics = len(metrics)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Set the width of the bars
bar_width = 0.2

# Create index for each metric group
index = np.arange(num_metrics)

# Plot the bars for each framework
bars1 = ax.bar(index, diln_scores, bar_width, label='DILN Framework', alpha=0.8)
bars2 = ax.bar(index + bar_width, centralized_scores, bar_width, label='Centralized Approach', alpha=0.8)
bars3 = ax.bar(index + 2 * bar_width, blockchain_scores, bar_width, label='Blockchain Solution', alpha=0.8)

# Add some space between the groups of bars
ax.set_xticks(index + bar_width)

# Set labels for each metric
ax.set_xticklabels(metrics, fontsize=12, rotation=45, ha='right')

# Add y-axis label
ax.set_ylabel('Normalized Score', fontsize=14)

# Set title and legend
ax.set_title('Comparative Analysis: DILN Framework vs. Centralized Approach vs. Blockchain Solution', fontsize=16)
ax.legend(loc='upper right', fontsize=12)

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()
