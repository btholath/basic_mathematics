
"""
robotics_coordinate_transform.py
--------------------------------
Demonstrates 2D homogeneous coordinate transforms for robotics/navigation.
We build a transform that rotates then translates local points into a global frame.
"""
import numpy as np
import math

def homogeneous_transform(theta_deg: float, tx: float, ty: float) -> np.ndarray:
    """Return 3x3 homogeneous transform for rotation (theta) and translation (tx, ty)."""
    th = math.radians(theta_deg)
    c, s = math.cos(th), math.sin(th)
    T = np.array([
        [ c, -s, tx],
        [ s,  c, ty],
        [ 0,  0,  1],
    ], dtype=float)
    return T

def transform_points(points_xy: np.ndarray, T: np.ndarray) -> np.ndarray:
    """Transform Nx2 points with homogeneous transform T."""
    N = points_xy.shape[0]
    homo = np.hstack([points_xy, np.ones((N, 1))])  # Nx3
    out = (T @ homo.T).T  # Nx3
    return out[:, :2]

if __name__ == "__main__":
    # Local LIDAR detections in robot frame
    points = np.array([[1.0, 0.0],
                       [1.0, 1.0],
                       [2.0, 0.5]])

    # Robot pose in global frame: rotate 45°, translate (2, 3)
    T = homogeneous_transform(theta_deg=45, tx=2.0, ty=3.0)
    global_points = transform_points(points, T)

    print("Global coordinates:")
    for p_local, p_global in zip(points, global_points):
        print(f"  {p_local} -> {p_global}")
