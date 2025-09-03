"""
2. Transpose Matrix
The transpose of a matrix swaps its rows and columns (A^T[i][j] = A[j][i]).

Business Context: In sales reporting, transposing a dataset (e.g., from customer-rows to feature-columns) simplifies analysis for stakeholders, such as computing correlations between sales metrics across regions. This aids in dashboard creation and interpretable visualizations.
ML Context: In linear regression or PCA, the transpose is used to compute the covariance matrix (e.g., X^T X), which reveals feature relationships. This helps stakeholders understand data multicollinearity, ensuring models are robust and interpretable.
"""

import numpy as np

# Business Scenario: Sales Data Reporting
# Sales data: Rows as customers, columns as products purchased.
sales_data = np.array([[10, 20, 15], [5, 25, 10], [15, 10, 20]])  # 3 customers x 3 products
transposed_sales = sales_data.T  # Transpose to products x customers for per-product analysis

print("Business: Transposed Sales Report:")
print("Original (Customers x Products):\n", sales_data)
print("Transposed (Products x Customers):\n", transposed_sales)
print("Interpretation: Stakeholders can now easily sum per product (e.g., total sales), improving report readability.")

# ML Scenario: Computing Covariance for Feature Analysis
# Customer features: Age, Income, Spending Score (3 samples x 3 features)
features = np.array([[25, 50000, 300], [35, 70000, 500], [45, 90000, 700]])
mean_features = np.mean(features, axis=0)  # Mean per feature
centered = features - mean_features  # Center data

# Covariance = (Centered^T * Centered) / (n-1)
covariance = np.dot(centered.T, centered) / (features.shape[0] - 1)
print("\nML: Covariance Matrix for Feature Relationships:")
print("Original Features:\n", features)
print("Centered Data:\n", centered)
print("Covariance Matrix:\n", covariance)
print("Interpretation: High off-diagonals indicate correlated features (e.g., age and income), helping stakeholders detect redundancies for better ML models.")