# -*- coding: utf-8 -*-
"""
Functions associated with multi NMF method

Created on Thu Mar  7 14:42:20 2019
@author:tim.kuijpers
"""
import numpy as np

def coAssociationMatrix(clusterlist):
    "For each list of samples in cluster create a association matrix"
    results = [[int(x == y) for y in clusterlist] for x in clusterlist]
    coAssociation = np.array(results)

    return coAssociation

def consensusMatrix(Hdata, samplenames):
    CoAssociationMatrices = []
    for x in range(len(Hdata)):
        MembersOfClusters, occurenceCluster = determineClusterMembers(Hdata[x], samplenames)
        CoAssociationMatrix = coAssociationMatrix(occurenceCluster)
        CoAssociationMatrices.append(CoAssociationMatrix)
        Consensusmatrix = sum(CoAssociationMatrices)
        Consensusmatrix = Consensusmatrix / len(Hdata)

    return Consensusmatrix

def initializeH(priorknowledge,k,samplenumbers):
    "Initialize the matrix"
    Hempty = np.full((k,samplenumbers), 0)
    for x in range(0, len(priorknowledge)):
        Hempty[priorknowledge[x]-1,x]=1
    return Hempty

def multi_nmf(ExperimentalData,k,Hinit,threshold,maxitermultinmf):
    numberofLayers=len(ExperimentalData)
    numberofObservations=[ExperimentalData[i].shape[0] for i in range(numberofLayers)]
    Wstate=[np.random.rand(numberofObservations[i],k) for i in range(numberofLayers)]
    H=Hinit
    it_no=0
    converged=False
    F = objective_value(ExperimentalData,Wstate,H)
    Fvalues=[]
    Fvalues.append(F)
    while(not converged) and it_no <=maxitermultinmf:
        Wstate_new=[seung_updateW(ExperimentalData[i],Wstate[i],H) for i in range(numberofLayers)]
        H_new=updateH_multiomics(ExperimentalData,Wstate,H)
        F_new=objective_value(ExperimentalData,Wstate_new,H_new)
        converged=np.abs(F_new-F) <=threshold
        Wstate,H=Wstate_new,H_new
        it_no=it_no+1
        Fvalues.append(F_new)
    return Wstate,H,Fvalues


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

def updateH_multiomics(Data,W,H):
    " H depends on both the combination of the omics layers, therefore of W1 and W2"
    """ Usage:
        H_new=updateH_multiomics(layer1,layer2,W_layer1,W_layer2)
        Parameters:
        X1: omics data layer 1
        X2: ommics data layer 2
        W1: (d1*k)-array of non-negative basis components layer 1
        W2: (d2*k)-array of non-negative basis components layer 2
        H:  (k*n)-array of weights, one column for each of the clusters
        Returns:
        H_new: updated version of H
     """
    WtX=[np.dot(W[i].T,Data[i]) for i in range(len(Data))]
    WtWH=[np.dot(np.dot(W[i].T,W[i]),H) for i in range(len(Data))]
    numdenum=[WtX[i]/WtWH[i] for i in range(len(Data))]
    H_new=H*(sum(numdenum))
    return H_new

def objective_value(Data,W,H):
    F=[np.linalg.norm(Data[i] - np.dot(W[i],H)) for i in range(len(Data))]
    "F=[(Data[i]*np.log(np.dot(W[i],H))-np.dot(W[i],H)) for i in range(len(Data))]"
    Fsum=sum(F)
    return Fsum