import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X = np.array(X)
    ex = 0
    try:
        n, f = X.shape
    except:
        X = np.expand_dims(X, axis=1)
        ex = 1
        n, f = X.shape
    for i in range(f):
        if np.isnan(X[:, i]).any:
            if strategy == 'mean':
                u = np.nanmean(X[:, i])
            else:
                u = np.nanmedian(X[:, i])
            if np.isnan(u):
                u = 0
            X[:, i] = np.array([u if np.isnan(X[j, i]) else X[j, i] for j in range(n)])
    if ex:
        return np.squeeze(X)
    return X
    pass