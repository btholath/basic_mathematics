
# Matrix Applications (Dot Product & Multiplication)

Professional, runnable Python scripts that demonstrate real-world uses of
matrix multiplication and dot products across domains.

## Contents
- `linear_regression_matrix_mult.py` — Fit/predict with Normal Equation; uses `X @ W`.
- `matrix_rotation_2d.py` — Rotate 2D points using a rotation matrix.
- `economic_input_output_model.py` — Leontief input-output total output calculation.
- `recommender_matrix_factorization.py` — SVD-based low-rank reconstruction for recommendations.
- `robotics_coordinate_transform.py` — 2D homogeneous transform (rotation + translation).
- `matrix_utils.py` — Tiny helper for pretty-printing matrices.

## Quickstart
```bash
python linear_regression_matrix_mult.py
python matrix_rotation_2d.py
python economic_input_output_model.py
python recommender_matrix_factorization.py
python robotics_coordinate_transform.py
```

## Requirements
- Python 3.9+
- NumPy
```bash
pip install numpy
```

## Notes
- Scripts avoid external dependencies besides NumPy.
- Each script has a `__main__` block showing a realistic, minimal example.
