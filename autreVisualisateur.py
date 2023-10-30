import tkinter as tk
from tkinter import ttk
import qcm
import random
root = tk.Tk()
frm = ttk.Frame(root, padding = 10)
frm.grid()
ttk.Style().configure('blue.TButton', background = 'blue', padding = '')
ttk.Style().configure('white.TButton', background = 'white', padding = '')

class Question():
    def __init__(self, questionLine):
        self.name = questionLine[0]
        self.answers = questionLine[1]
        self.choices = len(self.answers)

questionnaire = qcm.build_questionnaire('QCM.txt')
progress = 0
reDisplay = True
answerOrder = []
questions = []
input = []
grades = False
for i in range(len(questionnaire)):
    questions.append(Question(questionnaire[i]))
    input.append(-1)
questions.append(Question(["Are you ready to submit your answers?", []]))
for i in range(len(questions)-1):
    answerOrder.append([])
    for j in range(len(questions[i].answers)):
        answerOrder[i].append(-1)
for i in range(len(answerOrder)):
    for j in range(len(answerOrder[i])):
        while answerOrder[i][j] == -1:
            rNum = random.randint(0, len(answerOrder[i])-1)
            answerOrder[i][j] = rNum
            for k in range(0, j):
                if answerOrder[i][k] == rNum:
                    answerOrder[i][j] = -1
print(answerOrder)

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
    print(answerNum)
    if input[progress] == -1:
        input[progress] = answerNum
    elif input[progress] != answerNum:
        input[progress] = answerNum
    else:
        input[progress] = -1
    showQuestion()

#Stores points according to each marking method in list
def markMe(input, questions):
    #marks[] contains three values, one for each marking method
    totalQ = len(questions)
    totalA = 0
    for q in range(len(questions)):
        totalA += questions[q].choices
    print(str(totalA) + " " + str(totalQ))
    marks = [[0, 0, 0], []]
    for q in range(len(questions)-1):
        isCorrect = False
        if input[q] >= 0:
            isCorrect = questions[q].answers[input[q]][1]
        if isCorrect == True:
            marks[0][0] += 1
            marks[0][1] += 1
            marks[0][2] += ((totalA/totalQ) - 1)
            marks[1].append(True)
        else:
            marks[0][1] -= 1
            marks[0][2] -= 1
            marks[1].append(False)
    print(marks)
    return marks

def submit():
    print(input)
    markMe(input, questions)
    for widget in frm.winfo_children():
        widget.grid_remove()
    ttk.Button(frm, text = "Finish", command = root.destroy).grid(column = 0, row = 0)

def showQuestion():
    for widget in frm.winfo_children():
        widget.grid_remove()
    ttk.Button(frm, text = "<--", command = previousQuestion).grid(column = 0, row = 0)
    ttk.Button(frm, text = "-->", command = nextQuestion).grid(column = 2, row = 0)
    ttk.Label(frm, text = questions[progress].name).grid(column = 1, row = 1)
    for i in range(questions[progress].choices):
        if input[progress] == answerOrder[progress][i]:
            button = ttk.Button(frm, text = questions[progress].answers[answerOrder[progress][i]][0], command = lambda i = i: storeOrEraseInput(answerOrder[progress][i]), style = 'blue.TButton')
        else:
            button = ttk.Button(frm, text = questions[progress].answers[answerOrder[progress][i]][0], command = lambda i = i: storeOrEraseInput(answerOrder[progress][i]), style = 'white.TButton')
        button.grid(column = 1, row = i + 2)
    if progress == len(questions)-1:
        ttk.Button(frm, text = "Submit", command = submit).grid(column = 1, row = 3)
showQuestion()

root.mainloop()
