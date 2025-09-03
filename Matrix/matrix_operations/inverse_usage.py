"""
Scenario: Solving a system of equations for resource allocation or operational planning.
Why it matters: Inverse matrices are used to solve linear systems, optimize resource distribution, and back-calculate inputs from outputs.
"""
import numpy as np

# Coefficient matrix representing constraints
A = np.array([
    [2, 1],
    [1, 3]
])

# Outcome vector (e.g., required resources)
b = np.array([8, 13])

# Solve Ax = b → x = A⁻¹b
A_inv = np.linalg.inv(A)
solution = A_inv @ b

print("Coefficient Matrix A:\n", A)
print("Inverse of A:\n", A_inv)
print("Solution x (resource allocation):", solution)
