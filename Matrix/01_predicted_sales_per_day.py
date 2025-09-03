import numpy as np

# Features: [TV, Radio, Social Media] ad spend in $1000s
X = np.array([
    [10, 5, 2],   # Day 1
    [8, 7, 3],    # Day 2
    [12, 4, 1]    # Day 3
])

# Weights: effectiveness of each channel
W = np.array([1.5, 2.0, 0.5])  # Sales per $1000 spent

# Predicted sales
predicted_sales = np.dot(X, W)

print("Predicted Sales (in $1000s):", predicted_sales)