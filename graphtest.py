import matplotlib.pyplot as plt

# Hyperparameters and their variations
hyperparameters = ['Learning Rate', 'Number of Layers', 'Dropout Rate']
variations = ['Low', 'Medium', 'High']
performance_scores = [
    [0.85, 0.88, 0.92],
    [0.80, 0.87, 0.89],
    [0.82, 0.85, 0.90]
]

# Create a grouped bar plot
width = 0.2
x = range(len(hyperparameters))

fig, ax = plt.subplots(figsize=(10, 6))

for i, var in enumerate(variations):
    ax.bar([pos + width * i for pos in x], performance_scores[i], width, label=var)

ax.set_xlabel('Hyperparameters', fontsize=14)
ax.set_ylabel('Performance Score', fontsize=14)
ax.set_title('Sensitivity Analysis: Impact of Hyperparameter Variations on GNN Model', fontsize=16)
ax.set_xticks([pos + width for pos in x])
ax.set_xticklabels(hyperparameters, fontsize=12)
ax.legend(title='Hyperparameter Variations', fontsize=12)

# Adding data labels on top of the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=12)

for i in range(len(variations)):
    add_labels(ax.patches[i::len(variations)])

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()
