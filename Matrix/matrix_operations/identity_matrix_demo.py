"""
. Identity Matrix
The identity matrix is a square matrix with 1s on the diagonal and 0s elsewhere. It acts like the number 1 in multiplication, leaving other matrices unchanged when multiplied.

Business Context: In supply chain management, an identity matrix can represent a "no-transformation" scenario, such as direct passthrough of inventory levels without adjustments. This is useful for baseline forecasting or auditing systems where stakeholders need to verify that operations remain unchanged under neutral conditions.
ML Context: In neural networks (e.g., ResNet architectures), identity matrices are used in skip connections to preserve information across layers, preventing vanishing gradients and improving model training stability. This enhances interpretability by allowing stakeholders to trace how input features influence outputs without distortion.
"""
import numpy as np

# Business Scenario: Inventory Passthrough
# Represent inventory levels for 3 products. Identity matrix ensures no change in levels (e.g., no sales or restocking).
inventory = np.array([[100], [200], [150]])  # Current inventory (3 products x 1)
identity = np.eye(3)  # 3x3 identity matrix

# Multiply: New inventory = Identity * Current inventory (no change)
new_inventory = np.dot(identity, inventory)
print("Business: Inventory Passthrough (No Change):")
print("Original Inventory:\n", inventory)
print("After Identity Multiplication:\n", new_inventory)
print("Interpretation: For stakeholders, this confirms system stability—inventory remains unchanged, aiding audit trails.")

# ML Scenario: Skip Connection in Neural Network
# Simulate a simple layer output and add identity skip connection for feature preservation.
input_features = np.array([[0.5, 0.3], [0.7, 0.2]])  # 2 samples x 2 features
weights = np.array([[0.1, 0.4], [0.6, 0.9]])  # Transformation weights
layer_output = np.dot(input_features, weights)  # Transformed features

# Identity skip: Add original features (multiplied by identity) to preserve info
identity_skip = np.dot(input_features, np.eye(2))  # Identity preserves original
final_output = layer_output + identity_skip
print("\nML: Skip Connection for Feature Preservation:")
print("Input Features:\n", input_features)
print("Transformed Output:\n", layer_output)
print("Final Output with Identity Skip:\n", final_output)
print("Interpretation: Stakeholders see how original features are retained, improving model explainability in deep learning.")