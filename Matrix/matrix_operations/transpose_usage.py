"""
Scenario: Preparing customer data for similarity analysis (e.g., churn modeling or segmentation).
Why it matters: Transpose is essential for computing similarity scores, correlations, and aligning dimensions in ML pipelines.
"""
import numpy as np

# Customer feature matrix: rows = customers, cols = features
customer_data = np.array([
    [1, 0, 1],  # Customer A
    [0, 1, 1],  # Customer B
    [1, 1, 0]   # Customer C
])

# Transpose to align features for dot product similarity
transposed = customer_data.T

print("Original Matrix:\n", customer_data)
print("Transposed Matrix:\n", transposed)

