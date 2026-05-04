import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here
    y_true, y_score = np.array(y_true), np.array(y_score)
    n = len(y_true)
    loss = np.array([max(0, margin - y_true[i] * y_score[i]) for i in range(n)])
    if reduction == 'sum':
        return np.sum(loss)
    return np.mean(loss)
    pass