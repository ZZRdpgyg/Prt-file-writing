# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 18:42:49 2023

@author: Zirui Zhang
"""

import pandas as pd
import colorsys
import os
import glob
import csv
condition_list = ['Beach_Novelty','City_Novelty', 'City_8 times','Beach_8 times','City_Repeat once','Beach_Repeat once']
subID = ['RBE03']

for ref in subID:
    dataPath = "./"

    for file in glob.glob(dataPath + "*.txt"):
        
            dataFile = pd.read_csv(file,sep='\t')
            event = list([i for i in dataFile['event'] if i not in ['task','response']])
            del event[48]
            #a = dataFile['event'].map(len) == 4
            #####
            ## trials
            #####
            dataFile.drop(dataFile.index[(dataFile["event"]=='task')],axis=0,inplace=True)
            dataFile.drop(dataFile.index[(dataFile["event"]=='response')],axis=0,inplace=True)
            dataFile.drop(1,axis=0,inplace=True)
            onset = list(dataFile['onset'])
            
            prtPath = file[0:-4] + '_history.txt'
            f = open(prtPath,'w')
            writer = csv.writer(f, delimiter='\t')
            writer.writerow(['onset','event'])
            writer.writerows(zip(onset,event))
            f.close()
        
        
        
