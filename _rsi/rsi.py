#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on January 14, 2017, at 14:32
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, FINISHED)
import os  # handy system and path functions
import sys  # to get file system encoding

#imports
from psychopy import parallel
#constants 
pport = parallel.ParallelPort(address='0xDFF8')
pport.setData(int(0))
stim_duration = 60
#ttl - open = 7; closed = 8
lodd =  [['ro-0',7,'open'],['rc-1',8,'closed'],['rc-2',8,'closed'],['ro-2',7,'open'],['rc-3',8,'closed'],['ro-3',7,'open'],['ro-3',7,'open'],['rc-3',8,'closed']]
leven = [['rc-0',8,'closed'],['ro-1',7,'open'],['ro-2',7,'open'],['rc-2',8,'closed'],['ro-3',7,'open'],['rc-3',8,'closed'],['rc-3',8,'closed'],['ro-3',7,'open']]

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'RSI'  # from the Builder filename that created this script
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


#check if participant is even or odd #then run cooresponding task
subjectNum = int(expInfo['participant'])
if subjectNum % 2 == 0:
    sub_even = True
    lblockOrder = leven
    conditionType = 'even'
    print(lblockOrder)
else:
    sub_even = False
    lblockOrder = lodd
    conditionType = 'odd'
    print(lblockOrder)
    

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
    image="Instructions/png/r-start.png", mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
intro_sound = sound.Sound("Instructions/wav/r-start.wav")
intro_sound.setVolume(1)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
inst_image = visual.ImageStim(
    win=win, name='inst_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
inst_sound = sound.Sound('A', secs=-1)
inst_sound.setVolume(1)
inst_repeat = 0

# Initialize components for Routine "ready"
readyClock = core.Clock()
ready_image = visual.ImageStim(
    win=win, name='ready_image',
    image="Instructions/png/r-ready.png", mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ready_sound = sound.Sound("Instructions/wav/r-ready.wav")
ready_sound.setVolume(1)

# Initialize components for Routine "task"
taskClock = core.Clock()
task_image = visual.ImageStim(
    win=win, name='task_image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "Finish"
FinishClock = core.Clock()
finish_image = visual.ImageStim(
    win=win, name='finish_image',
    image="Instructions/png/r-finished.png", mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
finish_sound = sound.Sound("Instructions/wav/r-finished.wav")
finish_sound.setVolume(1)


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction"-------
t = 0
introductionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
intro_key = event.BuilderKeyResponse()
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
        win.callOnFlip(intro_key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if intro_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            intro_key.keys = theseKeys[-1]  # just the last key pressed
            intro_key.rt = intro_key.clock.getTime()
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
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=8, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
        
    #prepare block type
    lblock_info = lblockOrder.pop(0)
    blockImage = lblock_info[0]
    ttlNum  = lblock_info[1]
    blockType = lblock_info[2] 
    
    # ------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    inst_key = event.BuilderKeyResponse()
    inst_image.setImage("Instructions/png/%s.png"%(blockImage))
    inst_sound.setSound("Instructions/wav/%s.wav"%(blockImage))
    # keep track of which components have finished
    instructionsComponents = [inst_image, inst_key, inst_sound]
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
            win.callOnFlip(inst_key.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if inst_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                inst_key.keys = theseKeys[-1]  # just the last key pressed
                inst_key.rt = inst_key.clock.getTime()
                # a response ends the routine
                continueRoutine = False
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
    # check responses
    if inst_key.keys in ['', [], None]:  # No response was made
        inst_key.keys=None
    block.addData('inst_key.keys',inst_key.keys)
    if inst_key.keys != None:  # we had a response
        block.addData('inst_key.rt', inst_key.rt)
    inst_sound.stop()  # ensure sound has stopped at end of routine
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "ready"-------
    t = 0
    readyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ready_key = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    readyComponents = [ready_image, ready_key, ready_sound]
    for thisComponent in readyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ready"-------
    while continueRoutine:
        # get current time
        t = readyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ready_image* updates
        if t >= 0.0 and ready_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            ready_image.tStart = t
            ready_image.frameNStart = frameN  # exact frame index
            ready_image.setAutoDraw(True)
        
        # *ready_key* updates
        if t >= 0.0 and ready_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            ready_key.tStart = t
            ready_key.frameNStart = frameN  # exact frame index
            ready_key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(ready_key.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if ready_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                ready_key.keys = theseKeys[-1]  # just the last key pressed
                ready_key.rt = ready_key.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        # start/stop ready_sound
        if t >= 0.0 and ready_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            ready_sound.tStart = t
            ready_sound.frameNStart = frameN  # exact frame index
            ready_sound.play()  # start the sound (it finishes automatically)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in readyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ready"-------
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if ready_key.keys in ['', [], None]:  # No response was made
        ready_key.keys=None
    block.addData('ready_key.keys',ready_key.keys)
    if ready_key.keys != None:  # we had a response
        block.addData('ready_key.rt', ready_key.rt)
    ready_sound.stop()  # ensure sound has stopped at end of routine
    
    # the Routine "ready" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()    
    
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
    
    #prepare outputs
    block.addData('condition', conditionType)#output condition (even,odd)
    block.addData('blockType', blockType)#output block_type (open,closed)
    block.addData('blockImage', blockImage)#output block_type (open,closed)
    block.addData('TTL', ttlNum)#TTL (7,8)
    thisExp.nextEntry()  
# completed 8 repeats of 'block'


# ------Prepare to start Routine "Finish"-------
t = 0
FinishClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat

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
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if finish_image.status == STARTED and t >= frameRemains:
        finish_image.setAutoDraw(False)
    # start/stop finish_sound
    if t >= 0.0 and finish_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        finish_sound.tStart = t
        finish_sound.frameNStart = frameN  # exact frame index
        finish_sound.play()  # start the sound (it finishes automatically)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if finish_sound.status == STARTED and t >= frameRemains:
        finish_sound.stop()  # stop the sound (if longer than duration)
    
    
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

# the Routine "Finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
