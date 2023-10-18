import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Sample performance metrics for Logistic Regression and DeepCredNet
methods = ['Logistic Regression', 'DeepCredNet']
accuracy = [0.85, 0.92]
precision = [0.78, 0.85]
recall = [0.92, 0.89]
f1_score = [0.82, 0.88]

# Create a DataFrame for the data
import pandas as pd
data = pd.DataFrame({'Method': methods, 'Accuracy': accuracy, 'Precision': precision, 'Recall': recall, 'F1-Score': f1_score})

# Set the style
sns.set(style="whitegrid")
sns.set_palette("Set2")

# Create subplots for each metric
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Accuracy
sns.barplot(x='Method', y='Accuracy', data=data, ax=axs[0, 0])
axs[0, 0].set_title('Accuracy')

# Precision
sns.barplot(x='Method', y='Precision', data=data, ax=axs[0, 1])
axs[0, 1].set_title('Precision')

# Recall
sns.barplot(x='Method', y='Recall', data=data, ax=axs[1, 0])
axs[1, 0].set_title('Recall')

# F1-Score
sns.barplot(x='Method', y='F1-Score', data=data, ax=axs[1, 1])
axs[1, 1].set_title('F1-Score')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
