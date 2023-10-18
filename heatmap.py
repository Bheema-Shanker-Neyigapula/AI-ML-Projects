import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample text data
text_data = ["The news is credible.", "This news is not credible.", "Unsure about the credibility of this news."]

# Sample attention weights (fake values)
attention_weights = np.array([[0.2, 0.3, 0.5],
                              [0.4, 0.1, 0.5],
                              [0.3, 0.4, 0.3]])

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(attention_weights, annot=True, cmap="YlGnBu", xticklabels=text_data, yticklabels=["Sample 1", "Sample 2", "Sample 3"])
plt.title("Attention Heatmap")
plt.xlabel("Textual Regions")
plt.ylabel("Samples")
plt.show()
