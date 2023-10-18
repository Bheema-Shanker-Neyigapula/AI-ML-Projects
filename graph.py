import matplotlib.pyplot as plt

# Sample data
categories = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
scores = [0.85, 0.78, 0.92, 0.82]

# Create a bar plot
plt.bar(categories, scores, color=['blue', 'green', 'orange', 'red'])
plt.ylim(0, 1)  # Set y-axis limits between 0 and 1

# Add labels and title
plt.xlabel('Metrics')
plt.ylabel('Score')
plt.title('Performance Metrics')

# Show the plot
plt.show()
