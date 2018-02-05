# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 13:05:01 2018

@author: Jicheng Xu and Maxwell Lin
"""

from python_speech_features import mfcc
import knnclassifier
import numpy as np
import scipy.io.wavfile as wav
import os
import Music

PREPROCESS = True #if True, it will preprocess the data
FEATURE_COUNT = 1000
K = 5

def read_data(path_to_file):
    data = np.genfromtxt(path_to_file, delimiter=None)
    return knnclassifier.knnClassifer(data[:,1:],data[:,0])
    
def test_learner():
    test_train = np.asarray([[1,1,1,1,1],[2,3,1,1,1],[3,3,3,3,3]])
    classes = np.asarray(['jazz','classical','jazz'])
    test_pre = np.asarray([[1,1,1,1,1]])

    classify = knnclassifier.knnClassifer(test_train,classes)
    print(classify.predict(test_pre,5))

if __name__ == "__main__":
    if PREPROCESS:
        Music.preprocess(FEATURE_COUNT)
        print("preprocess done")
    directory = 'predictions'
    classifier = read_data("SongData.txt")
    #test_learner()
    output_file = open("predictions.txt",'w')
    results = []
    for filename in os.listdir(directory):
        if filename.endswith(".wav"): 
            file_path = os.path.join(directory, filename)
            print("loading prediction: " + file_path)
            (rate,sig) = wav.read(file_path)
            mfcc_feat = mfcc(sig,rate,numcep=13,)
            #print(mfcc_feat.ravel()[:FEATURE_COUNT])
            output_file.write(filename + 
                              " predicted as: " + 
                              Music.decrypt(classifier.predict(mfcc_feat.ravel()[:FEATURE_COUNT],K)) + '\n')
    output_file.close()
    

    
