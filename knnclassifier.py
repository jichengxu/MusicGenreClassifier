# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 13:06:47 2018

@author: Jicheng
"""
import numpy as np
from numpy import asarray as arr

class knnClassifer():
    def __init__(self,features,classes):
        self.classes = classes
        self.feats = features
        #print(self.feats)
        #print(self.classes)


    def predict(self,prediction_feats,K=1):
        '''predicts a music genre based on the given features and a K'''
        mtr,ntr = arr(self.feats).shape      # get size of training data
        #mte,nte = arr(prediction_feats).shape 
        assert K <= mtr
        #get the sum of the squared distances
        
        dist = np.sum(np.power((self.feats - prediction_feats), 2), axis=1)
        closest = self.classes[np.argsort(dist)[:K]]
        unique,counts = np.unique(closest,return_counts=True)
        print(closest)
        best=dict(zip(unique, counts))
        print(best)
        return max(best, key=best.get)
        