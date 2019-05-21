import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'
from subprocess import Popen
from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

#constants
lday = ['Day-1','Day-2']
ltask = ['RS-I','WF']  

#directory
task_directory = r'C:\Users\mdl\Desktop\R56'
winpython_path = task_directory+'\\x32\\python-2.7.10\\python.exe'
drs_i = task_directory+'tasks\\rsi\\rsi.py'
dwf_fema = task_directory+'tasks\\wf\\FEMA4ImagesEEG.py'
dwf_mafe = task_directory+'tasks\\wf\\MAFE4ImagesEEG.py'
lwf = [dwf_fema,dwf_mafe]

class R56(App):
    def __init__(self,**kwargs):
        App.__init__(self)
        self.layout = FloatLayout(padding=1,size=(500, 500))
        Config.set('graphics','resizable', False)
        #text output
        self.out = TextInput(font_size=60, text='Select Day', 
                             multiline=True,pos=(0, 360),size_hint=(.75, .4))
        #buttons
        self.day1 = Button(font_size=45, text='Day-1',pos=(600, 480),size_hint=(.25, .2))
        self.day2 = Button(font_size=45, text='Day-2',pos=(600, 360),size_hint=(.25, .2))
        self.wf_fema = Button(font_size=60, text='WF-1',pos=(0, 180),size_hint=(.50, .3))
        self.wf_mafe = Button(font_size=60, text='WF-2',pos=(400, 180),size_hint=(.50, .3))
        self.rsi = Button(font_size=60, text='RS-I',pos=(0, 0),size_hint=(1, .3))
        #list        
        self.lday = [self.day1,self.day2]
        self.ltask = [self.wf_mafe,self.wf_fema,self.rsi]
        self.day = ''
    # button pressed
    def callback(self,instance):
        task_button_pressed = instance.text
        subjectNum = self.out.text
        #if day 2 pressed
        if task_button_pressed == 'Day-2':
            self.day = 2
            print('pressed Day-%s'%self.day)
            self.day2.background_color = (.95,.5,.15,1)
            self.day1.background_color = (1,1,1,1)
            if self.out.text.isdigit() == True:
                pass
            else:    
                self.out.text = 'Enter Subject Number'
        #if day 1 pressed
        elif task_button_pressed == 'Day-1':
            self.day = 1
            print('pressed Day-%s'%self.day)
            self.day1.background_color = (.95,.5,.15,1)
            self.day2.background_color = (1,1,1,1)
            if self.out.text.isdigit() == True:
                pass
            else:    
                self.out.text = 'Enter Subject Number'
        #if task pressed
        else:
            #if day already selected
            if self.day == 1 or self.day == 2:
                print('day',self.day)
                self.subject(subjectNum, task_button_pressed)

    #check if entered subject number
    def subject(self, subjectNum, task_button_pressed):
        if subjectNum.isdigit() == True:
            subjectNum_append = int(subjectNum)
            print('test',self.day)
            if self.day == 2: #day 2
                subjectNum_append = 200000 + subjectNum_append
                print('subject %s'%subjectNum_append)
                self.run_task(subjectNum_append, task_button_pressed)
            elif self.day == 1: #day 1
                subjectNum_append = 100000 + subjectNum_append            
                print('subject %s'%subjectNum_append)
                self.run_task(subjectNum_append, task_button_pressed)
        else:
                self.out.text = 'Not Valid Subject Number'
                print('no subjectNum')

    #task    
    def run_task(self, subjectNum_append, task_button_pressed):
            #wf_fema
            if task_button_pressed == 'WF-1':
                print(task_button_pressed)
                self.wf_fema.background_color = (.95,.5,.15,1)
                print([winpython_path, dwf_fema, ('%s')%subjectNum_append])
                Popen([winpython_path, dwf_fema, ('%s')%subjectNum_append])
            #wf_mafe
            elif task_button_pressed == 'WF-2':
                print(task_button_pressed)
                self.wf_mafe.background_color = (.95,.5,.15,1)
                print([winpython_path, dwf_mafe, ('%s')%subjectNum_append])
                Popen([winpython_path, dwf_mafe, ('%s')%subjectNum_append])
            #rs-i
            elif task_button_pressed == 'RS-I':
                print(task_button_pressed)
                self.rsi.background_color = (.95,.5,.15,1)
                print([winpython_path, drs_i, ('%s')%subjectNum_append])
                Popen([winpython_path, drs_i, ('%s')%subjectNum_append])

    #build gui           
    def build(self):
        self.icon = 'app.ico'
        #Day-1, day-2        
        for litem in self.lday:
            litem.bind(on_press=self.callback)
            self.layout.add_widget(litem)
        #text box and press enter
        self.out.bind(on_text_validate=self.print_subject)
        self.layout.add_widget(self.out)
        #list of tasks 
        for litem in self.ltask:
            litem.bind(on_press=self.callback)
            self.layout.add_widget(litem)
        return self.layout
        
    #print subject number
    def print_subject(self,btn):
        print('subject number is %s'%self.out.text)
#run
app=R56()
app.run()