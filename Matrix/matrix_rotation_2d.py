
"""
matrix_rotation_2d.py
---------------------
Rotate a 2D point (x, y) by theta degrees using a rotation matrix.
Useful in graphics, gaming, and robotics for transforming coordinates.
"""
import numpy as np
import math

def rotation_matrix_2d(theta_degrees: float) -> np.ndarray:
    theta = math.radians(theta_degrees)
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[c, -s],
                     [s,  c]], dtype=float)

def rotate_point(point_xy, theta_degrees):
    p = np.asarray(point_xy, dtype=float).reshape(2, 1)
    R = rotation_matrix_2d(theta_degrees)
    return (R @ p).ravel()

if __name__ == "__main__":
    point = (2, 3)
    for deg in [30, 90, 180]:
        rp = rotate_point(point, deg)
        print(f"Rotate {point} by {deg:>3}° -> ({rp[0]:.3f}, {rp[1]:.3f})")
