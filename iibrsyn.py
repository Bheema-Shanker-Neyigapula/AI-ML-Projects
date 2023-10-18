import matplotlib.pyplot as plt

# Scenarios and their time measurements (in milliseconds)
scenarios = ['View Synthesis', 'Scene Rendering']
time_measurements = [120, 80]  # Placeholder time measurements for illustration purposes

# Create a line plot for time measurements
x = range(len(scenarios))

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, time_measurements, marker='o', linestyle='-', color='tab:blue', linewidth=2)

ax.set_xlabel('Scenarios', fontsize=14)
ax.set_ylabel('Time (ms)', fontsize=14)
ax.set_title('Computational Efficiency and Real-Time Performance of iIBR Framework', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(scenarios, fontsize=12)
ax.set_ylim(0, max(time_measurements) * 1.2)  # Set y-axis limits

# Adding data labels on top of the data points
def add_labels(points):
    for point in points:
        ax.annotate(f'{point} ms',
                    xy=(point, 0),  # Position of the label
                    xytext=(0, 10),  # 10 points vertical offset
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=12)

add_labels(time_measurements)

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()
