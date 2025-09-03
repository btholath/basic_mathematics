
"""
linear_regression_matrix_mult.py
--------------------------------
A minimal linear regression example that uses matrix multiplication
(dot products) end-to-end:
  1) Builds the design matrix X (with bias column of 1s)
  2) Solves for weights W using the Normal Equation
  3) Uses matrix multiplication (X @ W) to make predictions

Real-world tie-in: this is essentially what happens inside one layer
of a neural network or a regression model when transforming inputs.
"""
import numpy as np

def fit_linear_regression(hours, marks):
    """Fit y = W0 + W1 * x via Normal Equation.

    Args:
        hours (array-like): input feature (hours studied)
        marks (array-like): target values (marks)
    Returns:
        W (2x1 ndarray): [[intercept], [slope]]
    """
    x = np.asarray(hours).reshape(-1, 1)
    y = np.asarray(marks).reshape(-1, 1)

    # Design matrix with bias column
    X = np.hstack([np.ones((x.shape[0], 1)), x])
    # Normal Equation: W = (X^T X)^(-1) X^T y
    W = np.linalg.inv(X.T @ X) @ X.T @ y
    return W  # shape (2,1)

def predict(hours, W):
    """Make predictions using matrix multiplication: y_pred = X @ W."""
    x = np.asarray(hours).reshape(-1, 1)
    X = np.hstack([np.ones((x.shape[0], 1)), x])
    return X @ W

if __name__ == "__main__":
    # Example dataset (Hours vs Marks)
    hours = np.array([0, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9, 9], dtype=float)
    marks = np.array([40, 52, 53, 55, 56, 72, 71, 88, 56, 74, 89, 67, 89], dtype=float)

    W = fit_linear_regression(hours, marks)
    intercept, slope = W.ravel()
    print(f"Fitted model: marks = {intercept:.3f} + {slope:.3f} * hours")

    # Predict for new students
    new_hours = [2, 5, 7]
    preds = predict(new_hours, W)
    for h, p in zip(new_hours, preds.ravel()):
        print(f"Hours={h:>2} -> predicted marks = {p:.2f}")
