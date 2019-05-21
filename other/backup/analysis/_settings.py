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
    'definitions': {
        #------------------------file location
        'participant': 'participant number',
        'session': 'session number',
        'filename': 'filename',
        'duplicate': 'whether data had mismatched participant and filename number',
        'date': 'date',
        'condition': 'condition',
        'probe_emotion': 'emotion of probe (always opposite of error_emotion)',
        'error_emotion': 'incorrect emotion (always opposite of probe_emotion)',
        'Trials.thisRepN': 'Trials.thisRepN',
        'Trials.thisTrialN': 'Trials.thisTrialN',
        'Trials.thisN': 'Trials.thisN',
        'Trials.thisIndex': 'Trials.thisIndex',
        'trial': 'task level trial number',
        'Key_Resp.keys': 'participants keyboard response button',
        'correct_answer': 'keyboard correct response',
        'resp': 'participant response (from Key_resp.keys and converted to cardinal directions of stimuli))',
        'c_resp': 'correct response (from correct_answer and converted to cardinal directions of stimuli)',
        'acc': 'accuracy',
        'rt': 'response time',
        'code': 'code',
        'up': 'stimuli positioned above fixation',
        'right': 'stimuli positioned to the right of fixation',
        'down': 'stimuli positioned below fixation',
        'left': 'stimuli positioned to the left of fixation',
        'probe': 'probe'
    }
}