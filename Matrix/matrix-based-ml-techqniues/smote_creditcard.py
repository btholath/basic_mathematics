"""
Dataset: Credit Card Fraud Detection Goal: Balance imbalanced fraud data using SMOTE Matrix Insight: SMOTE interpolates minority class vectors in feature space
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
"""
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/workspaces/basic_mathematics/Matrix/matrix-based-ml-techqniues/creditcard.csv")
X = df.drop("Class", axis=1)
y = df["Class"]

# Apply SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Plot class distribution
sns.countplot(x=y_resampled, palette="Set2")
plt.title("Resampled Class Distribution (SMOTE)")
plt.show()
plt.savefig("/workspaces/basic_mathematics/Matrix/matrix-based-ml-techqniues/creditcard.png")


#------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE

# Create imbalanced dataset
X, y = make_classification(n_classes=2, weights=[0.9, 0.1], n_features=2, n_informative=2, n_redundant=0, random_state=42)

# Apply SMOTE
smote = SMOTE(k_neighbors=3, random_state=42)
X_res, y_res = smote.fit_resample(X, y)

# Separate original and synthetic samples
original_minority = X[y == 1]
synthetic_samples = X_res[len(X):][y_res[len(X):] == 1]

# Plot
plt.figure(figsize=(8,6))
plt.scatter(X[y == 0][:,0], X[y == 0][:,1], label="Majority", alpha=0.5)
plt.scatter(original_minority[:,0], original_minority[:,1], label="Minority", color='blue')
plt.scatter(synthetic_samples[:,0], synthetic_samples[:,1], label="Synthetic", color='green', marker='*')

# Optional: draw interpolation lines
for i in range(len(synthetic_samples)):
    # Randomly pair with original for illustration
    orig = original_minority[i % len(original_minority)]
    synth = synthetic_samples[i]
    plt.plot([orig[0], synth[0]], [orig[1], synth[1]], 'k--', alpha=0.3)

plt.title("SMOTE: Synthetic Sample Generation via Vector Interpolation")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("/workspaces/basic_mathematics/Matrix/matrix-based-ml-techqniues/creditcard_02.png")
