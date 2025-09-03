"""
4. Inverse Matrix
The inverse of a square matrix A is A^{-1} such that A * A^{-1} = I (identity).

Business Context: In economic input-output models (e.g., Leontief model), the inverse solves for production levels needed to meet demand. This helps stakeholders forecast resource allocation interpretably.
ML Context: In linear regression, the inverse is used in the normal equation ((X^T X)^{-1} X^T y) to find optimal coefficients, providing exact solutions for small datasets and clear coefficient interpretations.
"""

import numpy as np

# Business Scenario: Input-Output Economic Model
# Requirement matrix A: Rows/columns as sectors (e.g., agriculture, manufacturing).
A = np.array([[0.2, 0.1], [0.3, 0.4]])  # Input coefficients
I = np.eye(2)  # Identity
leontief_inv = np.linalg.inv(I - A)  # (I - A)^{-1}

demand = np.array([[100], [150]])  # Final demand
production = np.dot(leontief_inv, demand)  # Total production needed

print("Business: Inverse for Production Forecasting:")
print("Requirement Matrix A:\n", A)
print("Leontief Inverse (I - A)^{-1}:\n", leontief_inv)
print("Required Production for Demand:\n", production)
print("Interpretation: Stakeholders see exact output needs (e.g., sector totals), enabling precise planning.")

# ML Scenario: Linear Regression Normal Equation
# X: Features (3 samples x 2, with bias), y: Targets
X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([[6], [8], [10]])
X_tx_inv = np.linalg.inv(np.dot(X.T, X))  # (X^T X)^{-1}
coefficients = np.dot(np.dot(X_tx_inv, X.T), y)  # (X^T X)^{-1} X^T y

print("\nML: Inverse for Regression Coefficients:")
print("Feature Matrix X:\n", X)
print("Targets y:\n", y)
print("Coefficients (Intercept, Slope):\n", coefficients)
print("Interpretation: Exact coefficients make the model interpretable—e.g., slope shows feature impact, building stakeholder confidence.")