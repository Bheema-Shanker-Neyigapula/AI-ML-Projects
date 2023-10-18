import numpy as np
import matplotlib.pyplot as plt

# Sample evaluation metric values
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']
values = [0.85, 0.78, 0.92, 0.84, 0.91]  # Replace with your actual metric values

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(metrics, values, color='skyblue')
plt.title('ML-TPCPS Evaluation Metrics')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.ylim(0, 1)  # Set y-axis limit
plt.show()
