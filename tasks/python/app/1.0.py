from subprocess import Popen
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import random
import webbrowser 

class R56(App):
    # print task pressed
    def callback(self,instance):
        task_button_pressed = instance.text
        subjectNum = self.output_label.text
        #check if entered subject number
        if subjectNum.isdigit() == True:
            subjectNum = int(subjectNum)
            print('The button <%s> is being pressed' % instance.text)
            if task_button_pressed == 'DFAT':
                Popen([winpython_path, dfat, '%s'% self.output_label.text])
            if task_button_pressed == 'WF':
                random.shuffle(lwf)
                wfType = lwf[0]
                Popen([winpython_path, wfType, '%s'% self.output_label.text])
            if task_button_pressed == 'SMI':
                webbrowser.open('https://utexas.qualtrics.com/SE/?SID=SV_42hp2elKWQePbW5')
            if task_button_pressed == 'Questionnaire':
                webbrowser.open('https://utexas.qualtrics.com/SE/?SID=SV_09gxfPs7YeqSrml')
            if task_button_pressed == 'RS-I':
                Popen([winpython_path, rs_i, '%s'% self.output_label.text])
            if task_button_pressed == 'RS-II':
                Popen([winpython_path, rs_ii, '%s'% self.output_label.text])          
            if task_button_pressed == 'RS-III':
                Popen([winpython_path, rs_iii, '%s'% self.output_label.text])
        else:
            self.output_label.text = 'Not valid. Please try again.'
   
    def build(self):
        self.icon = 'app.ico'
        layout = BoxLayout(padding=1, orientation="vertical")
        #text box and press enter
        self.output_label = TextInput(font_size=20, text='Enter Subject', multiline=False)
        self.output_label.bind(on_text_validate=self.print_subject)
        layout.add_widget(self.output_label)
        #list of tasks
        ltask = ['RS-I','DFAT','WF','RS-II','SMI','RS-III','Questionnaire']
        for litem in ltask:
            btn = Button(text=litem)
            btn.bind(on_press=self.callback)
            layout.add_widget(btn)
        return layout
        
    #print subject number
    def print_subject(self,btn):
        print('subject number is %s'%self.output_label.text)

#directory
task_directory = r'C:\Users\mdl\Desktop\R56'
winpython_path = task_directory+'\\x32\\python-2.7.10\\python.exe'
rs_i = task_directory+'\\tasks\\rsi\\rsi.py'
rs_ii = task_directory+'\\tasks\\rsii\\rsii.py'
rs_iii = task_directory+'\\tasks\\rsiii\\rsiii.py'
dfat = task_directory+'\\tasks\\dfat\\DFAT.py'
wf_fema = task_directory+'\\tasks\\wf\\FEMA4ImagesEEG.py'
wf_mafe = task_directory+'\\tasks\\wf\\MAFE4ImagesEEG.py'
lwf = [wf_fema,wf_mafe]
app=R56()
app.run()