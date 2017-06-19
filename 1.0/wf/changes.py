# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:17:00 2016

@author: mdl
"""
#1)-----------------------------------------------------------------TTL
#Code
#black male = neutral male   
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
            
#Check for Correct or Incorrect
correct_answer = 1*16 #equal to R1 in PyCorder
incorrect_answer = 2*16 #equal to R2 in PyCorder
no_answer = 3*16 #equal to R3 in PyCorder
if (correct_answer == str(Key_Resp.keys)) or (correct_answer == Key_Resp.keys):
    accuracy = correct_answer
elif Key_Resp.keys in ['', [], None]:
    accuracy = no_answer
else:
    accuracy = incorrect_answer
    
    
if t >= 0.5 and p_port_images.status == NOT_STARTED:
# keep track of start time/frame for later
    p_port_images.tStart = t  # underestimates by a little under one frame
    p_port_images.frameNStart = frameN  # exact frame index
    p_port_images.status = STARTED
    win.callOnFlip(p_port_images.setData, int(14))
if p_port_images.status == STARTED and t >= (2.0-win.monitorFramePeriod*0.75): #most of one frame period left
    p_port_images.status = STOPPED
    win.callOnFlip(p_port_images.setData, int(15))


#2)-----------------------------------------------------------------parallel port
p_port = parallel.ParallelPort(address=u'0xDFF8')
p_port_images = parallel.ParallelPort(address=u'0xDFF8')

#3)-----------------------------------------------------------------parallel port
thisExp.addData('condition', center_image.name[1:3])

#4)-----------------------------------------------------------------stimuli
sad_male_images = []
sad_male_images = sad_male_images*int(180/20)
neutral_male_images = []
neutral_male_images = neutral_male_images*int(180/20)
sad_female_images = []
sad_female_images = sad_female_images*int(180/20)
neutral_female_images = []
neutral_female_images = neutral_female_images*int(180/20)


# set up handler to look after randomisation of conditions etc
Trials = data.TrialHandler(nReps=1.........................

# *p_port_images* updates
if t >= 0.5 and p_port_images.status == NOT_STARTED:
# keep track of start time/frame for later
    p_port_images.tStart = t  # underestimates by a little under one frame
    p_port_images.frameNStart = frameN  # exact frame index
    p_port_images.status = STARTED
    win.callOnFlip(p_port_images.setData, int(15))
if p_port_images.status == STARTED and t >= (2.0-win.monitorFramePeriod*0.75): #most of one frame period left
    p_port_images.status = STOPPED
    win.callOnFlip(p_port_images.setData, int(0))



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
        sad_male_images.append(visual.ImageStim(win=win, name=name,units='deg', 
    image=file, mask=None,
    ori=0, pos=[0, 3.2], size=[6, 6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0))
    #black male = neutral male   
    for i in range(NUM_IMAGES):
        file = path_to_images + "AMNE" + "%02d" %(i + 1) + ".jpg"
        name = "AMNE" + "%02d" %(i + 1) + ".jpg"
        neutral_male_images.append(visual.ImageStim(win=win, name=name,units='deg', 
    image=file, mask=None,
    ori=0, pos=[0, 3.2], size=[6, 6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0))
    #white female = sad female
    for i in range(NUM_IMAGES):
        file = path_to_images + "AFSA" + "%02d" %(i + 1) + ".jpg"
        name = "AFSA" + "%02d" %(i + 1) + ".jpg"
        sad_female_images.append(visual.ImageStim(win=win, name=name,units='deg', 
    image=file, mask=None,
    ori=0, pos=[0, 3.2], size=[6, 6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0))
    #black female  = neutral female    
    for i in range(NUM_IMAGES):
        file = path_to_images + "AFNE" + "%02d" %(i + 1) + ".jpg"
        name = "AFNE" + "%02d" %(i + 1) + ".jpg"
        neutral_female_images.append(visual.ImageStim(win=win, name=name,units='deg', 
    image=file, mask=None,
    ori=0, pos=[0, 3.2], size=[6, 6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0))


#-------Starting Practice Trials-------#
# Each trial executes this function
def execute_trial(name, gender):
    endExpNow = False
    if gender == MALE:
        conditions_file = data.importConditions(u'MalePracticeFile.csv')
    else:
        conditions_file = data.importConditions(u'FemalePracticeFile.csv')


#----------Starting Actual Trials---------#
# Each trial executes this function
def execute_trial(name, gender):
    endExpNow = False
    if gender == MALE:
        conditions_file = data.importConditions(u'EmotionMaConditionsFile.csv')
    else:
        conditions_file = data.importConditions(u'EmotionFeConditionsFile.csv')