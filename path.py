# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 12:49:49 2018

@author: Maxwell Lin Jicheng Xu
"""
import os
import os.path

"""
***NOTE:*** must make a 'Music' directory in the current diectory of your python module!
"""

cwd = os.getcwd()
cwd = os.path.join(cwd, 'Music')
rootdir = cwd

def get_all_strpath():
    musicList = []
    for subdir, dirs, files in os.walk(rootdir):
        genreNpath = []
        for file in files:
            if os.path.basename(subdir) in genreNpath:
                genreNpath.append(os.path.join(subdir, file))
            else:
                genreNpath.append(os.path.basename(subdir))
                genreNpath.append(os.path.join(subdir, file))
        musicList.append(genreNpath)
#            print( os.path.basename(subdir) )
#            print os.path.join(subdir, file)
    musicList.pop(0)
    return musicList
#print(get_all_strpath())
