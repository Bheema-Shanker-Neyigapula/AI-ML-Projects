import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style using Seaborn
sns.set(style="whitegrid")

# Simulated performance values for ML-TPCPS and traditional methods
methods = ['ML-TPCPS', 'Rule-based IDS', 'Signature-based']
accuracy = [0.95, 0.75, 0.82]
false_positive_rate = [0.03, 0.18, 0.12]
false_negative_rate = [0.02, 0.07, 0.09]
response_time = [0.015, 0.045, 0.035]

# Create subplots for different metrics
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Comparative Assessment of ML-TPCPS vs. Traditional Methods', fontsize=16)

# Customize colors
colors = sns.color_palette("pastel")

# Accuracy
sns.barplot(x=methods, y=accuracy, ax=axes[0, 0], palette=colors)
axes[0, 0].set_title('Accuracy')
axes[0, 0].set_ylim(0, 1)
axes[0, 0].set_ylabel("")

# False Positive Rate
sns.barplot(x=methods, y=false_positive_rate, ax=axes[0, 1], palette=colors)
axes[0, 1].set_title('False Positive Rate')
axes[0, 1].set_ylim(0, 0.5)
axes[0, 1].set_ylabel("")

# False Negative Rate
sns.barplot(x=methods, y=false_negative_rate, ax=axes[1, 0], palette=colors)
axes[1, 0].set_title('False Negative Rate')
axes[1, 0].set_ylim(0, 0.5)

# Response Time
sns.barplot(x=methods, y=response_time, ax=axes[1, 1], palette=colors)
axes[1, 1].set_title('Response Time')
axes[1, 1].set_ylim(0, 0.05)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()
