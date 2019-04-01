# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:30:36 2019

@author: tim.kuijpers
"""

def readData(fileName):
    import pandas as pd
    datafile=pd.read_csv(fileName,sep='\t',index_col=0)
    return datafile
