# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:35:06 2019

@author: tim.kuijpers
"""

from readData import readData
from multiNMF import coAssociationMatrix,consensusMatrix,initializeH
from createToyData import createToyData,getPriorKnowledge,randomizeToyData
from multiNMF import updateH_multiomics,seung_updateW,multi_nmf,objective_value
from plotFunctionsNMF import consensusMatrix,determineClusterMembers,coAssociationMatrix

