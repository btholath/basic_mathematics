
"""
recommender_matrix_factorization.py
-----------------------------------
Demonstrates matrix multiplication in a recommender workflow:
1) Take a small user-item ratings matrix R
2) Compute a low-rank approximation via truncated SVD
3) Use reconstructed scores to recommend top items for a user

This mirrors real systems where user and item latent factor matrices
are multiplied to produce preference scores.
"""
import numpy as np

def svd_top_k(R: np.ndarray, k: int = 2):
    U, s, Vt = np.linalg.svd(R, full_matrices=False)
    S = np.diag(s[:k])
    U_k = U[:, :k]
    Vt_k = Vt[:k, :]
    return U_k, S, Vt_k

def recommend_for_user(R: np.ndarray, user_index: int, top_n: int = 3):
    U_k, S, Vt_k = svd_top_k(R, k=min(2, min(R.shape)))
    R_hat = U_k @ S @ Vt_k  # reconstructed score matrix
    user_scores = R_hat[user_index]

    # Exclude items already rated (non-zero entries)
    already = R[user_index] != 0
    scores = np.where(already, -np.inf, user_scores)  # mask
    top_items = np.argsort(scores)[::-1][:top_n]
    return top_items, user_scores[top_items]

if __name__ == "__main__":
    # Rows = users, Cols = items
    # 0 means "not rated yet"
    R = np.array([
        [5, 4, 0, 1],
        [4, 0, 0, 1],
        [1, 1, 0, 5],
        [0, 0, 5, 4],
    ], dtype=float)

    user_idx = 0
    items, scores = recommend_for_user(R, user_idx, top_n=2)
    print(f"Top recommendations for user {user_idx}:")
    for it, sc in zip(items, scores):
        print(f"  Item {it} with predicted score {sc:.3f}")
