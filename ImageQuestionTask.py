import random, math, array, random, csv
from psychopy import core,visual,event

class Task:

    ITI = 0.5
   
    def __init__(self,win,filename,tasknr,which,anchor):

        self.datafile = open(filename, 'a') #a simple text file with 'comma-separated-values'
        self.win = win
        self.tasknr = tasknr
        self.which = which
        self.anchor = anchor
        #if which == 1:
        #    self.instructionText = 'blue = ' + comparativeOptions[0] + ', ' + 'yellow = ' + comparativeOptions[1]
        #else:
        self.instructionText = 'Use the keyboard to type in your answer and press enter to submit'
        #self.unit = unit
        self.which = which
        self.trial = 1
        
        # visuals
        self.Question = visual.TextStim(self.win,text="",pos=(.0,.3),height=.08,alignVert='center',wrapWidth=1.5)
        self.Instructions = visual.TextStim(self.win,text=self.instructionText,pos=(.0,-.8),height=.07,alignVert='center',wrapWidth=1.5)
        self.Response = visual.TextStim(self.win,text="",pos=(.0,.0),height=.08,alignVert='center',wrapWidth=1.5)
        self.trialClock = core.Clock()
        self.datafile.write('taskNr,taskId,acnhor,question,response,RT\n')
        
    def Run(self):
        trial = 1
        done = False
        while not done:        
            if self.which == "season":
                if trial == 1:
                    qst = "Thinking about the pictures you saw, which season describes these best? (type 1 for winter, 2 for spring, 3 for summer, 4 for autumn)"
                if trial == 2:
                    qst = "Thinking about the pictures you saw, on a day like those shown, what temperature is it? (in degrees Celcius)"
                if trial == 3:
                    qst = "Thinking about the pictures you saw, describe in a short sentence (e.g. 6 words) what a person might do on a day like those."
            if self.which == "cars":
                if trial == 1:
                    qst = "Thinking about the pictures you saw, what type of car describes these best? (type 1 for luxury, 2 for economy, 3 for people carrier, 4 for commercial)"
                if trial == 2:
                    qst = "Thinking about the pictures you saw, how much would a car like those shown cost? (in pounds)"
                if trial == 3:
                    qst = "Thinking about the pictures you saw, describe in a short sentence (e.g. 6 words) who would drive a car like those."
                    
            self.Question.setText(qst)
            # display question
            self.Question.draw()
            self.Instructions.draw()
            self.Response.draw()
            self.win.flip()
            # start RT measurement
            self.trialClock.reset()
            # wait for response
            text = ""
            cont = False
            if trial == 1:
                # multiple choice answer, only allow a single digit
                while event.getKeys(keyList=['return','num_enter'])==[] or len(text) == 0:
                    letterlist=event.getKeys(keyList=['1','2','3','4','num_1','num_2','num_3','num_4','backspace'])
                    for l in letterlist:
                        #if key isn't backspace, set key pressed as the string
                        if l !='backspace':
                            text=l.replace('num_','')[0]
                        #otherwise, take the last letter off the string
                        elif len(text)>0:
                            text=''
                        elif len(text) < 1:
                            text=''
                    self.Response.setText(text)
                    self.Question.draw()
                    self.Response.draw()
                    self.Instructions.draw()
                    self.win.flip()
            elif trial == 2:
                # numeric answer, only allow digits
                while event.getKeys(keyList=['return','num_enter'])==[] or len(text) == 0:
                    letterlist=event.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0',
                    'num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9','num_0',
                    'backspace'])
                    for l in letterlist:
                        #if key isn't backspace, add key pressed to the string
                        if l !='backspace':
                            text+=l.replace('num_','')
                        #otherwise, take the last letter off the string
                        elif len(text)>0:
                            text=text[:-1]
                        elif len(text) < 1:
                            text=''
                    self.Response.setText(text)
                    self.Question.draw()
                    self.Response.draw()
                    self.Instructions.draw()
                    self.win.flip()
            else:
                # free text answer
                while event.getKeys(keyList=['return','num_enter'])==[] or len(text) == 0:
                    letterlist=event.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0',
                    'num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9','num_0',
                    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                    'comma','period','space','exclamation','question',
                    'backspace',])
                    for l in letterlist:
                        #if key isn't backspace, add key pressed to the string
                        if l !='backspace':
                            text+=l.replace('num_','').replace('comma',',').replace('period','.').replace('space',' ').replace('exclamation','!').replace('question','?')
                        #otherwise, take the last letter off the string
                        elif len(text)>0:
                            text=text[:-1]
                        elif len(text) < 1:
                            text=''
                    self.Response.setText(text)
                    self.Question.draw()
                    self.Response.draw()
                    self.Instructions.draw()
                    self.win.flip()
                    
                
            # get RT
            RT = self.trialClock.getTime()
            # get response
            response = text
            # clear keypresses
            event.clearEvents()
            
            # write data
            self.datafile.write(
                    str(self.tasknr) + ',' + str(self.which) + ',' + str(self.anchor) + ',' +
                    qst + ',' +
                    response + ',' +
                    str(1000*RT) + '\n')
            
            # ITI
            self.win.flip()
            core.wait(self.ITI)
            trial += 1
            text=""
            self.Response.setText(text)
            if trial > 3:
                done = True
                    
        self.datafile.close()
