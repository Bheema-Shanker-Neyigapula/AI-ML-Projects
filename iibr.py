import matplotlib.pyplot as plt

# Metrics and their scores
metrics = ['PSNR', 'SSIM', 'MSE', 'Abs. Relative Error', 'RMSE']
scores = [32.5, 0.92, 0.011, 0.07, 0.15]  # Placeholder scores for illustration purposes

# Create a bar plot with enhanced aesthetics
x = range(len(metrics))

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(x, scores, color=['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd'])

ax.set_xlabel('Metrics', fontsize=14)
ax.set_ylabel('Score', fontsize=14)
ax.set_title('Effectiveness Assessment of iIBR Framework', fontsize=16)
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

# Adding a subtle background grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()
