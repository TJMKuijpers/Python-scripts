# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:04:56 2019

@author: tim.kuijpers
"""
import numpy as np
def consensusMatrix(Hdata,samplenames):
    CoAssociationMatrices=[]
    for x in range(len(Hdata)):
        MembersOfClusters,occurenceCluster=determineClusterMembers(Hdata[x],samplenames)
        CoAssociationMatrix=coAssociationMatrix(occurenceCluster)
        CoAssociationMatrices.append(CoAssociationMatrix)
        Consensusmatrix=sum(CoAssociationMatrices)
        Consensusmatrix=Consensusmatrix/len(Hdata)
    
    return Consensusmatrix

def determineClusterMembers(Hmatrix,samplenames):
    "For each column in H, maximum value will be determined and right cluster assigned"
    index_maxvalue=np.argmax(Hmatrix,axis=0)
    ClusterMembers=[]
    for cluster in range(np.min(index_maxvalue),np.max(index_maxvalue)+1):
        ClusterMembers.append([i for indx, i in enumerate(samplenames) if index_maxvalue[indx]==cluster])
        
    return ClusterMembers,index_maxvalue

def coAssociationMatrix(clusterlist):
    "For each list of samples in cluster create a association matrix"
    results=[[int(x==y) for y in clusterlist]for x in clusterlist]
    coAssociation=np.array(results)
    
    return coAssociation