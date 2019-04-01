# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 17:19:04 2019

@author: tim.kuijpers
"""

def seung_nmf(V, k,Hinit, threshold=1e-5, maxiter=1000):
    ''' decomposes X into r components by non-negative matrix factorization

    Usage:
        W, H = seung_nmf(X, r)
    Parameters:
        V: a (d x n)-array containing n observations in the columns
        k: number of components to extract
        threshold: relative error threshold of the iteration
        maxiter: maximum number of iterations
    Returns:
        W: (d x k)-array of non-negative basis images (components)
        H: (k x n)-array of weights, one column for each of the n observations
    '''

    d, n = V.shape
    W = np.random.rand(d, k)
    H = Hinit
    F = seung_objective(V, W, H)
    Fvalues=[]
    Fvalues.append(F)
    it_no = 0
    converged = False

    while (not converged) and it_no <= maxiter:
        W_new = seung_updateW(V, W, H)
        H_new = seung_updateH(V, W_new, H)
        F_new = seung_objective(V, W_new, H_new)

        converged = np.abs(F_new - F) <= threshold
        W, H = W_new, H_new
        it_no = it_no + 1
        Fvalues.append(F_new)

    return W, H,Fvalues

def seung_objective(V, W, H):
    ''' calculated the non-negative matrix factorization objective

    Usage:
        W, H = seung_update(V, W, H)
    Parameters:
        V: a (d x n)-array containing n observations in the columns
        W: (d x k)-array of non-negative basis images (components)
        H: (k x n)-array of weights, one column for each of the n observations
    Returns:
        F: a scalar objective
    '''
    d, n = V.shape
    WH = np.dot(W, H)
    F= np.linalg.norm(V - np.dot(W,H))
    "F = (V * np.log(WH) - WH).sum() / (d * n)"
    return F

def seung_updateW(V, W, H):
    ''' performs the multiplicative non-negative matrix factorization updates for W

    Usage:
        W, H = seung_update(V, W, H)
    Parameters:
        V: a (d x n)-array containing n observations in the columns
        W: (d x k)-array of non-negative basis images (components)
        H: (k x n)-array of weights, one column for each of the n observations
    Returns:
        W: (d x k)-array of updated non-negative basis images (components)
    '''

    WH = np.dot(W, H)
    W_new = W * np.dot(V / WH, H.T)
    W_new = W_new / np.sum(W_new, axis=0, keepdims=True)
    return W_new


def seung_updateH(V, W, H):
    ''' performs the multiplicative non-negative matrix factorization updates

    Usage:
        W, H = seung_update(V, W, H)
    Parameters:
        V: a (d x n)-array containing n observations in the columns
        W: (d x k)-array of non-negative basis images (components)
        H: (k x n)-array of weights, one column for each of the n observations
    Returns:
        H: (k x n)-array of updated weights, one column for each of the n observations
    '''

    WH = np.dot(W, H)
    H_new = H * np.dot((V / WH).T, W).T
    return H_new