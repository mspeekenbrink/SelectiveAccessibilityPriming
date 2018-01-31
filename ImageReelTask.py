import random, math, array, random, csv, os
from psychopy import core,visual,event

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

class Task:

    fixTime = 1.0 # fixation time in seconds
    displayTime = 1.5 # display time for consonants in seconds
    intervalTime = 0.0 # interval between consonants in seconds
    ITI = 1.0 # inter-trial interval in seconds
    
    def __init__(self,win,imageFolder):

        self.win = win
        # read filnames
        files = listdir_fullpath(imageFolder)

        # visuals
        self.ImageStims = []
        for i in range(len(files)):
            self.ImageStims.append(visual.ImageStim(self.win, image=files[i], pos=(0,0),size=(1.2,1.2)))
        # randomize order
        random.shuffle(self.ImageStims)
        
        #self.Instructions = visual.TextStim(self.win,text="Please type in the letters in the correct order and press enter to confirm",pos=(.0,-.8),height=.07,alignVert='center',wrapWidth=1.5)
        #self.Stimulus = visual.TextStim(self.win,text="",pos=(.0,.0),height=.15,alignVert='center',wrapWidth=1.5)
        #self.Response = visual.TextStim(self.win,text="___",pos=(.0,.0),height=.15,alignVert='center',wrapWidth=1.5)
        self.fixation = visual.ShapeStim(win,
            units='pix',
            lineColor='white',
            lineWidth=3.0,
            vertices=((-25, 0), (25, 0), (0,0), (0,25), (0,-25)),
            closeShape=False,
            pos= [0,0])
        self.trialClock = core.Clock()

        
    def Run(self):
        # display fixation cross
        self.fixation.draw()
        self.win.flip()
        core.wait(self.fixTime)
        for i in range(len(self.ImageStims)):
            self.ImageStims[i].draw()
            self.win.flip()
            core.wait(self.displayTime)
            if self.intervalTime > 0:
                self.win.flip()
                core.wait(self.intervalTime)
