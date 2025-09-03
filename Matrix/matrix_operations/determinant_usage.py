"""
Scenario: Checking invertibility of a feature matrix before regression or PCA.
Why it matters: Determinants help diagnose multicollinearity and ensure model stability in linear systems.
"""
import numpy as np

# Feature matrix (2x2)
features = np.array([
    [4, 7],
    [2, 6]
])

# Compute determinant
det = np.linalg.det(features)

print("Feature Matrix:\n", features)
print("Determinant:", det)

if det == 0:
    print("Matrix is singular — not suitable for inversion or PCA.")
else:
    print("Matrix is invertible — safe for regression or PCA.")
