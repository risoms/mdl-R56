# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:24:33 2018

@author: sr38553
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 10:13:24 2018

@author: sr38553
"""

#include local library in path
import sys
import os
sys.path.insert(0, './lib')
#reading csv files
try: #use _file_ in most cases
    dir = os.path.dirname(__file__)
except NameError:  #except when running python from py2exe script
    import sys
    dir = os.path.dirname(sys.argv[0])

config={
    #------------------------file location
    'path': os.path.abspath(os.path.join(os.getcwd(), '..\\','raw')),
    'root': os.path.abspath(os.path.join(os.getcwd(), '..\\')),
    'output': os.path.abspath(os.path.join(os.getcwd(), '..\\','output')),
}