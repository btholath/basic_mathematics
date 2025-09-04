"""
Dataset: Wine Quality 
Goal: Reduce dimensionality for visualization 
Matrix Insight: PCA decomposes feature matrix into orthogonal components



"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/workspaces/basic_mathematics/Matrix/matrix-based-ml-techqniues/winequality-red.csv", sep=";")
X = df.drop("quality", axis=1)
y = df["quality"]

# Standardize and apply PCA
X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plot PCA
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=y, palette="Spectral")
plt.title("PCA Projection of Wine Quality")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
plt.savefig("/workspaces/basic_mathematics/Matrix/matrix-based-ml-techqniues/winequality-red.png")