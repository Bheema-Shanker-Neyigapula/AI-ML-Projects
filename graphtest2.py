import matplotlib.pyplot as plt
import numpy as np

# Data for visualization techniques
techniques = ['Attention Maps', 'Feature Importance']
influence_scores = [0.7, 0.9]  # Placeholder influence scores for illustration purposes

# Create a bar plot for interpretability techniques and influence scores
x = np.arange(len(techniques))
width = 0.4

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(x, influence_scores, width, color=['#1f77b4', '#2ca02c'])

ax.set_xlabel('Interpretability Techniques', fontsize=14)
ax.set_ylabel('Influence Score', fontsize=14)
ax.set_title('Interpretability of GNNs: Attention Maps vs. Feature Importance', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(techniques, fontsize=12)

# Adding data labels on top of the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=12)

add_labels(bars)

plt.tight_layout()
plt.show()
