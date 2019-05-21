# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:27:47 2018

@author: sr38553
"""

import sys
if not __IPYTHON__:
    import pkg_resources
    from distutils.version import StrictVersion
    import pip
    pip_v = pkg_resources.get_distribution("pip").version
    modules = ['pandas','pdb','glob','io','pathlib','scipy']
    
    '''if pip version 10.01 or greater'''
    if StrictVersion(pip_v) > StrictVersion('10.0.0'):
        from pip._internal import main as _main  
        for m in modules:
            _main(['install',m])
    else:
        for m in modules:
            pip.main(['install',m])


from pdb import set_trace as breakpoint

import numpy as np
import pandas as pd
import pandas.io.formats.excel
import os
import glob
from pathlib import Path
import math as m

"""include local library in path"""
sys.path.insert(0, '.')
import _settings as settings

config = settings.config
#getting data for analysis
##get data
class data:
    #reading csv files
    try: #use _file_ in most cases
        dir = os.path.dirname(__file__)
    except NameError:  #except when running python from py2exe script
        import sys
        dir = os.path.dirname(sys.argv[0])

    def __init__(self, config):
        pandas.io.formats.excel.header_style = None
        self.cgxy = ''
        self.log = ''
        self.config = config
        self.c = dict(
            black = '\33[40m',
            red =  '\33[41m',
            green =  '\33[42m',
            orange = '\33[43m',
            purple = '\33[45m',
            blue =  '\33[46m',
            grey =  '\33[47m',
            ENDC = '\033[0m')

    def getData(self):
        """step 1: importing data
        """
        #------------read csv as dataframe

        ##directory
        directory = glob.glob(os.path.join(config['path'] + "/*.csv"))
        ##list of dataframes
        l_df = []
        ##for each file
        for f in directory: 
            df_ = pd.read_csv(f, engine='c', delimiter=',', encoding="utf-8-sig")
            
            #skip files less than a certain size
            filesize = os.path.getsize(f)
            #print('file: %s; size: %s'%(f,filesize))
            if filesize <= 2000:
                continue
            
            ##removing instructions and breaks
            df_ = df_[~(df_['InstrKey_resp.keys'] == 'space') & ~(df_['BreakKey_resp.keys'] == 'space')]
            
            ##add filename as column
            df_ = df_.assign(filename = os.path.splitext(os.path.basename(f))[0])
            
            #add trial as column
            df_['trial'] = df_.index
            
            ##append
            l_df.append(df_)
            
          
        ##concatinate
        df = pd.concat(l_df, ignore_index=True, sort=False)
        
        #------------get subject list
        files = []
        for idx in directory:
            p = Path(idx)
            subject = p.name
            subject_session = [subject]
            files.append(subject_session)       
        
        #------------clean data
        df = self.cleanData(df)

        return df, directory, files

    def cleanData(self, df):
        """step 2: cleaning data
        """
        print('collapse columns') 
        #-------------collapse columns
        ##group > Block > Block_Trial > Event
        cols=['TrialsF1.thisRepN','TrialsF2.thisRepN','TrialsM1.thisRepN','TrialsM2.thisRepN']
        df['Trials.thisRepN'] = df[cols].sum(1)   
        
        cols=['TrialsF1.thisTrialN','TrialsF2.thisTrialN','TrialsM1.thisTrialN','TrialsM2.thisTrialN']
        df['Trials.thisTrialN'] = df[cols].sum(1)       
        
        cols=['TrialsF1.thisN','TrialsF2.thisN','TrialsM1.thisN','TrialsM2.thisN']
        df['Trials.thisN'] = df[cols].sum(1)       
        
        cols=['TrialsF1.thisIndex','TrialsF2.thisIndex','TrialsM1.thisIndex','TrialsM2.thisIndex']
        df['Trials.thisIndex'] = df[cols].sum(1)

        print('keep columns')    
        #-------------keep columns
        df = df[['participant','filename','date','condition','Trials.thisRepN','Trials.thisTrialN','Trials.thisN','Trials.thisIndex','trial',
                 'Key_Resp.keys','correct_answer','accuracy','Key_Resp.rt','code',
                 'Image0 _Position','Image1 _Position','Image2 _Position','Image3 _Position','Center_image']]
        
        print('date format')                
        #-------------date format
        df['date'] = pd.to_datetime(df['date'], format='%Y_%b_%d_%H%M')
        
        print('rename')
        #-------------rename
        df = df.rename(columns={"Key_Resp.rt": "rt", 'accuracy':'acc', 'Center_image':'probe',"Image0 _Position": "up", 
                                "Image1 _Position": "right", 'Image2 _Position':'down', 'Image3 _Position':'left'})
        
        print('convert rt to msec')
        #-------------convert rt to msec
        df['rt'] = df['rt'].apply(lambda x: x*1000)
        
        print('convert accuracy from [16,32,48] to 1,0')
        #-------------convert accuracy from [16,32,48] to 1,0
        ##accuracy: 1(16)=correct; 0(32)=incorrect; 0(48)=no response
        df['acc'] = df['acc'].replace({16:1,32:0,48:0})
        
        print('remove duplicates')
        #-------------remove duplicates
        if True:
            ##filter if participant and filename do not match (i.e. 1000 and 1000x)
            df = df.assign(duplicate = df['participant'].astype(str) != df['filename'].astype(str))
            ##rearrange columns
            _col = list(df)
            _col.insert(2, _col.pop(_col.index('duplicate')))
            df = df.loc[:, _col]
            ##finish
            duplicates = df[df['duplicate'] == True] #duplicates
            df = df[df['duplicate'] == False] #originals
            
            ##list of subjects
            print('list of subjects')
            ###originals
            subjects = df.groupby(['filename'], as_index=False).first().reset_index(drop=True)
            subjects[['participant','filename','date']].to_excel(config['output'] + '\\subjects.xlsx', index_label='index')
            ###duplicates
            duplicates = duplicates.groupby(['filename'], as_index=False).first().reset_index(drop=True)
            duplicates[['participant','filename','date']].to_excel(config['output'] + '\\duplicates.xlsx', index_label='index')
        
        print('convert from: num8, num6 etc. to: top, right, etc.')
        #-------------convert num8, num6 etc. to top, right, etc
        if True:
            #-------------response
            df['resp'] = df['Key_Resp.keys']
            for idx, r in enumerate(['up','right','down','left']):
                num = ['num_8','num_6','num_2','num_4']
                df['resp'] = df['resp'].apply(lambda x: r if x == num[idx] else x)
            del r, idx, num
            ##rearrange columns
            _col = list(df)
            _col.insert(12, _col.pop(_col.index('resp')))
            df = df.loc[:, _col]
            
            #-------------correct response
            df['c_resp'] = df['correct_answer']
            for idx, r in enumerate(['up','right','down','left']):
                num = ['num_8','num_6','num_2','num_4']
                df['c_resp'] = df['c_resp'].apply(lambda x: r if x == num[idx] else x)
            del r, idx, num
            ##rearrange columns
            _col = list(df)
            _col.insert(13, _col.pop(_col.index('c_resp')))
            df = df.loc[:, _col]
            
        print('remove jpg, JPG from stim name')
        #-------------remove jpg, JPG from stim name
        if True:    
            for r in ['up','right','down','left','probe']:
                df[r] = df[r].map(lambda x: x.rstrip('.jpg'))
            del r
        
        print('adding probe emotion variable')
        #-------------adding probe emotion variable
        if True:
            df['probe_emotion'] = np.where(((df['condition'] == 'FS') | (df['condition'] == 'MS')), 'sad', 'neutral')
        
            ##rearrange columns
            _col = list(df)
            _col.insert(5, _col.pop(_col.index('probe_emotion')))
            df = df.loc[:, _col]
        
        print('adding error emotion variable')
        #-------------adding error emotion variable
        if True:
            df["error_emotion"] = np.where((df['probe_emotion'] == 'neutral'), 'sad', 'neutral')
            ##rearrange columns
            _col = list(df)
            _col.insert(6, _col.pop(_col.index('error_emotion')))
            df = df.loc[:, _col]
        
        print('get real participant and session numbers')
        #-------------get real participant and session numbers
        if True:    
            ##get real session number
            df['session'] = df['participant'].map(lambda x: str(x)[:-5])
            ###rearrange columns
            _col = list(df)
            _col.insert(1, _col.pop(_col.index('session')))
            df = df.loc[:, _col]
            
            ##get real participant number
            df['participant'] = df['participant'].map(lambda x: str(x)[1:])
            ###rearrange columns
            _col = list(df)
            _col.insert(0, _col.pop(_col.index('participant')))
            df = df.loc[:, _col]
            
            ##sort and finished
            df = df.sort_values(['participant', 'session'], ascending=[True, True])
        
        return df

    def run(self):
        ##get raw data
        df, directory, files = self.getData()
        return df, directory, files




















