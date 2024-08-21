# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 18:42:49 2023

@author: Zirui Zhang
"""

import pandas as pd
import colorsys
import os
import glob
condition_list = ['City_Novelty','Beach_8 times','Beach_Repeat once','Beach_Novelty','City_8 times','City_Repeat once']
runs = ['Run1']
subID = ['ZZR']

for ref in subID:
    dataPath = "./"

    for file in glob.glob(dataPath + "*.txt"):
        c = str(file)
        
        if str(file[6:10]) in runs: #needto match the file name: str(file[6:10]) = 'Run1'
        
        

            dataFile = pd.read_csv(file,sep='\t')
            #a = dataFile['event'].map(len) == 4
            #####
            ## trials
            #####
    
            prtPath = file[0:-4] + '_test_split.prt'
            c = dataFile['event']
           # dataEvent = []
            #for event in dataFile['event']:
                #if event not in ['task','response']:
                    #j = event.split('_',1)[1]
                    #dataEvent.append(j)
                
                
    
            trialOnsets = [event in condition_list for event in dataFile['event']]
            #trialOnsets = [event in condition_list for event in dataEvent]
            dataFile_filt = dataFile[trialOnsets].copy()
            dataFile_filt['Type'] = [event.split('_',1)[1] for event in dataFile.iloc[dataFile[trialOnsets].index]["event"]]
    
            # in ms, rounded to cs
            dataFile_filt['Onset_1'] = round(dataFile_filt.onset*100, 0).astype('int')*10
            dataFile_filt['Onset_2'] = dataFile_filt.Onset_1 + 6000
    
            types = pd.unique(dataFile_filt.Type.ravel())
            types.sort()
            f = [dataFile_filt.loc[dataFile_filt.Type == i, ['Type', 'Onset_1', 'Onset_2']] for i in types]
    
            f_str = [f[i][['Onset_1', 'Onset_2']].to_string(header = False, index = False, col_space=4, justify='right') for i in range(len(types))]
    
            colors = [[int(255*x) for x in colorsys.hsv_to_rgb(1.0 / (len(types) + 1) * i, 1.0, 1.0)] for i in range(0, len(types))]
    
            p = '\n'.join(['{}\n{}\n{}\nColor: {}\n'.format(types[i], len(f[i]), f_str[i], ' '.join(map(str,colors[i]))) for i in range(len(types))])
    
            printFile = open(prtPath,'w')
            printFile.writelines(['\n',
                                'FileVersion:        2\n',
                                '\n',
                                'ResolutionOfTime:   msecs\n',
                                '\n',
                                'Experiment:         Memory\n',
                                '\n',
                                'BackgroundColor:    0 0 0\n',
                                'TextColor:          255 255 255\n',
                                'TimeCourseColor:    255 255 255\n',
                                'TimeCourseThick:    3\n',
                                'ReferenceFuncColor: 100 100 200\n',
                                'ReferenceFuncThick: 2\n',
                                '\n'])
            printFile.write('NrOfConditions:     {}\n\n'.format(len(types)))
            printFile.write(p  + '\n')
            
    
    
            trialOnsets = [event in ['target','border'] for event in dataFile['event']]
     
            dataFile_filt = dataFile[trialOnsets].copy()
     
            dataFile_filt['Type'] = [event for event in dataFile.iloc[dataFile[trialOnsets].index]["event"]]
     
             # in ms, rounded to cs
            dataFile_filt['Onset_1'] = round(dataFile_filt.onset*100, 0).astype('int')*10
            dataFile_filt['Onset_2'] = dataFile_filt.Onset_1 + 12000
     
            types = pd.unique(dataFile_filt.Type.ravel())
            types.sort()
            f = [dataFile_filt.loc[dataFile_filt.Type == i, ['Type', 'Onset_1', 'Onset_2']] for i in types]
     
            f_str = [f[i][['Onset_1', 'Onset_2']].to_string(header = False, index = False, col_space=4, justify='right') for i in range(len(types))]
     
            colors = [[int(255*x) for x in colorsys.hsv_to_rgb(1.0 / (len(types) + 1) * i, 1.0, 1.0)] for i in range(0, len(types))]
     
            p = '\n'.join(['{}\n{}\n{}\nColor: {}\n'.format(types[i], len(f[i]), f_str[i], ' '.join(map(str,colors[i]))) for i in range(len(types))])
    
            printFile.write(p  + '\n')
            printFile.close()


print("done")
