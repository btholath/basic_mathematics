"""
3. Determinant
The determinant is a scalar value computed from a square matrix, indicating properties like volume scaling or invertibility (det=0 means singular).

Business Context: In financial risk management, the determinant of a covariance matrix for asset returns assesses portfolio diversity. A near-zero determinant signals high correlation (redundancy), alerting stakeholders to potential risks like overexposure.
ML Context: In regression models, the determinant of X^T X checks for multicollinearity; if zero, the matrix is singular, and the model can't be inverted, prompting feature selection for interpretable, stable predictions.
"""
import numpy as np

# Business Scenario: Portfolio Risk Assessment
# Covariance matrix of 3 asset returns (synthetic).
cov_matrix = np.array([[0.04, 0.02, 0.01], [0.02, 0.03, 0.015], [0.01, 0.015, 0.02]])
det_cov = np.linalg.det(cov_matrix)

print("Business: Determinant for Portfolio Diversity:")
print("Covariance Matrix:\n", cov_matrix)
print("Determinant:", det_cov)
if abs(det_cov) < 1e-5:
    print("Interpretation: Near-zero det indicates high asset correlation—stakeholders should diversify to reduce risk.")
else:
    print("Interpretation: Positive det suggests good diversity, aiding confident investment decisions.")

# ML Scenario: Checking Multicollinearity in Regression
# Feature matrix X (3 samples x 2 features, with near-collinear features).
X = np.array([[1, 2], [2, 4.1], [3, 5.9]])  # Almost collinear (feature2 ≈ 2*feature1)
X_tx = np.dot(X.T, X)
det_xtx = np.linalg.det(X_tx)

print("\nML: Determinant for Model Stability:")
print("Feature Matrix X:\n", X)
print("X^T X:\n", X_tx)
print("Determinant of X^T X:", det_xtx)
if abs(det_xtx) < 1e-5:
    print("Interpretation: Singular matrix (det≈0) means multicollinearity—stakeholders need to remove redundant features for reliable predictions.")
else:
    print("Interpretation: Invertible matrix ensures stable model, enhancing trust in ML outputs.")