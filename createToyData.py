# -*- coding: utf-8 -*-
"""
Function file to create toy data
Created on Thu Mar  7 16:32:05 2019

@author: tim.kuijpers
"""
import numpy as np
from sklearn.utils import shuffle

def createToyData(noiseLevel):
    " Create data with 50 columns and 3 groups but different dimensions "
    pattern1=np.ones((1500,50))
    pattern2=np.ones((1000,100))
    pattern3=np.ones((1500,50))

    pattern4=np.ones((200,50))
    pattern5=np.ones((1000,100))
    pattern6=np.ones((800,50))


    "Initialize X1 and X2 toy data matrices"
    X1toy=noiseLevel*np.random.rand(4000,200)
    X2toy=noiseLevel*np.random.rand(2000,200)

    "Place patterns in toy data matrices"
    X1toy[0:1500,0:50]=pattern1
    X1toy[1500:2500,50:150]=pattern2
    X1toy[2500:4000,150:200]=pattern3

    X2toy[0:200,0:50]=pattern4
    X2toy[200:1200,50:150]=pattern5
    X2toy[1200:2000,150:200]=pattern6

    x1r,x1c=X1toy.shape
    x2r,x2c=X2toy.shape
    X1toynoise=noiseLevel*np.random.rand(x1r,x1c)
    X2toynoise=noiseLevel*np.random.rand(x2r,x2c)
   
    return (X1toy,X2toy)

def getPriorKnowledge():
    membersCluster1=np.ones((1,50),dtype='int')
    membersCluster2=np.ones((1,100),dtype='int')+1
    membersCluster3=np.ones((1,50),dtype='int')+2
    priorknowledgeToyData=np.concatenate((membersCluster1,membersCluster2,membersCluster3),axis=None)
    priorknowledgeToyData=priorknowledgeToyData.tolist()
    return priorknowledgeToyData

def randomizeToyData(X1,X2):
    X1shuffled=shuffle(X1,random_state=0)
    X2shuffled=shuffle(X2,random_state=0)
    X1t=np.transpose(X1shuffled)
    X2t=np.transpose(X2shuffled)
    X1t=shuffle(X1t,random_state=0)
    X2t=shuffle(X2t,random_state=0)
    X1=np.transpose(X1t)
    X2=np.transpose(X2t)
    return X1,X2
