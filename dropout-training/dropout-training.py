import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.array(x)
    s = x.shape
    if rng is not None:
        ps = rng.random(size=s)
    else:
        ps = np.random.random(size=s)
    m = (ps > p) / (1 - p)
    d = x * m
    return d, m
    pass