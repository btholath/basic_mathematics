
"""
matrix_utils.py
---------------
Small helpers for displaying matrices and basic checks.
"""
import numpy as np

def pretty(M: np.ndarray, precision: int = 3) -> str:
    return np.array2string(M, precision=precision, suppress_small=True)
