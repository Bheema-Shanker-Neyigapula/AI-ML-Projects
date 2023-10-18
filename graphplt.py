import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score

# Generate some sample ground truth and predicted traffic data
ground_truth_traffic = np.array([100, 150, 200, 250, 300])
predicted_traffic = np.array([110, 140, 190, 260, 290])

# Calculate evaluation metrics
mae = mean_absolute_error(ground_truth_traffic, predicted_traffic)
rmse = np.sqrt(mean_squared_error(ground_truth_traffic, predicted_traffic))
mape = mean_absolute_percentage_error(ground_truth_traffic, predicted_traffic)
r2 = r2_score(ground_truth_traffic, predicted_traffic)

# Plot the evaluation metrics
metrics = ['MAE', 'RMSE', 'MAPE', 'R2']
values = [mae, rmse, mape, r2]

plt.figure(figsize=(10, 6))
plt.bar(metrics, values, color=['blue', 'green', 'orange', 'red'])
plt.xlabel('Metrics')
plt.ylabel('Value')
plt.title('Evaluation Metrics for GNN-based Traffic Prediction Model')
plt.show()
