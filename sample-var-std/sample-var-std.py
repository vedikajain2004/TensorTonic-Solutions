import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    n, x = len(x), np.array(x)
    var = np.var(x) * n / (n - 1)
    return var, var ** 0.5
    pass