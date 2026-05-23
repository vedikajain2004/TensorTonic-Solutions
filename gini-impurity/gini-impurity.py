import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    yl, yr = np.array(y_left), np.array(y_right)
    _, cl = np.unique(yl, return_counts=True)
    _, cr = np.unique(yr, return_counts=True)
    nl, nr = yl.size, yr.size
    try:
        ginil = 1 - np.sum((cl / nl) ** 2)
    except ZeroDivisionError:
        ginil = 0
    try:
        ginir = 1 - np.sum((cr / nr) ** 2)
    except ZeroDivisionError:
        ginir = 0
    n = nl + nr
    try:
        return (nl / n) * ginil + (nr / n) * ginir
    except ZeroDivisionError:
        return 0.0
    pass