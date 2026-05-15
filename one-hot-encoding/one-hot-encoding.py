import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    if num_classes is None:
        num_classes = max(y) + 1
    return np.eye(num_classes)[y]
    pass