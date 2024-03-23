import numpy as np
import matplotlib.pyplot as plt

# Define the range of predicted probabilities (between 0 and 1)
predictions = np.linspace(0.01, 0.99, 100)

# Define the binary cross-entropy loss function
def binary_cross_entropy(y_true, y_pred):
    return - (y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# Set the true label (0 or 1)
true_label = 1  # For example, let's consider the true label to be 1

# Calculate the binary cross-entropy loss for the given true label
loss = binary_cross_entropy(true_label, predictions)

# Plotting
plt.plot(predictions, loss)
plt.xlabel('Predicted Probability')
plt.ylabel('Binary Cross-Entropy Loss')
plt.title('Binary Cross-Entropy Loss vs. Predicted Probability')
plt.grid(True)
plt.show()