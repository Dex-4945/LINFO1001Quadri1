from tkinter import *
from tkinter import ttk
import qcm
root = Tk()
frm = ttk.Frame(root, padding = 10)
frm.grid()
style = ttk.Style()
#style.map('TButton', background=[('isChosen', 'blue')], foreground=[('isChosen', 'blue')])

class Question():
    def __init__(self, questionLine):
        self.name = questionLine[0]
        self.answers = questionLine[1]
        self.choices = len(self.answers)


questionnaire = qcm.build_questionnaire('QCM.txt')
progress = 0

questions = []
input = []
for i in range(len(questionnaire)):
    questions.append(Question(questionnaire[i]))
    input.append(-1)

def nextQuestion():
    global progress
    if(progress + 1 < len(questions)):
        progress += 1
    showQuestion()

def previousQuestion():
    global progress
    if(progress != 0):
        progress -= 1
    showQuestion()

def storeOrEraseInput(answerNum):
    #toggleState()
    if input[progress] == -1:
        input[progress] = answerNum
    else:
        input[progress] = -1

"""
toggled = ttk.BooleanVar()
toggled.set(False)

def toggleState():
    if toggled.get():
        toggled.set(False)
    else:
        toggled.set(True)
    #button.state(['!isChosen', 'isChosen'][toggled.get()])
"""

def showQuestion():
    for widget in frm.winfo_children():
        widget.grid_remove()
    ttk.Button(frm, text = "<--", command = previousQuestion).grid(column = 0, row = 0)
    ttk.Button(frm, text = "-->", command = nextQuestion).grid(column = 2, row = 0)
    ttk.Label(frm, text = questions[progress].name).grid(column = 1, row = 1)
    for i in range(questions[progress].choices):
        ttk.Button(frm, text = questions[progress].answers[i][0], command = storeOrEraseInput(i)).grid(column = 1, row = i+2)

ttk.Button(frm, text = "<--", command = previousQuestion).grid(column = 0, row = 0)
ttk.Button(frm, text = "-->", command = nextQuestion).grid(column = 2, row = 0)
showQuestion()

root.mainloop()
