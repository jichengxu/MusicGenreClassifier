# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import path
import numpy

from python_speech_features import mfcc

import scipy.io.wavfile as wav


# returns a list of nemcep numbers

def encrypt(string):
    encoder = {'Rock':1,'Pop':2,'Jazz':3,'Classical':4,'Blues':5}
    return encoder[string]
def decrypt(integer):
    decrypter = {1:'Rock', 2:'Pop', 3:'Jazz', 4:'Classical', 5:'Blues'}
    return decrypter[integer]

def numcepGen(strPath):
    print("preprocessing " + strPath)
    (rate,sig) = wav.read(strPath)
    mfcc_feat = mfcc(sig,rate,numcep=13,)
    return ( mfcc_feat.ravel() )

def controlledNumcepGen(strPath,count):
    return numcepGen(strPath)[:count]

def preprocess(count):
    f = open('SongData.txt','w')
    musicList = path.get_all_strpath()
    for genreList in musicList:
        #print(musicList)
        genre = encrypt(genreList[0])
        for i in genreList[1:]:
            f.write(str(genre))
            f.write(' ')
            numList = controlledNumcepGen(i,count)
            for num in numList:
                f.write(str(num))
                f.write(' ')
            f.write('\n')
    f.close()
