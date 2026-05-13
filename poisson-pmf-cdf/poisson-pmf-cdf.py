import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    pmf = lambda x: np.exp(-lam) * lam ** x / np.prod(np.arange(1, x + 1, 1))
    cdf = np.exp(-lam) + np.sum([pmf(i) for i in range(1, k + 1)])
    return pmf(k), cdf
    pass