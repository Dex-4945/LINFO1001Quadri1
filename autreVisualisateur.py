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
results = []
amountAnswers = 0
for i in range(len(questionnaire)):
    questions.append(Question(questionnaire[i]))
    input.append(-1)
questions.append(Question(["Are you ready to submit your answers?", []]))
for i in range(len(questions)-1):
    answerOrder.append([])
    for j in range(len(questions[i].answers)):
        answerOrder[i].append(-1)
        amountAnswers += 1
for i in range(len(answerOrder)):
    for j in range(len(answerOrder[i])):
        while answerOrder[i][j] == -1:
            rNum = random.randint(0, len(answerOrder[i])-1)
            answerOrder[i][j] = rNum
            for k in range(0, j):
                if answerOrder[i][k] == rNum:
                    answerOrder[i][j] = -1
maxPoints = [(len(questions) - 1), (len(questions) - 1), ((len(questions) - 1) * ((amountAnswers/(len(questions) - 1)) - 1))]

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
    if input[progress] == -1:
        input[progress] = answerNum
    elif input[progress] != answerNum:
        input[progress] = answerNum
    else:
        input[progress] = -1
    nextQuestion()
    showQuestion()

#Stores points according to each marking method in list
def markMe(input, questions):
    #marks[] contains three values, one for each marking method
    marks = [[0, 0, 0], []]
    for q in range(len(questions)-1):
        isCorrect = False
        if input[q] >= 0:
            isCorrect = questions[q].answers[input[q]][1]
        if isCorrect == True:
            marks[0][0] += 1
            marks[0][1] += 1
            marks[0][2] += ((amountAnswers/(len(questions) - 1)) - 1)
            marks[1].append(True)
        else:
            marks[0][1] -= 1
            marks[0][2] -= 1
            marks[1].append(False)
    return marks

def showAll(previousRow, mode):
    for i in range(len(questions) - 1):
        ttk.Label(frm, text = questions[i].name).grid(column = 1, row = previousRow + 1)
        isCorrect = False
        if input[i] >= 0:
            isCorrect = questions[i].answers[input[i]][1]
        if mode == 0:
            ttk.Label(frm, text = "Without negative points").grid(column = 2, row = previousRow)
            if isCorrect:
                labelTrue = ttk.Label(frm, text = "1/1", foreground = 'green').grid(column = 2, row = previousRow + 1)
            else:
                labelFalse = ttk.Label(frm, text = "0/1", foreground = 'red').grid(column = 2, row = previousRow + 1)
        elif mode == 1:
            ttk.Label(frm, text = "With negative points").grid(column = 2, row = previousRow)
            if isCorrect:
                labelTrue = ttk.Label(frm, text = "1/1", foreground = 'green').grid(column = 2, row = previousRow + 1)
            else:
                labelFalse = ttk.Label(frm, text = "-1/1", foreground = 'red').grid(column = 2, row = previousRow + 1)
        elif mode == 2:
            ttk.Label(frm, text = "With balanced points").grid(column = 2, row = previousRow)
            if isCorrect:
                labelTrue = ttk.Label(frm, text = str((amountAnswers/(len(questions) - 1)) - 1) + "/" + str((amountAnswers/(len(questions) - 1)) - 1), foreground = 'green').grid(column = 2, row = previousRow + 1)
            else:
                labelFalse = ttk.Label(frm, text = "-1/" + str((amountAnswers/(len(questions) - 1)) - 1), foreground = 'red').grid(column = 2, row = previousRow + 1)
        elif mode == 3:
            ttk.Label(frm, text = "Without negative points").grid(column = 2, row = previousRow)
            if isCorrect:
                labelTrue = ttk.Label(frm, text = "1/1", foreground = 'green').grid(column = 2, row = previousRow + 1)
            else:
                labelFalse = ttk.Label(frm, text = "0/1", foreground = 'red').grid(column = 2, row = previousRow + 1)
            ttk.Label(frm, text = "With negative points").grid(column = 3, row = previousRow)
            if isCorrect:
                labelTrue = ttk.Label(frm, text = "1/1", foreground = 'green').grid(column = 3, row = previousRow + 1)
            else:
                labelFalse = ttk.Label(frm, text = "-1/1", foreground = 'red').grid(column = 3, row = previousRow + 1)
            ttk.Label(frm, text = "With balanced points").grid(column = 4, row = previousRow)
            if isCorrect:
                labelTrue = ttk.Label(frm, text = str((amountAnswers/(len(questions) - 1)) - 1) + "/" + str((amountAnswers/(len(questions) - 1)) - 1), foreground = 'green').grid(column = 4, row = previousRow + 1)
            else:
                labelFalse = ttk.Label(frm, text = "-1/" + str((amountAnswers/(len(questions) - 1)) - 1), foreground = 'red').grid(column = 4, row = previousRow + 1)
        for j in range(questions[i].choices):
            if input[i] == answerOrder[i][j]:
                label = ttk.Label(frm, text = questions[i].answers[answerOrder[i][j]][0] + " : " + questions[i].answers[answerOrder[i][j]][2], foreground = 'blue')
            else:
                label = ttk.Label(frm, text = questions[i].answers[answerOrder[i][j]][0] + " : " + questions[i].answers[answerOrder[i][j]][2], foreground = 'black')
            label.grid(column = 1, row = previousRow + 2 + j)
        for j in range(questions[i].choices):
            if (questions[i].answers[answerOrder[i][j]][1]):
                labelIsCorrect = ttk.Label(frm, text = "Correct", foreground = 'green')
            else:
                labelIsCorrect = ttk.Label(frm, text = "Incorrect", foreground = 'red')
            labelIsCorrect.grid(column = 0, row = previousRow + 2 + j)
        ttk.Label(frm, text = "").grid(column = 1, row = previousRow + 2 + questions[i].choices)
        ttk.Label(frm, text = "").grid(column = 0, row = previousRow + 2 + questions[i].choices)
        previousRow += 3 + questions[i].choices
    if mode == 0 or mode == 1 or mode == 2:
        ttk.Label(frm, text = "Total : " + str(results[0][mode]) + "/" + str(maxPoints[mode])).grid(column = 2, row = previousRow)
    elif mode == 3:
        for i in range(3):
            ttk.Label(frm, text = "Total : " + str(results[0][i]) + "/" + str(maxPoints[i])).grid(column = 2 + i, row = previousRow)
    return previousRow

def displayGrades(mode):
    thisRow = 0
    for widget in frm.winfo_children():
        widget.grid_remove()
    if(mode == 0 or mode == 1):
        ttk.Label(frm, text = "Here is your corrected submission:").grid(column = 1, row = 0)
        ttk.Label(frm, text = "").grid(column = 1, row = 1)
        ttk.Label(frm, text = "").grid(column = 1, row = 2)
        thisRow = showAll(4, mode)
    elif (mode == 2):
        ttk.Label(frm, text = "Here is your corrected submission:").grid(column = 1, row = 0)
        ttk.Label(frm, text = "").grid(column = 1, row = 1)
        ttk.Label(frm, text = "").grid(column = 1, row = 2)
        thisRow = showAll(4, mode)
    elif (mode == 3):
        ttk.Label(frm, text = "Here is your corrected submission:").grid(column = 1, row = 0)
        ttk.Label(frm, text = "").grid(column = 1, row = 1)
        ttk.Label(frm, text = "").grid(column = 1, row = 2)
        thisRow = showAll(2, mode)
    for i in range(1, 4):
        ttk.Label(frm, text = "").grid(column = 1, row = thisRow + i)
    ttk.Button(frm, text = "Finish", command = root.destroy).grid(column = 1, row = thisRow + 4)

def submit():
    for widget in frm.winfo_children():
        widget.grid_remove()
    global results 
    results = markMe(input, questions)
    ttk.Label(frm, text = "").grid(column = 0, row = 0)
    ttk.Label(frm, text = "How would you like to be graded?").grid(column = 0, row = 1)
    ttk.Label(frm, text = "").grid(column = 0, row = 2)
    ttk.Button(frm, text = "Mode1: No negative points", command = lambda : displayGrades(0)).grid(column = 0, row = 3)
    ttk.Button(frm, text = "Mode2: Negative points allowed", command = lambda : displayGrades(1)).grid(column = 0, row = 4)
    ttk.Button(frm, text = "Mode3: Balanced points", command = lambda : displayGrades(2)).grid(column = 0, row = 5)
    ttk.Button(frm, text = "Mode4: Compare all three modes", command = lambda : displayGrades(3)).grid(column = 0, row = 6)
    ttk.Label(frm, text = "").grid(column = 0, row = 7)

def showQuestion():
    for widget in frm.winfo_children():
        widget.grid_remove()
    ttk.Button(frm, text = "<--", command = previousQuestion).grid(column = 0, row = 0)
    ttk.Button(frm, text = "-->", command = nextQuestion).grid(column = 2, row = 0)
    ttk.Label(frm, text = "").grid(column = 0, row = 1)
    ttk.Label(frm, text = questions[progress].name).grid(column = 1, row = 2)
    ttk.Label(frm, text = "").grid(column = 0, row = 3)
    for i in range(questions[progress].choices):
        if input[progress] == answerOrder[progress][i]:
            button = ttk.Button(frm, text = questions[progress].answers[answerOrder[progress][i]][0], command = lambda i = i : storeOrEraseInput(answerOrder[progress][i]), style = 'blue.TButton')
        else:
            button = ttk.Button(frm, text = questions[progress].answers[answerOrder[progress][i]][0], command = lambda i = i : storeOrEraseInput(answerOrder[progress][i]), style = 'white.TButton')
        button.grid(column = 1, row = i + 4)
    ttk.Label(frm, text = "").grid(column = 0, row = 5 + questions[progress].choices)
    if progress == len(questions)-1:
        ttk.Button(frm, text = "Submit", command = submit).grid(column = 1, row = 5)
        ttk.Label(frm, text = "").grid(column = 0, row = 6)
showQuestion()

root.mainloop()