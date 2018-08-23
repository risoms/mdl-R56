# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:02:40 2018

@author: sr38553
"""
#include local library in path
if not __IPYTHON__:
    import pkg_resources
    from distutils.version import StrictVersion
    import pip
    pip_v = pkg_resources.get_distribution("pip").version
    modules = ['pandas','numpy']
    
    '''if pip version 10.01 or greater'''
    if StrictVersion(pip_v) > StrictVersion('10.0.0'):
        from pip._internal import main as _main  
        for m in modules:
            _main(['install',m])
    else:
        for m in modules:
            pip.main(['install',m])
            
#loading
import _settings as settings
import _process as process
import pandas as pd
import numpy as np

#--------------------------------------------------------------------------------notes
#notes
##trial
'''
1) fixation cross
2) probe: one face (replaces fixation cross)
3) stimuli: 4 faces with fixation (probe gone) 
4) delay with fixation (no 4 faces, no probe)
'''
##variables
'''
positioning of stimuli: Image1/num_8: up, Image2/num_6: right, Image3/num_2: down, Image4/num_4: left
accuracy: 1(16)=correct; 0(32)=incorrect; 0(48)=no response
condition: 'male_neutral'='MN'; 'male_sad'='MS'; 'female_neutral'='FN'; 'female_sad':'FS'
'''
##participant numbers
'''
2 sessions (i.e. 100028[session 1], 200028[session 2])
'''
#--------------------------------------------------------------------------------todo
#TODO! 2018-09-20 3:39PM - Semeon
"""
1) Done: prevent duplicate participant data from being combined (i.e. 100048.csv and 100048x.csv)
2) Done: do email requests
3) Done: run task in psychopy to make sure image location is included
4) Done: upload to box
5) Done: send results to chris, alex, molly, david
"""

#--------------------------------------------------------------------------------start
if True:
    config = settings.config
    analysis = process.data(config)
    
    #get raw data
    #note #converted accuracy from [48,32,16] to 2,1,0
    #triggers
    ##accuracy: 1(16)=correct; 0(32)=incorrect; 0(48)=no response
    ##condition:'male_neutral'='MN';'male_sad'='MS';'female_neutral'='FN';'female_sad':'FS'
    print('get raw data')
    df, path_, list_ = analysis.run()
    df = df.reset_index(drop=True)

print('summary statistics')
#--------------------------------------------------------------------------------summary statistics
if True:
    ##by participant
    print('by participant')
    by_participant = df.groupby(['participant','session'], as_index=True).agg({
        'trial':['count'],
        'acc':['mean'],
        'rt': ['mean']
    }).reset_index()
    ##collapse multindex columns to single column
    by_participant.columns = [w.replace('mean', '(mean)') for w in [' '.join(col).strip() for col in by_participant.columns.values]]
    ##save
    by_participant.to_excel(config['output'] + '\\by_participant.xlsx', index_label='index')
    
    ##by condition
    print('by condition')
    by_condition = df.groupby(['participant','session','condition'], as_index=True).agg({
        'trial':['count'],
        'acc':['mean'],
        'rt': ['mean']
    }).reset_index()
    ##collapse multindex columns to single column
    by_condition.columns = [w.replace('mean', '(mean)') for w in [' '.join(col).strip() for col in by_condition.columns.values]]
    by_condition.to_excel(config['output'] + '\\by_condition.xlsx', index_label='index')
    
    ##by emotion
    print('by emotion')
    by_emotion = df.groupby(['participant','session','acc','probe_emotion','error_emotion'], as_index=True).agg({
        'trial':['count'],
        'rt': ['mean']
    }).reset_index()
    ##collapse multindex columns to single column
    by_emotion.columns = [w.replace('mean', '(mean)').replace('count', '(count)') 
        for w in [' '.join(col).strip() for col in by_emotion.columns.values]]
    by_emotion.to_excel(config['output'] + '\\by_emotion.xlsx', index_label='index')

del list_, path_    

print('testing')
#--------------------------------------------------------------------------------testing
#TODO! Test with subject 100028. delete this when done and just use df
test = df[df['filename'] == str('100028')].reset_index(drop=True)


variables = df.columns.to_frame(index=True)
variables.to_excel(config['output'] + '\\variables.xlsx', index_label='index')