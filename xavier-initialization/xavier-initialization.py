def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    l = (6 / (fan_in + fan_out)) ** 0.5
    w = [[j * 2 * l - l for j in i] for i in W]
    return w