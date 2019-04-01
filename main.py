# -*- coding: utf-8 -*-
"""
Main file
Created on Thu Mar  7 16:18:42 2019

@author: tim.kuijpers
"""

"Use the Toy data"
from readData import readData
from multiNMF import coAssociationMatrix,consensusMatrix,initializeH
from createToyData import createToyData,getPriorKnowledge,randomizeToyData
from multiNMF import updateH_multiomics,seung_updateW,multi_nmf,objective_value
from plotFunctionsNMF import consensusMatrix,determineClusterMembers,coAssociationMatrix


import matplotlib.pyplot as plt
import numpy as np

X1,X2=createToyData(0.6)
X1rand,X2rand=randomizeToyData(X1,X2)
priorknowledge_ToyDataNoise=getPriorKnowledge()
k=3
samples=200
initializedH_toydata=initializeH(priorknowledge_ToyDataNoise,k,samples)

# Perform multi NMF 
"""
Toydata=[X1,X2]
Wstate_ResultsRandom_MultipleRuns=[]
Hmulti_ResultsRandom_MultipleRuns=[]
Fvalues_MultipleRuns=[]
simulations=1
for y in range(simulations):
    Hrandom=np.random.rand(3,200)
    Wstate_multi,Hmulti,Fvalues_multi=multi_nmf(Toydata,3,Hrandom,threshold=1e-5,maxitermultinmf=2000)
    Wstate_ResultsRandom_MultipleRuns.append(Wstate_multi)
    Hmulti_ResultsRandom_MultipleRuns.append(Hmulti)
    Fvalues_MultipleRuns.append(Fvalues_multi)
    if (y%2)==0:
        print('simulation',y)

"""
" Use the TCGA breast cancer dataset"
# Read the expression data (gene, methylation) and metadata for TCGA breast cancer
print('Load data')  
geneExpression=readData(fileName='C:/Users/tim.kuijpers/Desktop/NCI60 data/GeneDataNMF.txt')
dnaMethylation=readData(fileName='C:/Users/tim.kuijpers/Desktop/NCI60 data/CpGDataNMF.txt')
#metaData=readData(fileName='C:/Users/tim.kuijpers/Desktop/NCI60 data/')
print(geneExpression.shape)
NCI60data=[geneExpression,dnaMethylation]
# Use the groupClustering to initialize H
#groupClustering=groupClustering['clusterid'].values
k_NCI60=7                 # number of clusters
#samples_TCGA=len(groupClustering)       # number of samples
#initializedH_TCGAbreastData=initializeH(groupClustering,k_TCGA,samples_TCGA)

# Run multi nmf
Wstate_ResultsHinit_NCI60=[]
Hmulti_ResultsHinit_NCI60=[]
Fvalues_Hinit_NCI60=[]
simulations_TCGA=5
for y in range(simulations_TCGA):
    Hinitialized=np.random.rand(k_NCI60,geneExpression.shape[1])
    Wstate_multi_TCGA,Hmulti_TCGA,Fvalues_multi_TCGA=multi_nmf(NCI60data,k_NCI60,Hinitialized,threshold=1e-5,maxitermultinmf=2000)
    Wstate_ResultsHinit_NCI60.append(Wstate_multi_TCGA)
    Hmulti_ResultsHinit_NCI60.append(Hmulti_TCGA)
    Fvalues_Hinit_NCI60.append(Fvalues_multi_TCGA)

       