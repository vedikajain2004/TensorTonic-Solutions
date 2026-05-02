import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.array(C)
    m, n = C.shape
    c, r = [np.sum(C[: , j]) for j in range(n)], [np.sum(C[i, :]) for i in range(m)]
    E = np.array([[r[i] * c[j] for j in range(n)] for i in range(m)])
    E = E / np.sum(C)
    chi = np.sum(((C - E) ** 2) / E)
    return chi, E
    pass