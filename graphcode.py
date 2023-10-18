import matplotlib.pyplot as plt
import numpy as np

# Models and evaluation metrics
models = ['GNN', 'Baseline']
metrics = ['MAE', 'RMSE', 'MAPE', 'R2']

# Placeholder performance scores for illustration purposes
gnn_scores = [3.5, 5.2, 8.1, 0.75]
baseline_scores = [5.8, 7.3, 10.2, 0.60]

# Create a grouped bar plot
width = 0.4
x = np.arange(len(metrics))

fig, ax = plt.subplots(figsize=(10, 6))

gnn_bars = ax.bar(x - width/2, gnn_scores, width, label='GNN', color='#1f77b4')
baseline_bars = ax.bar(x + width/2, baseline_scores, width, label='Baseline', color='#2ca02c')

ax.set_xlabel('Metrics', fontsize=14)
ax.set_ylabel('Value', fontsize=14)
ax.set_title('Comparative Study: GNN-based Traffic Prediction vs. Baseline Models', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=12)
ax.legend(fontsize=12)

# Adding data labels on top of the bars with a slight rotation for better alignment
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=12, rotation=45, color='black')

add_labels(gnn_bars)
add_labels(baseline_bars)

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()
