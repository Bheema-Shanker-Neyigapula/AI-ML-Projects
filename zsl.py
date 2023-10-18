import matplotlib.pyplot as plt
import numpy as np

# Sample baseline method accuracies
baseline_methods = ['Baseline Method 1', 'Baseline Method 2', 'Baseline Method 3']
baseline_accuracies = [0.85, 0.68, 0.78]

# Sample ZSL method accuracy
zsl_method = 'ZSL Method'
zsl_accuracy = 0.92

# Plotting
methods = baseline_methods + [zsl_method]
accuracies = baseline_accuracies + [zsl_accuracy]

# Set up colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

plt.figure(figsize=(10, 6))
bars = plt.bar(methods, accuracies, color=colors)

# Adding data labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, round(yval, 2), ha='center', va='bottom', fontsize=10)

plt.xlabel('Methods')
plt.ylabel('Accuracy')
plt.title('Comparison of Baseline Methods with ZSL Method')
plt.ylim(0, 1.0)
plt.xticks(rotation=45, ha='right')



# Adjust layout
plt.tight_layout()

plt.show()
