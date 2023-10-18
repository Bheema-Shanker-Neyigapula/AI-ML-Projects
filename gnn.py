import matplotlib.pyplot as plt

# Data for baseline models and comparison
models = ['ARIMA', 'Linear Regression', 'SVM', 'Random Forests', 'GNN', 'GCNs', 'GATs']
performance = [0.75, 0.82, 0.78, 0.85, 0.92, 0.88, 0.89]  # Placeholder performance scores

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(models, performance, color=['#1f77b4'] * 4 + ['#2ca02c'] * 3)  # Different colors for baseline and graph-based models

plt.xlabel('Models', fontsize=14)
plt.ylabel('Performance Score', fontsize=14)
plt.title('Comparison of Baseline and Graph-Based Traffic Prediction Models', fontsize=16)

plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Add annotations to the bars
for i, score in enumerate(performance):
    plt.text(i, score + 0.02, f'{score:.2f}', ha='center', fontsize=12, color='black')

# Adding a legend to differentiate baseline and graph-based models
plt.legend(['Baseline Models', 'Graph-Based Models'], fontsize=12)

plt.show()
