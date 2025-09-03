
"""
economic_input_output_model.py
------------------------------
Simple Leontief input-output model:
  x = (I - A)^(-1) d
where
  A is the inter-industry technical coefficients matrix,
  d is final demand,
  x is total output required to satisfy d.

Real-world use: estimate ripple effects across industries when demand changes.
"""
import numpy as np

def leontief_total_output(A: np.ndarray, d: np.ndarray) -> np.ndarray:
    I = np.eye(A.shape[0])
    return np.linalg.inv(I - A) @ d

if __name__ == "__main__":
    # Example with 3 industries: Agriculture, Manufacturing, Services
    A = np.array([
        [0.10, 0.20, 0.10],  # inputs needed by Agriculture per $1 of output
        [0.05, 0.15, 0.10],  # Manufacturing
        [0.02, 0.10, 0.08],  # Services
    ], dtype=float)
    # Final demand vector (billions of $)
    d = np.array([[50.0],
                  [70.0],
                  [90.0]])

    x = leontief_total_output(A, d)
    print("Total output required (billions):")
    print(x.ravel())
