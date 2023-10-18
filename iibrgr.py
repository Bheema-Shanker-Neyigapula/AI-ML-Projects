import matplotlib.pyplot as plt

# Methods and their scores
methods = ['iIBR', 'Plane Sweeping', 'Depth Image-Based Rendering (DIBR)']
completeness_scores = [0.85, 0.72, 0.78]  # Placeholder completeness scores for illustration purposes
quality_scores = [0.92, 0.78, 0.80]  # Placeholder quality scores for illustration purposes
accuracy_scores = [0.89, 0.72, 0.76]  # Placeholder accuracy scores for illustration purposes

# Create a line plot with enhanced aesthetics and bottom-right legends
x = range(len(methods))

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Methods', fontsize=14)
ax1.set_ylabel('Completeness Score', color=color, fontsize=14)
line1 = ax1.plot(x, completeness_scores, color=color, marker='o', label='Completeness Score', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0, 1)  # Set y-axis limits for completeness score

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:green'
ax2.set_ylabel('Quality and Accuracy Scores', color=color, fontsize=14)
line2 = ax2.plot(x, quality_scores, color=color, marker='s', label='Quality Score', linewidth=2)
line3 = ax2.plot(x, accuracy_scores, color=color, linestyle='dashed', marker='x', label='Accuracy Score', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0, 1)  # Set y-axis limits for quality and accuracy scores

# Set legends to be outside the axes and aligned in the bottom right corner
lines = line1 + line2 + line3
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='lower right', fontsize=12, frameon=False)

# Set x-axis labels and title
plt.xticks(x, methods, fontsize=12, rotation=20, ha='right')
plt.title('Comparative Analysis: iIBR Framework vs. Existing IBR Methods', fontsize=16)

# Adding grid lines for better readability
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax2.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()
