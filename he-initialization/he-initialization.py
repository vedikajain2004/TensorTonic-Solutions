def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    l = (6 / fan_in) ** 0.5
    m, n = len(W), len(W[0])
    win = [[W[i][j] * 2 * l - l for j in range(n)] for i in range(m)]
    return win