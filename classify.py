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
            output_file.write(filename + 
                              " predicted as: " + 
                              Music.decrypt(Music.numcepGen(filename),K) + '\n')
    output_file.close()
    

    
