"""
Scenario: Resetting feature weights in a recommender system or ML model.
Why it matters: Identity matrices are used to preserve structure during transformations or to initialize models without bias.
"""
import numpy as np

# Simulated feature weights for 3 marketing channels
weights = np.array([[0.6, 0.3, 0.1]])

# Identity matrix to preserve original weights
identity = np.eye(3)

# Applying identity transformation
transformed = weights @ identity

print("Original Weights:", weights)
print("After Identity Transformation:", transformed)
