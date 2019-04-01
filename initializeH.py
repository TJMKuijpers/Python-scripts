# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:41:39 2019

@author: tim.kuijpers
"""
import numpy as np
def initializeH(priorknowledge,k,samplenumbers):
    "Initialize the matrix"
    Hempty = np.full((k,samplenumbers), 0)
    for x in range(0, len(priorknowledge)):
        Hempty[priorknowledge[x]-1,x]=1
    return Hempty