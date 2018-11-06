# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 08:14:22 2017

@author: sr38553
"""

import glob
import os
import pandas
try: #use _file_ in most cases
    dir = os.path.dirname(__file__)
except NameError:  #except when running python from py2exe script
    import sys
    dir = os.path.dirname(sys.argv[0])



#read images
img_dir = os.listdir("Stim/")
img_df = pandas.DataFrame({'scenestim': img_dir})

#read csv
var_dir = os.path.join(dir, "data/variable_list.csv")
var_df = pandas.read_csv(var_dir)

#merged
#df_merged = pandas.merge(img_df, var_df, left_on=['scenestim'],right_on=['scenestim'],how='inner') 
df_merged = img_df.merge(var_df, left_on='scenestim', right_on='scenestim')
df_merged.to_csv('merged.csv', index=False)


