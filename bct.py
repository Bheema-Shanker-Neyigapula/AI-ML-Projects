import matplotlib.pyplot as plt

# Metrics and their scores
metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'AUC-ROC', 'Transaction Throughput', 'Confirmation Time', 'Consensus Efficiency']
scores = [0.85, 0.90, 0.82, 0.87, 0.92, 1200, 5, 0.95]  # Placeholder scores for illustration purposes

# Create a bar plot with enhanced aesthetics
x = range(len(metrics))

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(x, scores, color=['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd', '#17becf', '#8c564b', '#e377c2'])

ax.set_xlabel('Metrics', fontsize=14)
ax.set_ylabel('Score', fontsize=14)
ax.set_title('Performance Assessment of Integrated System', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=12, rotation=45, ha='right')

# Adding data labels with percentage formatting on top of the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=12)

add_labels(bars)

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()
