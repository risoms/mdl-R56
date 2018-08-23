#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was partially created using PsychoPy2 Experiment Builder (v1.83.04), Tue Feb 23 13:01:04 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui, parallel
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding
import random
from pdb import set_trace as breakpoint

locations = ((0, 256), (256, 0), (0, -256), (-256, 0))
number_texts = []
NUM_IMAGES = 20
MALE = 0
FEMALE = 1
NUM_BLOCKS = 3
sad_male_images = []
sad_male_images = sad_male_images*int(180/20)
neutral_male_images = []
neutral_male_images = neutral_male_images*int(180/20)
sad_female_images = []
sad_female_images = sad_female_images*int(180/20)
neutral_female_images = []
neutral_female_images = neutral_female_images*int(180/20)
corr_answer = 1*16 #equal to R1 in PyCorder
incorrect_answer = 2*16 #equal to R2 in PyCorder
no_answer = 3*16 #equal to R3 in PyCorder

def choose_male_images():
    my_faces = []
    my_faces.extend(np.random.choice(sad_male_images, 2, False))
    my_faces.extend(np.random.choice(neutral_male_images, 2, False))
    random.shuffle(my_faces)
    for i in range(len(my_faces)):
        my_faces[i].setPos(newPos = locations[i])
        thisExp.addData("Image" + str(i) + " _Position", my_faces[i].name)
    return my_faces
    
def choose_female_images():
    my_faces = []
    my_faces.extend(np.random.choice(sad_female_images, 2,False))
    my_faces.extend(np.random.choice(neutral_female_images, 2,False))
    random.shuffle(my_faces)
    for i in range(len(my_faces)):
        my_faces[i].setPos(newPos = locations[i])
        thisExp.addData("Image" + str(i) + " _Position", my_faces[i].name)
    return my_faces
    
def get_all_images(win):
    path_to_images = "stim/"
    #white male = sad male
    for i in range(NUM_IMAGES):
        file = path_to_images + "AMSA" + "%02d" %(i + 1) + ".jpg"
        name = "AMSA" + "%02d" %(i + 1) + ".jpg"
        sad_male_images.append(visual.ImageStim(win=win, name=name,units='pix', 
    image=file, mask=None,
    ori=0, pos=[0, 3.2], size=[128, 128],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0))
    #black male = neutral male   
    for i in range(NUM_IMAGES):
        file = path_to_images + "AMNE" + "%02d" %(i + 1) + ".jpg"
        name = "AMNE" + "%02d" %(i + 1) + ".jpg"
        neutral_male_images.append(visual.ImageStim(win=win, name=name,units='pix', 
    image=file, mask=None,
    ori=0, pos=[0, 3.2], size=[128, 128],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0))
    #white female = sad female
    for i in range(NUM_IMAGES):
        file = path_to_images + "AFSA" + "%02d" %(i + 1) + ".jpg"
        name = "AFSA" + "%02d" %(i + 1) + ".jpg"
        sad_female_images.append(visual.ImageStim(win=win, name=name,units='pix', 
    image=file, mask=None,
    ori=0, pos=[0, 3.2], size=[128, 128],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0))
    #black female  = neutral female    
    for i in range(NUM_IMAGES):
        file = path_to_images + "AFNE" + "%02d" %(i + 1) + ".jpg"
        name = "AFNE" + "%02d" %(i + 1) + ".jpg"
        neutral_female_images.append(visual.ImageStim(win=win, name=name,units='pix', 
    image=file, mask=None,
    ori=0, pos=[0, 3.2], size=[128, 128],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0))
    
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'MAFE4ImagesEEG'  # from the Builder filename that created this script
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
print ('subject:',expInfo['participant'])
print ('exp:',expName)
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data\%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=False, screen=0,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    allowGUI=False, allowStencil=False, blendMode='avg', useFBO=True)

# Get all the images
get_all_images(win)

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instr"
InstrClock = core.Clock()
Instructions = visual.TextStim(win=win, ori=0, name='Instructions',
    text='You will be presented with an array of 4 faces; afterwards you will be presented with a face cue in the center of the screen.\n\nYour task is to indicate the location of the face cue in the previous array by pressing the correct location number (1-4) on the labeled keys.\n\nPlease keep your EYES FIXATED ON THE CROSS.\nPlease use your DOMINANT hand to respond as quickly and accurately as possible.\n\nYou will start with a practice session.\nPlease press the spacebar to continue.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create the 4 numbers
for i in range(4):
    number_texts.append(visual.TextStim(win=win, ori=0, name='Number' + str(i+1), units='pix',
    text=str(i+1),    font='Arial',
    pos=locations[i], height=2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0))

# Initialize components for Routine "Continue"
ContinueClock = core.Clock()
Ready = visual.TextStim(win=win, ori=0, name='Ready',
    text='That was the end of the block.\n\nIf you need to take a break please do so now.\n\nWhen you are ready to continue please press the spacebar and remember to KEEP YOUR EYES FIXATED ON THE CROSS.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
FixationPoint = visual.TextStim(win=win, ori=0, name='FixationPoint',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
p_port = parallel.ParallelPort(address=u'0xDFF8')
p_port_images = parallel.ParallelPort(address=u'0xDFF8')

# Initialize components for Routine "Break"
BreakClock = core.Clock()
Break = visual.TextStim(win=win, ori=0, name='Break',
    text='That was the end of the block.\n\nIf you need to take a break please take one now.\n\nWhen you are ready to continue please press the spacebar.',  font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Instr"-------
t = 0
InstrClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
InstrKey_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
InstrKey_resp.status = NOT_STARTED
# keep track of which components have finished
InstrComponents = []
InstrComponents.append(Instructions)
InstrComponents.append(InstrKey_resp)
for thisComponent in InstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instr"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if t >= 0.0 and Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions.tStart = t  # underestimates by a little under one frame
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.setAutoDraw(True)
    if Instructions.status == STARTED:  # only update if being drawn
        Instructions.setColor('white', colorSpace='rgb', log=False)
    
    # *InstrKey_resp* updates
    if t >= 0.0 and InstrKey_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrKey_resp.tStart = t  # underestimates by a little under one frame
        InstrKey_resp.frameNStart = frameN  # exact frame index
        InstrKey_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(InstrKey_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if InstrKey_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            InstrKey_resp.keys = theseKeys[-1]  # just the last key pressed
            InstrKey_resp.rt = InstrKey_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instr"-------
for thisComponent in InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if InstrKey_resp.keys in ['', [], None]:  # No response was made
   InstrKey_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('InstrKey_resp.keys',InstrKey_resp.keys)
if InstrKey_resp.keys != None:  # we had a response
    thisExp.addData('InstrKey_resp.rt', InstrKey_resp.rt)
thisExp.nextEntry()
# the Routine "Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


#-------Starting Practice Trials-------#
# Each trial executes this function
def execute_trial(name, gender):
    endExpNow = False
    if gender == MALE:
        conditions_file = data.importConditions(u'MalePracticeFile.csv')
    else:
        conditions_file = data.importConditions(u'FemalePracticeFile.csv')

    # set up handler to look after randomisation of conditions etc
    Trials = data.TrialHandler(nReps=1, method='random', extraInfo=expInfo, originPath="-1", trialList=conditions_file, seed=None, name=name)
    thisExp.addLoop(Trials)  # add the loop to the experiment
    thisTrials = Trials.trialList[0]  # so we can initialise stimuli with some values

    # abbreviate parameter names if possible (e.g. rgb=thisTrialsF1.rgb)


    for thisTrials in Trials:
        currentLoop = Trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsF1.rgb)
        #if thisTrials != None:
        #    for paramName in thisTrials.keys():
        #        exec(paramName + "= thisTrials." + paramName)

        #------Prepare to start Routine "Trial"-------
        t = 0
        TrialClock.reset()  # clock 
        frameN = -1
        routineTimer.add(8.500000)

        # update component parameters for each repeat
        FixationPoint.setColor('white', colorSpace='rgb')
        for number in number_texts:
            number.setColor('white', colorSpace='rgb') #Numbers & color of numbers
        Key_Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Key_Resp.status = NOT_STARTED

        # Get the random images
        if gender == MALE:
            random_images = choose_male_images()
        else:
            random_images = choose_female_images()
        Image1 = random_images[0]
        Image2 = random_images[1]
        Image3 = random_images[2]
        Image4 = random_images[3]
        print('image 1: %s'%(Image1))

        #Choose center image & Add to file
        center_image = random.choice(random_images)
        thisExp.addData('Center_image', center_image.name)
        
        #Code
        print(str(center_image.name[1:3]))
        if str(center_image.name[1:3]) == 'MN':
            code = '1'
        #white male = sad male
        elif str(center_image.name[1:3]) == 'MS':
            code = '2'
        #black female = neutral female   
        elif str(center_image.name[1:3]) == 'FN':
            code = '3'
        #white female = sad female
        else:
            code = '4'

        #Adding Condition Column to Data File
        thisExp.addData('condition', center_image.name[1:3])
        #Adding Code Column to Data File
        thisExp.addData('code', code)
        
        #Correct Answer
        if center_image == Image1:
            correct_answer = 'num_8'
        elif center_image == Image2:
            correct_answer = 'num_6'
        elif center_image == Image3:
            correct_answer = 'num_2'
        elif center_image == Image4:
            correct_answer = 'num_4'
        else:
            correct_answer = 'None'
        print('image1: %s'%(Image1.image))
        print('Image2: %s'%(Image2.image))
        print('Image3: %s'%(Image3.image))
        print('Image4: %s'%(Image4.image))
        print('center_image: %s'%(center_image.image))
        print('correct_answer: %s'%(correct_answer))
        
        
        #Adding Correct Answer Column to Data File
        thisExp.addData('correct_answer', correct_answer)
        
        # keep track of which components have finished
        TrialComponents = []
        TrialComponents.append(FixationPoint)
        TrialComponents.append(Image1)
        TrialComponents.append(Image2)
        TrialComponents.append(Image3)
        TrialComponents.append(Image4)
        TrialComponents.append(center_image)
        TrialComponents.append(p_port) #Adding port
        TrialComponents.append(p_port_images) #Adding images port
        
        for number in number_texts:
            TrialComponents.append(number)
        TrialComponents.append(Key_Resp)

        for thisComponent in TrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
    #-------Start Routine "Trial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = TrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *FixationPoint* updates
            if t >= 0.0 and FixationPoint.status == NOT_STARTED:
                # keep track of start time/frame for later
                FixationPoint.tStart = t  # underestimates by a little under one frame
                FixationPoint.frameNStart = frameN  # exact frame index
                FixationPoint.setAutoDraw(True)
            if FixationPoint.status == STARTED and t >= (0.0 + (8.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            #if FixationPoint.status == STARTED and t >= 0: 
                FixationPoint.setAutoDraw(False)

            #Random Images
            if t >= 0.5 and random_images[0].status == NOT_STARTED:
                for image in random_images:
                    # keep track of start time/frame for later
                    image.tStart = t  # underestimates by a little under one frame
                    image.frameNStart = frameN  # exact frame index
                    image.setAutoDraw(True)
            if random_images[0].status == STARTED and t >= 2.0 and t < 3.0: #most of one frame period left
                for image in random_images:
                    image.setAutoDraw(False)
            # *p_port_images* updates
            if t >= 0.5 and p_port_images.status == NOT_STARTED:
            # keep track of start time/frame for later
                p_port_images.tStart = t  # underestimates by a little under one frame
                p_port_images.frameNStart = frameN  # exact frame index
                p_port_images.status = STARTED
                win.callOnFlip(p_port_images.setData, int(14))
            if p_port_images.status == STARTED and t >= (2.0-win.monitorFramePeriod*0.75): #most of one frame period left
                breakpoint() #TODO!
                p_port_images.status = STOPPED
                win.callOnFlip(p_port_images.setData, int(15))
            
            # *Numbers* updates
            if t >= 3.5 and number_texts[0].status == NOT_STARTED:
                for number in number_texts:
                    number.tStart = t  # underestimates by a little under one frame
                    number.frameNStart = frameN  # exact frame index
                    number.setAutoDraw(True)
            if number_texts[0].status == STARTED and t >= 8.5: #most of one frame period left
                for number in number_texts:
                    number.setAutoDraw(False)
            
            # *Key_Resp* updates
            if t >= 3.5 and Key_Resp.status == NOT_STARTED:
                center_image.setPos(newPos = (0, 0))
                center_image.setAutoDraw(True)

                # keep track of start time/frame for later
                Key_Resp.tStart = t  # underestimates by a little under one frame
                Key_Resp.frameNStart = frameN  # exact frame index
                Key_Resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Key_Resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            
            if Key_Resp.status == STARTED and t >= 8.5: #most of one frame period left
                Key_Resp.status = STOPPED
                center_image.setAutoDraw(False)
            if Key_Resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['num_8', 'num_6', 'num_2', 'num_4'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                accuracy = 0
                if len(theseKeys) > 0:  # at least one key was pressed
                    Key_Resp.keys = theseKeys[-1]  # just the last key pressed
                    Key_Resp.rt = Key_Resp.clock.getTime()
                    print('resp')
                    #Check for Correct or Incorrect
                    if (correct_answer == str(Key_Resp.keys)) or (correct_answer == Key_Resp.keys):
                        accuracy = corr_answer						
                    elif Key_Resp.keys in ['', [], None]:
                        accuracy = no_answer
                    else:
                        accuracy = incorrect_answer
                    # a response ends the routine
                    continueRoutine = False
                # *p_port* updates
                if t >= 3.5 and p_port.status == NOT_STARTED:
                # keep track of start time/frame for later
                    p_port.tStart = t  # underestimates by a little under one frame
                    p_port.frameNStart = frameN  # exact frame index
                    p_port.status = STARTED
                    win.callOnFlip(p_port.setData, int(code))
                if p_port.status == STARTED and t >= (8.5-win.monitorFramePeriod*0.75): #most of one frame period left
                    p_port.status = STOPPED
                    win.callOnFlip(p_port.setData, int(0))
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Trial"-------
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Key_Resp.keys in ['', [], None]:  # No response was made
           Key_Resp.keys=None
        
        #Adding Accuracy Column to Data File
        if (correct_answer == str(Key_Resp.keys)) or (correct_answer == Key_Resp.keys):
            accuracy = corr_answer
        elif Key_Resp.keys in ['', [], None]:
            accuracy = no_answer
        else:
            accuracy = incorrect_answer
        thisExp.addData('accuracy', accuracy)
        
        # store data for TrialsF1 (TrialHandler)
        Trials.addData('Key_Resp.keys',Key_Resp.keys)
        if p_port_images.status == STARTED:
            win.callOnFlip(p_port_images.setData, int(0))
        if Key_Resp.keys != None:  # we had a response
            Trials.addData('Key_Resp.rt', Key_Resp.rt)
        if p_port.status == STARTED:
            win.callOnFlip(p_port.setData, int(accuracy))
        thisExp.nextEntry()


for t in range(NUM_BLOCKS):
    print(MALE)
    print(FEMALE)
    execute_trial("TrialsM" + str(t+1), MALE)
    execute_trial("TrialsF" + str(t+1), FEMALE)
#Change order to change Male/Female blocks
# completed 1 repeats of 'practice'



#----------Starting Actual Trials---------#
# Each trial executes this function
def execute_trial(name, gender):
    endExpNow = False
    if gender == MALE:
        conditions_file = data.importConditions(u'EmotionMaConditionsFile.csv')
    else:
        conditions_file = data.importConditions(u'EmotionFeConditionsFile.csv')

    # set up handler to look after randomisation of conditions etc
    Trials = data.TrialHandler(nReps=6, method='random', #CHANGE NUMBER OF REPS
        extraInfo=expInfo, originPath="-1",
        trialList=conditions_file,
        seed=None, name=name)
    thisExp.addLoop(Trials)  # add the loop to the experiment
    thisTrials = Trials.trialList[0]  # so we can initialise stimuli with some values

    # abbreviate parameter names if possible (e.g. rgb=thisTrialsF1.rgb)
    if thisTrials != None:
        for paramName in thisTrials.keys():
            exec(paramName + "= thisTrials." + paramName)

    for thisTrials in Trials:
        currentLoop = Trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsF1.rgb)
        if thisTrials != None:
            for paramName in thisTrials.keys():
                exec(paramName + "= thisTrials." + paramName)
        
        #------Prepare to start Routine "Trial"-------
        t = 0
        TrialClock.reset()  # clock 
        frameN = -1
        routineTimer.add(8.500000)

        # update component parameters for each repeat
        FixationPoint.setColor('white', colorSpace='rgb')
        for number in number_texts:
            number.setColor('white', colorSpace='rgb')
        Key_Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Key_Resp.status = NOT_STARTED

        # Get the random images
        if gender == MALE:
            random_images = choose_male_images()
        else:
            random_images = choose_female_images()
        Image1 = random_images[0]
        Image2 = random_images[1]
        Image3 = random_images[2]
        Image4 = random_images[3]
        
        #Choose center image & Add to file
        center_image = random.choice(random_images)
        thisExp.addData('Center_image', center_image.name)
        
        #Code
        print(str(center_image.name[1:3]))
        if str(center_image.name[1:3]) == 'MN':
            code = '1'
        #white male = sad male
        elif str(center_image.name[1:3]) == 'MS':
            code = '2'
        #black female = neutral female   
        elif str(center_image.name[1:3]) == 'FN':
            code = '3'
        #white female = sad female
        else:
            code = '4'

        #Adding Condition Column to Data File
        thisExp.addData('condition', center_image.name[1:3])
        #Adding Code Column to Data File
        thisExp.addData('code', code)
        
        #Correct Answer
        if center_image == Image1:
            correct_answer = 'num_8'
        elif center_image == Image2:
            correct_answer = 'num_6'
        elif center_image == Image3:
            correct_answer = 'num_2'
        elif center_image == Image4:
            correct_answer = 'num_4'
        else:
            correct_answer = 'None'
        #Adding Correct Answer Column to Data File
        thisExp.addData('correct_answer', correct_answer)

        # keep track of which components have finished
        TrialComponents = []
        TrialComponents.append(FixationPoint)
        TrialComponents.append(Image1)
        TrialComponents.append(Image2)
        TrialComponents.append(Image3)
        TrialComponents.append(Image4)
        TrialComponents.append(center_image)
        TrialComponents.append(p_port)
        TrialComponents.append(p_port_images)
        
        for number in number_texts:
            TrialComponents.append(number)
        TrialComponents.append(Key_Resp)

        for thisComponent in TrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Trial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = TrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *FixationPoint* updates
            if t >= 0.0 and FixationPoint.status == NOT_STARTED:
                # keep track of start time/frame for later
                FixationPoint.tStart = t  # underestimates by a little under one frame
                FixationPoint.frameNStart = frameN  # exact frame index
                FixationPoint.setAutoDraw(True)
            if FixationPoint.status == STARTED and t >= (0.0 + (8.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            #if FixationPoint.status == STARTED and t >= 0: 
                FixationPoint.setAutoDraw(False)

            #Random Images
            if t >= 0.5 and random_images[0].status == NOT_STARTED:
                for image in random_images:
                    # keep track of start time/frame for later
                    image.tStart = t  # underestimates by a little under one frame
                    image.frameNStart = frameN  # exact frame index
                    image.setAutoDraw(True)
            if random_images[0].status == STARTED and t >= 2.0 and t < 3.0: #most of one frame period left
                for image in random_images:
                    image.setAutoDraw(False)
            # *p_port_images* updates
            if t >= 0.5 and p_port_images.status == NOT_STARTED:
            # keep track of start time/frame for later
                p_port_images.tStart = t  # underestimates by a little under one frame
                p_port_images.frameNStart = frameN  # exact frame index
                p_port_images.status = STARTED
                win.callOnFlip(p_port_images.setData, int(14))
            if p_port_images.status == STARTED and t >= (2.0-win.monitorFramePeriod*0.75): #most of one frame period left
                p_port_images.status = STOPPED
                win.callOnFlip(p_port_images.setData, int(15))

            # *Numbers* updates
            if t >= 3.5 and number_texts[0].status == NOT_STARTED:
                for number in number_texts:
                    number.tStart = t  # underestimates by a little under one frame
                    number.frameNStart = frameN  # exact frame index
                    number.setAutoDraw(True)
            if number_texts[0].status == STARTED and t >= 8.5: #most of one frame period left
                for number in number_texts:
                    number.setAutoDraw(False)
            
            # *Key_Resp* updates
            if t >= 3.5 and Key_Resp.status == NOT_STARTED:
                center_image.setPos(newPos = (0, 0))
                center_image.setAutoDraw(True)

                # keep track of start time/frame for later
                Key_Resp.tStart = t  # underestimates by a little under one frame
                Key_Resp.frameNStart = frameN  # exact frame index
                Key_Resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Key_Resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            
            if Key_Resp.status == STARTED and t >= 8.5: #most of one frame period left
                Key_Resp.status = STOPPED
                center_image.setAutoDraw(False)
            if Key_Resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['num_8', 'num_6', 'num_2', 'num_4'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Key_Resp.keys = theseKeys[-1]  # just the last key pressed
                    Key_Resp.rt = Key_Resp.clock.getTime()
                    #Check for Correct or Incorrect
                    if (correct_answer == str(Key_Resp.keys)) or (correct_answer == Key_Resp.keys):
                        accuracy = corr_answer
                    elif Key_Resp.keys in ['', [], None]:
                        accuracy = no_answer
                    else:
                        accuracy = incorrect_answer
                    # a response ends the routine
                    continueRoutine = False
            # *p_port* updates
            if t >= 3.5 and p_port.status == NOT_STARTED:
            # keep track of start time/frame for later
                p_port.tStart = t  # underestimates by a little under one frame
                p_port.frameNStart = frameN  # exact frame index
                p_port.status = STARTED
                win.callOnFlip(p_port.setData, int(code))
            if p_port.status == STARTED and t >= (8.5-win.monitorFramePeriod*0.75): #most of one frame period left
                p_port.status = STOPPED
                win.callOnFlip(p_port.setData, int(0))
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Trial"-------
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Key_Resp.keys in ['', [], None]:  # No response was made
           Key_Resp.keys=None
        
        
        #Adding Accuracy Column to Data File
        if (correct_answer == str(Key_Resp.keys)) or (correct_answer == Key_Resp.keys):
            accuracy = corr_answer
        elif Key_Resp.keys in ['', [], None]:
            accuracy = no_answer
        else:
            accuracy = incorrect_answer
        thisExp.addData('accuracy', accuracy)
        
        
        # store data for TrialsF1 (TrialHandler)
        Trials.addData('Key_Resp.keys',Key_Resp.keys)
        if p_port_images.status == STARTED:
            win.callOnFlip(p_port_images.setData, int(0))
        if Key_Resp.keys != None:  # we had a response
            Trials.addData('Key_Resp.rt', Key_Resp.rt)
        if p_port.status == STARTED:
            win.callOnFlip(p_port.setData, int(accuracy))
        thisExp.nextEntry()


#------Prepare to start Routine "Break"-------       
def execute_Break(name):
    t = 0
    BreakClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    BreakKey_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    BreakKey_resp.status = NOT_STARTED
    # keep track of which components have finished
    BreakComponents = []
    BreakComponents.append(Ready)
    BreakComponents.append(BreakKey_resp)
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "Break"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = BreakClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
    
        # *Ready* updates
        if t >= 0.0 and Ready.status == NOT_STARTED:
            # keep track of start time/frame for later
            Ready.tStart = t  # underestimates by a little under one frame
            Ready.frameNStart = frameN  # exact frame index
            Ready.setAutoDraw(True)
    
        # *BreakKey_resp* updates
        if t >= 0.0 and BreakKey_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            BreakKey_resp.tStart = t  # underestimates by a little under one frame
            BreakKey_resp.frameNStart = frameN  # exact frame index
            BreakKey_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(BreakKey_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if BreakKey_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
        
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                BreakKey_resp.keys = theseKeys[-1]  # just the last key pressed
                BreakKey_resp.rt = BreakKey_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        endExpNow = False 

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
    
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()


    #-------Ending Routine "Break"-------
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if BreakKey_resp.keys in ['', [], None]:  # No response was made
       BreakKey_resp.keys=None
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('BreakKey_resp.keys',BreakKey_resp.keys)
    if BreakKey_resp.keys != None:  # we had a response
        thisExp.addData('BreakKey_resp.rt', BreakKey_resp.rt)
    thisExp.nextEntry()
    # the Routine "Continue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    

for t in range(NUM_BLOCKS):
    execute_Break("Break")
    execute_trial("TrialsM" + str(t+1), MALE)
    execute_Break("Break")
    execute_trial("TrialsF" + str(t+1), FEMALE)

#Change order to change Male/Female blocks

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
