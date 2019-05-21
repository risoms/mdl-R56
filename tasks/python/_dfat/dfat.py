#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on January 11, 2017, at 11:44
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, FINISHED)
from numpy import random
import os  # handy system and path functions
import sys  # to get file system encoding

###-------added by me
#imports
from psychopy import parallel
#constants
stim_duration = 60 #stim duration (60)
numpad_list = ['num_1','num_2','num_3','num_4','num_5','num_6','num_7']
pport = parallel.ParallelPort(address='0xDFF8')
pport.setData(int(0))
prac_ttl = 1

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'DFAT'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
try: #look for pipe from app
    expInfo['participant'] = '%s'%(sys.argv[1])
    expInfo['session'] = '001'
except IndexError: #if no pipe, run normally
    print ('ran without app')
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    if dlg.OK == False:
        print ('app closed')
        core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
print 'subject:',expInfo['participant']
print 'exp:',expName
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920,1080], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
intro_image = visual.ImageStim(
    win=win, name='intro_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
intro_sound = sound.Sound(u'A', secs=-1)
intro_sound.setVolume(1)
#loop counter-practice
intro_repeat = 0

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
inst_image = visual.ImageStim(
    win=win, name='inst_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
inst_sound = sound.Sound(u'A', secs=-1)
inst_sound.setVolume(1)
inst_repeat = 0

# Initialize components for Routine "task"
taskClock = core.Clock()
task_image = visual.ImageStim(
    win=win, name='task_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "relax"
relaxClock = core.Clock()
relax_image = visual.ImageStim(
    win=win, name='relax_image',
    image="Instructions/png/r-0.png", mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
relax_sound = sound.Sound(u'A', secs=-1)
relax_sound.setVolume(1)

# Initialize components for Routine "survey"
surveyClock = core.Clock()
survey_image = visual.ImageStim(
    win=win, name='survey_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "block_finish"
block_finishClock = core.Clock()
block_finish_image = visual.ImageStim(
    win=win, name='block_finish_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
block_finish_sound = sound.Sound(u'A', secs=-1)
block_finish_sound.setVolume(1)
bf_repeat = 0

# Initialize components for Routine "task_introduction"
task_introductionClock = core.Clock()
task_intro_image = visual.ImageStim(
    win=win, name='task_intro_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
task_intro_sound = sound.Sound(u'A', secs=-1)
task_intro_sound.setVolume(1)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
inst_image = visual.ImageStim(
    win=win, name='inst_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
inst_sound = sound.Sound(u'A', secs=-1)
inst_sound.setVolume(1)
inst_repeat = 0

# Initialize components for Routine "task"
taskClock = core.Clock()
task_image = visual.ImageStim(
    win=win, name='task_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "relax"
relaxClock = core.Clock()
relax_image = visual.ImageStim(
    win=win, name='relax_image',
    image="Instructions/png/r-0.png", mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
relax_sound = sound.Sound(u'A', secs=-1)
relax_sound.setVolume(1)

# Initialize components for Routine "survey"
surveyClock = core.Clock()
survey_image = visual.ImageStim(
    win=win, name='survey_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "block_finish"
block_finishClock = core.Clock()
block_finish_image = visual.ImageStim(
    win=win, name='block_finish_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
block_finish_sound = sound.Sound(u'A', secs=-1)
block_finish_sound.setVolume(1)
bf_repeat = 0

# Initialize components for Routine "Finish"
FinishClock = core.Clock()
finish_image = visual.ImageStim(
    win=win, name='finish_image',
    image="Instructions/png/finish-0.png", mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
finish_sound = sound.Sound(u'A', secs=-1)
finish_sound.setVolume(1)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
intro_loop = data.TrialHandler(nReps=10, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='prac_intro_loop')
thisExp.addLoop(intro_loop)  # add the loop to the experiment
thisIntro_loop = intro_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIntro_loop.rgb)
if thisIntro_loop != None:
    for paramName in thisIntro_loop.keys():
        exec(paramName + '= thisIntro_loop.' + paramName)

for thisIntro_loop in intro_loop:
    currentLoop = intro_loop
    # abbreviate parameter names if possible (e.g. rgb = thisIntro_loop.rgb)
    if thisIntro_loop != None:
        for paramName in thisIntro_loop.keys():
            exec(paramName + '= thisIntro_loop.' + paramName)
    
    # ------Prepare to start Routine "introduction"-------
    t = 0
    introductionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    intro_key = event.BuilderKeyResponse()
    intro_image.setImage("Instructions/png/int-%s.png"%(intro_repeat))
    intro_sound.setSound("Instructions/wav/int-%s.wav"%(intro_repeat))
    # keep track of which components have finished
    introductionComponents = [intro_image, intro_key, intro_sound]
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "introduction"-------
    while continueRoutine:
        # get current time
        t = introductionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intro_image* updates
        if t >= 0.0 and intro_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            intro_image.tStart = t
            intro_image.frameNStart = frameN  # exact frame index
            intro_image.setAutoDraw(True)
        
        # *intro_key* updates
        if t >= 0.0 and intro_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            intro_key.tStart = t
            intro_key.frameNStart = frameN  # exact frame index
            intro_key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if intro_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        # start/stop intro_sound
        if t >= 0.0 and intro_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            intro_sound.tStart = t
            intro_sound.frameNStart = frameN  # exact frame index
            intro_sound.play()  # start the sound (it finishes automatically)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introductionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "introduction"-------
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    intro_sound.stop()  # ensure sound has stopped at end of routine
    intro_repeat = intro_repeat+1
    # the Routine "introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 10 repeats of 'intro_loop'

    
# set up handler to look after randomisation of conditions etc
prac_block = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(prac_block)  # add the loop to the experiment
thisPrac_block = prac_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_block.rgb)
if thisPrac_block != None:
    for paramName in thisPrac_block.keys():
        exec(paramName + '= thisPrac_block.' + paramName)

for thisPrac_block in prac_block:
    currentLoop = prac_block
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_block.rgb)
    if thisPrac_block != None:
        for paramName in thisPrac_block.keys():
            exec(paramName + '= thisPrac_block.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    prac_inst_loop = data.TrialHandler(nReps=3, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='inst_loop')
    thisExp.addLoop(prac_inst_loop)  # add the loop to the experiment
    thisPrac_inst_loop = prac_inst_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_inst_loop.rgb)
    if thisPrac_inst_loop != None:
        for paramName in thisPrac_inst_loop.keys():
            exec(paramName + '= thisPrac_inst_loop.' + paramName)
    
    for thisPrac_inst_loop in prac_inst_loop:
        currentLoop = prac_inst_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_inst_loop.rgb)
        if thisPrac_inst_loop != None:
            for paramName in thisPrac_inst_loop.keys():
                exec(paramName + '= thisPrac_inst_loop.' + paramName)
        
        # ------Prepare to start Routine "instructions"-------
        t = 0
        instructionsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        inst_key = event.BuilderKeyResponse()
        inst_image.setImage("Instructions/png/pi-%s.png"%(inst_repeat))
        #prevent loading of inst_sound for pi-0 and pi-2
        if not (inst_repeat== 0 or inst_repeat== 3):
            inst_sound.setSound("Instructions/wav/pi-%s.wav"%(inst_repeat))
            instructionsComponents = [inst_image, inst_key, inst_sound]
        else:
            # keep track of which components have finished
            instructionsComponents = [inst_image, inst_key]
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instructions"-------
        while continueRoutine:
            # get current time
            t = instructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inst_image* updates
            if t >= 0.0 and inst_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                inst_image.tStart = t
                inst_image.frameNStart = frameN  # exact frame index
                inst_image.setAutoDraw(True)
            
            # *inst_key* updates
            if t >= 0.0 and inst_key.status == NOT_STARTED:
                # keep track of start time/frame for later
                inst_key.tStart = t
                inst_key.frameNStart = frameN  # exact frame index
                inst_key.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if inst_key.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            #prevent loading of inst_sound for pi-0 and pi-2
            if not (inst_repeat== 0 or inst_repeat== 3):
                # start/stop inst_sound
                if t >= 0.0 and inst_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    inst_sound.tStart = t
                    inst_sound.frameNStart = frameN  # exact frame index
                    inst_sound.play()  # start the sound (it finishes automatically)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instructions"-------
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #prevent loading of inst_sound for pi-0 and pi-2
        if not (inst_repeat== 0 or inst_repeat== 3):
            inst_sound.stop()  # ensure sound has stopped at end of routine
        inst_repeat = inst_repeat+1
        # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()        
    # completed 2 repeats of 'prac_inst_loop'
    
    
    # ------Prepare to start Routine "task"-------
    t = 0
    t_0 = 0
    t_1 = 0
    taskClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(stim_duration)
    # update component parameters for each repeat
    
    # keep track of which components have finished
    taskComponents = [task_image]
    for thisComponent in taskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "task"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = taskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_image* updates
        if t >= 0.0 and task_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            task_image.tStart = t
            task_image.frameNStart = frameN  # exact frame index
            task_image.setAutoDraw(True)
        frameRemains = 0.0 + stim_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if task_image.status == STARTED and t >= frameRemains:
            task_image.setAutoDraw(False)
        
        #task trigger
        t = taskClock.getTime()
        t_1 = t
        pport.setData(int(0))
        if (t_1 - t_0) >= .500:
            pport.setData(int(prac_ttl))
            t_0 = t
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task"-------
    for thisComponent in taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    prac_relax_loop = data.TrialHandler(nReps=2, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='relax_loop')
    thisExp.addLoop(prac_relax_loop)  # add the loop to the experiment
    thisPrac_relax_loop = prac_relax_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_relax_loop.rgb)
    if thisPrac_relax_loop != None:
        for paramName in thisPrac_relax_loop.keys():
            exec(paramName + '= thisPrac_relax_loop.' + paramName)
    
    relax_repeat = 0
    for thisPrac_relax_loop in prac_relax_loop:
        currentLoop = prac_relax_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_relax_loop.rgb)
        if thisPrac_relax_loop != None:
            for paramName in thisPrac_relax_loop.keys():
                exec(paramName + '= thisPrac_relax_loop.' + paramName)
                
        # ------Prepare to start Routine "relax"-------
        t = 0
        relaxClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        relax_key = event.BuilderKeyResponse()
        relax_image.setImage("Instructions/png/r-%s.png"%(relax_repeat))
        relax_sound.setSound("Instructions/wav/r-%s.wav"%(relax_repeat))
        # keep track of which components have finished
        relaxComponents = [relax_image, relax_key, relax_sound]
        for thisComponent in relaxComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "relax"-------
        while continueRoutine:
            # get current time
            t = relaxClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *relax_image* updates
            if t >= 0.0 and relax_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                relax_image.tStart = t
                relax_image.frameNStart = frameN  # exact frame index
                relax_image.setAutoDraw(True)
            
            # *relax_key* updates
            if t >= 0.0 and relax_key.status == NOT_STARTED:
                # keep track of start time/frame for later
                relax_key.tStart = t
                relax_key.frameNStart = frameN  # exact frame index
                relax_key.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if relax_key.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            # start/stop relax_sound
            if t >= 0.0 and relax_sound.status == NOT_STARTED:
                # keep track of start time/frame for later
                relax_sound.tStart = t
                relax_sound.frameNStart = frameN  # exact frame index
                relax_sound.play()  # start the sound (it finishes automatically)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in relaxComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "relax"-------
        for thisComponent in relaxComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        relax_sound.stop()  # ensure sound has stopped at end of routine
        relax_repeat = relax_repeat+1
        # the Routine "relax" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 2 repeats of 'prac_relax_loop'

    # set up handler to look after randomisation of conditions etc
    prac_survey_loop = data.TrialHandler(nReps=7, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='survey_loop')
    thisExp.addLoop(prac_survey_loop)  # add the loop to the experiment
    thisPrac_survey_loop = prac_survey_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_survey_loop.rgb)
    if thisPrac_survey_loop != None:
        for paramName in thisPrac_survey_loop.keys():
            exec(paramName + '= thisPrac_survey_loop.' + paramName)
    #reset survey
    lsurvey = ['anger','discomfort','disgust','fear','happiness','interest','sadness']#list of questions types
    random.shuffle(lsurvey)
    print(lsurvey)
    for thisPrac_survey_loop in prac_survey_loop:
        currentLoop = prac_survey_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_survey_loop.rgb)
        if thisPrac_survey_loop != None:
            for paramName in thisPrac_survey_loop.keys():
                exec(paramName + '= thisPrac_survey_loop.' + paramName)    
    
    
        # ------Prepare to start Routine "survey"-------
        t = 0
        surveyClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        survey_key = event.BuilderKeyResponse()
        surveyType = lsurvey.pop(0)
        survey_image.setImage("Instructions/png/%s.png"%(surveyType))

        # keep track of which components have finished
        surveyComponents = [survey_image, survey_key]
        for thisComponent in surveyComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "survey"-------
        while continueRoutine:
            # get current time
            t = surveyClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *survey_image* updates
            if t >= 0.0 and survey_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                survey_image.tStart = t
                survey_image.frameNStart = frameN  # exact frame index
                survey_image.setAutoDraw(True)
            
            # *survey_key* updates
            if t >= 0.0 and survey_key.status == NOT_STARTED:
                # keep track of start time/frame for later
                survey_key.tStart = t
                survey_key.frameNStart = frameN  # exact frame index
                survey_key.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(survey_key.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if survey_key.status == STARTED:
                theseKeys = event.getKeys(keyList=numpad_list)
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if survey_key.keys == []:  # then this was the first keypress
                        survey_key.keys = theseKeys[0]  # just the first key pressed
                        survey_key.rt = survey_key.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in surveyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "survey"-------
        for thisComponent in surveyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if survey_key.keys in ['', [], None]:  # No response was made
            survey_key.keys=None
        prac_survey_loop.addData('survey_key.keys',survey_key.keys)
        if survey_key.keys != None:  # we had a response
            prac_survey_loop.addData('survey_key.rt', survey_key.rt)
        # the Routine "survey" was not non-slip safe, so reset the non-slip timer
        prac_survey_loop.addData('surveyType', surveyType)
        prac_survey_loop.addData('blockType', 'pb%s'%(prac_ttl-1))
        routineTimer.reset()
        thisExp.nextEntry()
        print(survey_key.keys)
    # completed 7 repeats of 'prac_survey_loop'
    
    # ------Prepare to start Routine "block_finish"-------
    t = 0
    block_finishClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    block_finish_key = event.BuilderKeyResponse()
    block_finish_image.setImage("Instructions/png/bf-%s.png"%(bf_repeat))
    block_finish_sound.setSound("Instructions/wav/bf-%s.wav"%(bf_repeat))
    # keep track of which components have finished
    block_finishComponents = [block_finish_image, block_finish_key, block_finish_sound]
    for thisComponent in block_finishComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "block_finish"-------
    while continueRoutine:
        # get current time
        t = block_finishClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block_finish_image* updates
        if t >= 0.0 and block_finish_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            block_finish_image.tStart = t
            block_finish_image.frameNStart = frameN  # exact frame index
            block_finish_image.setAutoDraw(True)
        
        # *block_finish_key* updates
        if t >= 0.0 and block_finish_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            block_finish_key.tStart = t
            block_finish_key.frameNStart = frameN  # exact frame index
            block_finish_key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if block_finish_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        # start/stop block_finish_sound
        if t >= 0.0 and block_finish_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            block_finish_sound.tStart = t
            block_finish_sound.frameNStart = frameN  # exact frame index
            block_finish_sound.play()  # start the sound (it finishes automatically)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_finishComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_finish"-------
    for thisComponent in block_finishComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_finish_sound.stop()  # ensure sound has stopped at end of routine
    bf_repeat = bf_repeat+1
    
    # the Routine "block_finish" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    prac_ttl = prac_ttl + 1
# completed 2 repeats of 'prac_block'
inst_repeat = 0 #reset
intro_repeat = 0 #reset

# set up handler to look after randomisation of conditions etc
task_intro_loop = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='task_intro_loop')
thisExp.addLoop(task_intro_loop)  # add the loop to the experiment
thisTask_intro_loop = task_intro_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask_intro_loop.rgb)
if thisTask_intro_loop != None:
    for paramName in thisTask_intro_loop.keys():
        exec(paramName + '= thisTask_intro_loop.' + paramName)

for thisTask_intro_loop in task_intro_loop:
    currentLoop = task_intro_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTask_intro_loop.rgb)
    if thisTask_intro_loop != None:
        for paramName in thisTask_intro_loop.keys():
            exec(paramName + '= thisTask_intro_loop.' + paramName)
    
    # ------Prepare to start Routine "task_introduction"-------
    t = 0
    task_introductionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    task_intro_key = event.BuilderKeyResponse()
    task_intro_image.setImage("Instructions/png/tintro-%s.png"%(intro_repeat))
    task_intro_sound.setSound("Instructions/wav/tintro-%s.wav"%(intro_repeat))
    # keep track of which components have finished
    task_introductionComponents = [task_intro_image, task_intro_key, task_intro_sound]
    for thisComponent in task_introductionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "task_introduction"-------
    while continueRoutine:
        # get current time
        t = task_introductionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_intro_image* updates
        if t >= 0.0 and task_intro_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            task_intro_image.tStart = t
            task_intro_image.frameNStart = frameN  # exact frame index
            task_intro_image.setAutoDraw(True)
        
        # *task_intro_key* updates
        if t >= 0.0 and task_intro_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            task_intro_key.tStart = t
            task_intro_key.frameNStart = frameN  # exact frame index
            task_intro_key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if task_intro_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        # start/stop task_intro_sound
        if t >= 0.0 and task_intro_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            task_intro_sound.tStart = t
            task_intro_sound.frameNStart = frameN  # exact frame index
            task_intro_sound.play()  # start the sound (it finishes automatically)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_introductionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task_introduction"-------
    for thisComponent in task_introductionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    task_intro_sound.stop()  # ensure sound has stopped at end of routine
    intro_repeat = intro_repeat+1
    # the Routine "task_introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
# completed 5 repeats of 'task_intro_loop'


# set up handler to look after randomisation of conditions etc
task_block = data.TrialHandler(nReps=4, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(task_block)  # add the loop to the experiment
thisTask_block = task_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask_block.rgb)
if thisTask_block != None:
    for paramName in thisTask_block.keys():
        exec(paramName + '= thisTask_block.' + paramName)

#---------------block loop
#create block list and shuffle
#list of block types, instruction slides, and ttls
lblockType = [['b0',7,3],['b1',6,4],['b2',7,5],['b3',8,6]] 
random.shuffle(lblockType)
blockNum=0 #block counter
for thisTask_block in task_block:
    #get block type then pop list
    blockType = lblockType.pop(0)
    #get ttl
    ttlNum = blockType[2]
    #print
    print 'blockType:',blockType[0]
    print 'blockNum:',blockNum
    #loop
    currentLoop = task_block
    # abbreviate parameter names if possible (e.g. rgb = thisTask_block.rgb)
    if thisTask_block != None:
        for paramName in thisTask_block.keys():
            exec(paramName + '= thisTask_block.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    task_inst_loop = data.TrialHandler(nReps=blockType[1], method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='inst_loop')
    thisExp.addLoop(task_inst_loop)  # add the loop to the experiment
    thisTask_inst_loop = task_inst_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTask_inst_loop.rgb)
    if thisTask_inst_loop != None:
        for paramName in thisTask_inst_loop.keys():
            exec(paramName + '= thisTask_inst_loop.' + paramName)
    
    inst_repeat = 0
    #---------------task instructions loop
    for thisTask_inst_loop in task_inst_loop:
        currentLoop = task_inst_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTask_inst_loop.rgb)
        if thisTask_inst_loop != None:
            for paramName in thisTask_inst_loop.keys():
                exec(paramName + '= thisTask_inst_loop.' + paramName)
        
        # ------Prepare to start Routine "instructions"-------
        t = 0
        instructionsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        inst_key = event.BuilderKeyResponse()
        inst_image.setImage("Instructions/png/%s-%s.png"%(blockType[0],inst_repeat))
        #prevent loading of inst_sound for first slide
        if not (inst_repeat== 0):
            inst_sound.setSound("Instructions/wav/%s-%s.wav"%(blockType[0],inst_repeat))
            instructionsComponents = [inst_image, inst_key, inst_sound]
        else:
            instructionsComponents = [inst_image, inst_key]            
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instructions"-------
        while continueRoutine:
            # get current time
            t = instructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inst_image* updates
            if t >= 0.0 and inst_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                inst_image.tStart = t
                inst_image.frameNStart = frameN  # exact frame index
                inst_image.setAutoDraw(True)
            
            # *inst_key* updates
            if t >= 0.0 and inst_key.status == NOT_STARTED:
                # keep track of start time/frame for later
                inst_key.tStart = t
                inst_key.frameNStart = frameN  # exact frame index
                inst_key.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if inst_key.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            #prevent loading of inst_sound for first slide            
            if not (inst_repeat== 0):
                # start/stop inst_sound
                if t >= 0.0 and inst_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    inst_sound.tStart = t
                    inst_sound.frameNStart = frameN  # exact frame index
                    inst_sound.play()  # start the sound (it finishes automatically)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instructions"-------
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #prevent loading of inst_sound for first slide
        if not (inst_repeat== 0):
            inst_sound.stop()  # ensure sound has stopped at end of routine
        inst_repeat = inst_repeat+1
        # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
    # completed 5 repeats of 'task_inst_loop'
    
    
    # ------Prepare to start Routine "task"-------
    t = 0
    t_0 = 0
    t_1 = 0
    taskClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(stim_duration)
    # update component parameters for each repeat
    
    # keep track of which components have finished
    taskComponents = [task_image]
    for thisComponent in taskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "task"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = taskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_image* updates
        if t >= 0.0 and task_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            task_image.tStart = t
            task_image.frameNStart = frameN  # exact frame index
            task_image.setAutoDraw(True)
        frameRemains = 0.0 + stim_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if task_image.status == STARTED and t >= frameRemains:
            task_image.setAutoDraw(False)
        #task trigger
        t = taskClock.getTime()
        t_1 = t
        pport.setData(int(0))
        if (t_1 - t_0) >= .500:
            pport.setData(int(ttlNum))
            t_0 = t
            
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task"-------
    for thisComponent in taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # set up handler to look after randomisation of conditions etc
    task_relax_loop = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='relax_loop')
    thisExp.addLoop(task_relax_loop)  # add the loop to the experiment
    thisTask_relax_loop = task_relax_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTask_relax_loop.rgb)
    if thisTask_relax_loop != None:
        for paramName in thisTask_relax_loop.keys():
            exec(paramName + '= thisTask_relax_loop.' + paramName)
    
    relax_repeat = 0
    for thisTask_relax_loop in task_relax_loop:
        currentLoop = task_relax_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTask_relax_loop.rgb)
        if thisTask_relax_loop != None:
            for paramName in thisTask_relax_loop.keys():
                exec(paramName + '= thisTask_relax_loop.' + paramName)
        
        # ------Prepare to start Routine "relax"-------
        t = 0
        relaxClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        relax_key = event.BuilderKeyResponse()
        relax_image.setImage("Instructions/png/r-%s.png"%(relax_repeat))
        relax_sound.setSound("Instructions/wav/r-%s.wav"%(relax_repeat))
        # keep track of which components have finished
        relaxComponents = [relax_image, relax_key, relax_sound]
        for thisComponent in relaxComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED    
    
        # ------Prepare to start Routine "relax"-------
        t = 0
        relaxClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        relax_key = event.BuilderKeyResponse()
        relax_image.setImage("Instructions/png/r-%s.png"%(relax_repeat))
        relax_sound.setSound("Instructions/wav/r-%s.wav"%(relax_repeat))
        # keep track of which components have finished
        relaxComponents = [relax_image, relax_key, relax_sound]
        for thisComponent in relaxComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "relax"-------
        while continueRoutine:
            # get current time
            t = relaxClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *relax_image* updates
            if t >= 0.0 and relax_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                relax_image.tStart = t
                relax_image.frameNStart = frameN  # exact frame index
                relax_image.setAutoDraw(True)
            
            # *relax_key* updates
            if t >= 0.0 and relax_key.status == NOT_STARTED:
                # keep track of start time/frame for later
                relax_key.tStart = t
                relax_key.frameNStart = frameN  # exact frame index
                relax_key.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if relax_key.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            # start/stop relax_sound
            if t >= 0.0 and relax_sound.status == NOT_STARTED:
                # keep track of start time/frame for later
                relax_sound.tStart = t
                relax_sound.frameNStart = frameN  # exact frame index
                relax_sound.play()  # start the sound (it finishes automatically)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in relaxComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "relax"-------
        for thisComponent in relaxComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        relax_sound.stop()  # ensure sound has stopped at end of routine
        relax_repeat = relax_repeat+1
        # the Routine "relax" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    task_survey_loop = data.TrialHandler(nReps=7, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='survey_loop')
    thisExp.addLoop(task_survey_loop)  # add the loop to the experiment
    thisTask_survey_loop = task_survey_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTask_survey_loop.rgb)
    if thisTask_survey_loop != None:
        for paramName in thisTask_survey_loop.keys():
            exec(paramName + '= thisTask_survey_loop.' + paramName)
    #reset survey
    lsurvey = ['anger','discomfort','disgust','fear','happiness','interest','sadness']#list of questions types
    random.shuffle(lsurvey)
    print(lsurvey)
    for thisTask_survey_loop in task_survey_loop:
        currentLoop = task_survey_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTask_survey_loop.rgb)
        if thisTask_survey_loop != None:
            for paramName in thisTask_survey_loop.keys():
                exec(paramName + '= thisTask_survey_loop.' + paramName)
    
        # ------Prepare to start Routine "survey"-------
        t = 0
        surveyClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        surveyType = lsurvey.pop(0)
        survey_image.setImage("Instructions/png/%s.png"%(surveyType))
        survey_key = event.BuilderKeyResponse()
        # keep track of which components have finished
        surveyComponents = [survey_image, survey_key]
        for thisComponent in surveyComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "survey"-------
        while continueRoutine:
            # get current time
            t = surveyClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *survey_image* updates
            if t >= 0.0 and survey_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                survey_image.tStart = t
                survey_image.frameNStart = frameN  # exact frame index
                survey_image.setAutoDraw(True)
            
            # *survey_key* updates
            if t >= 0.0 and survey_key.status == NOT_STARTED:
                # keep track of start time/frame for later
                survey_key.tStart = t
                survey_key.frameNStart = frameN  # exact frame index
                survey_key.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(survey_key.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if survey_key.status == STARTED:
                theseKeys = event.getKeys(keyList=numpad_list)
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if survey_key.keys == []:  # then this was the first keypress
                        survey_key.keys = theseKeys[0]  # just the first key pressed
                        survey_key.rt = survey_key.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in surveyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "survey"-------
        for thisComponent in surveyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if survey_key.keys in ['', [], None]:  # No response was made
            survey_key.keys=None
        task_survey_loop.addData('survey_key.keys',survey_key.keys)
        if survey_key.keys != None:  # we had a response
            task_survey_loop.addData('survey_key.rt', survey_key.rt)
        # the Routine "survey" was not non-slip safe, so reset the non-slip timer
        task_survey_loop.addData('surveyType', surveyType)
        task_survey_loop.addData('blockType', blockType[0])
        routineTimer.reset()
        thisExp.nextEntry()
        print(survey_key.keys)  
    blockNum = blockNum + 1
# completed 5 repeats of 'task_block'


# ------Prepare to start Routine "Finish"-------
t = 0
FinishClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
finish_sound.setSound("Instructions/wav/finish-0.wav")
# keep track of which components have finished
FinishComponents = [finish_image, finish_sound]
for thisComponent in FinishComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Finish"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FinishClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finish_image* updates
    if t >= 0.0 and finish_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        finish_image.tStart = t
        finish_image.frameNStart = frameN  # exact frame index
        finish_image.setAutoDraw(True)
    frameRemains = 0.0 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if finish_image.status == STARTED and t >= frameRemains:
        finish_image.setAutoDraw(False)
    # start/stop finish_sound
    if t >= 0.0 and finish_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        finish_sound.tStart = t
        finish_sound.frameNStart = frameN  # exact frame index
        finish_sound.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finish"-------
for thisComponent in FinishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
finish_sound.stop()  # ensure sound has stopped at end of routine

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
