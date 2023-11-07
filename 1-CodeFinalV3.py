#import necessary libraries for Tkinter which allows to create a window and determine where and how elemnts should be placed inside it.
import tkinter as tk
from tkinter import ttk
#import the library that allows to parse the text file containning the questions, answers and descriptions of the questionnaire
import qcm
#import the random library to randomise the order in which the answers are displayed to the user
import random

#create a window
root = tk.Tk()
#create a frame inside that window so we can arrange our elements inside it.
frm = ttk.Frame(root, padding = 10)
#use the grid() method (as oppposed to pack() method) to arrange our elements. grid is more precise than pack
frm.grid()
#determine two ways styles for the buttons. Meaning one style will make their background blue, the other style is white.
ttk.Style().configure('blue.TButton', background = 'blue', padding = '')
ttk.Style().configure('white.TButton', background = 'white', padding = '')

#initialize a class that will allow to handle questions and their answers as objects rather than arrays.
class Question():
    def __init__(self, questionLine):
        #'title' of the question
        self.name = questionLine[0]
        #2d array holding the answers, their True or False value and their optionnal description.
        self.answers = questionLine[1]
        #amount of answers for that question.
        self.choices = len(self.answers)

#variable initialisation
#4d list -> questionnaire[] list holds lists of [questions groups] -> each question group[] list holds a list of question title + [answers]
# -> answers[] list holds list of each [answer] -> answer[] list holds the answer title + true/false value + optionnal description
questionnaire = qcm.build_questionnaire('QCM.txt')
#variable tells me what question the user is looking at.
progress = 0
#This 2D list will hold the lists of orders in which the questions will be randomly displayed.
#The first index of the list = index of the question in questions object-list. 
#The second index of the list = index of the answer according to the order in which they have been written in the text file.
#The value associated to each index = the new order in which the answers will be displayed.
answerOrder = []
#This list holds all the question objects created by the questions class based on the questionnaire list based on the text file parsed by build_questionnaire.
questions = []
#This list will hold the index of the answers the user will have chosen, or -1 by default to indicate he hasn't answered.
input = []
#This list holds two lists. The first holds the total amount of points that have been scored according to the three marking methods. 
#The second holds the sequence of values of the chosen answer (is the chosen answer true or false)
results = []
#This variable holds the total amount of True answers that have been written for all questions in the text file
amountTrueAnswers = 0
#This variable holds the total amount of answers that have been written for all questions in the text file
amountAnswers = 0
#This loop creates a new empty space at the end of the questions list and immediately stores an instance of the questions object according to the values stored in the questionnaire list
#It also creates an empty space at the end of the input list and immediatley sets as unanswered by storing the value -1
for i in range(len(questionnaire)):
    questions.append(Question(questionnaire[i]))
    input.append(-1)
#Because after the questions I wanted to display this message before ending the first stage of the test (answering), I stored it at the end of the questions array without any answers.
#The parameter I wrote to the Question class is a list because that is what it would have received from the questionnaire list
questions.append(Question(["Are you ready to submit your answers?", []]))
#This loop creates a new empty list at the end of the answerOrder list as long as it hasn't created a number of lists matching the number of objects stored in the questions list.
#The amount specified in the range of the outer loop is ... -1 because the last object is a message ("Are you ready to submit your answers?"), not a question with answers.
for i in range(len(questions)-1):
    answerOrder.append([])
    #This loop initialises the list just created in answerOrder with the value -1. This will be usefull in the next loop.
    #It also adds a value to amountTrueAnswers for each true answer in the questionnaire. That way the exact number of true answers is counted into the variable.
    for j in range(len(questions[i].answers)):
        answerOrder[i].append(-1)
        amountAnswers += 1
        if questions[i].answers[j][1]:
            amountTrueAnswers += 1
#This loop iterates through the 2D list answerOrder to store in it random integers ranging from 0 to the number of answers there are for each question.
#We want to make sure the same random number isn't chosen twice. The chosen method:
#The entire list has been previously initialized to -1. as long as the value of the current indexes is -1, we try to store a random integer.
#Why "as long as", since the value will be changed to a positif integer after a random integer will be chosen?
#Because if my index isn't the first one, I make sure the chosen number hasn't already been assigned to z previous index of this same question.
#If the number was already assigned then we put back -1 as value at the current index and the loop can start again until it finds a not yet chosen random number.
for i in range(len(answerOrder)):
    for j in range(len(answerOrder[i])):
        while answerOrder[i][j] == -1:
            rNum = int((random.randint(0, ((len(answerOrder[i])-1)*10)))/10)
            answerOrder[i][j] = rNum
            for k in range(0, j):
                if answerOrder[i][k] == rNum:
                    answerOrder[i][j] = -1
#This variable calculates the maximum amount of points the user can get with each marking method.
#First mode: +1 per good answer so maximum amount of points = amount of questions.
#Second mode: +1 per good answer so maximum amount of points = amount of questions.
#Third mode: amount of questions * points per question. The formula for the points per question = (amount of answers / (amount of questions - 1)).
#The choice of this formula should make the points of a user choosing his answers randomly average to zero.
maxPoints = [(len(questions) - 1), (len(questions) - 1), ((len(questions) - 1) * ((amountTrueAnswers/(len(questions) - 1)) - 1))]

#This function allows to display the next question of the questionnaire and is called by a click on the corresponding button (-->).
#We achieve this by adding a value to the 'progress' variable, but only if the last question isn't reached. This prevents out-of-bounds errors.
#After that we call the function again to display the question according to the value given to 'progress'
def nextQuestion():
    global progress
    if(progress + 1 < len(questions)):
        progress += 1
    showQuestion()

#This function allows to display the previous question of the questionnaire and is called by a click on the corresponding button (<--).
#I achieve this by subtracting a value to the 'progress' variable, but only if the first question isn't being displayed. This prevents out-of-bounds errors.
#After that we call the function again to display the question according to the value given to 'progress'
def previousQuestion():
    global progress
    if(progress != 0):
        progress -= 1
    showQuestion()

#This function is called when an answer has been chosen by the user by a click on it.
#If the question was unanswered (value -1) then we store the index of the question in the list.
#If the question was already answered and the user clicked again on the same answer as to deselect it, then we reset the value to unanswered (value -1)
#If the question was already answered and the user choses a new answer by clicking on it then we simply change the stored value to the newly chosen one.
#We then call the next question function.
def storeOrEraseInput(answerNum):
    if input[progress] == -1:
        input[progress] = answerNum
    elif input[progress] != answerNum:
        input[progress] = answerNum
    else:
        input[progress] = -1
    nextQuestion()

#This function stores points according to each marking method in a list
#Marks[0] contains three values, one for each marking method
#Marks[1] is the sequence of values for each chosen answer (True or False)
#Returns the list
def markMe(input, questions):
    marks = [[0, 0, 0], []]
    for q in range(len(questions)-1):
        isCorrect = False
        if input[q] >= 0:
            isCorrect = questions[q].answers[input[q]][1]
        if isCorrect == True:
            marks[0][0] += 1
            marks[0][1] += 1
            marks[0][2] += (amountAnswers/amountTrueAnswers)
            marks[1].append(True)
        else:
            marks[0][1] -= 1
            marks[0][2] -= 1
            marks[1].append(False)
    return marks

#This function arranges all the elements in the grade-displaying window
#If the 
#details
def showAll(previousRow, mode, frmGrades):
    for i in range(len(questions) - 1):
        ttk.Label(frmGrades, text = questions[i].name).grid(column = 1, row = previousRow + 1)
        isCorrect = False
        if input[i] >= 0:
            isCorrect = questions[i].answers[input[i]][1]
        if mode == 0:
            ttk.Label(frmGrades, text = "Without negative points").grid(column = 2, row = previousRow)
            if isCorrect:
                ttk.Label(frmGrades, text = "1/1", foreground = 'green').grid(column = 2, row = previousRow + 1)
            else:
                ttk.Label(frmGrades, text = "0/1", foreground = 'red').grid(column = 2, row = previousRow + 1)
        elif mode == 1:
            ttk.Label(frmGrades, text = "With negative points").grid(column = 2, row = previousRow)
            if isCorrect:
                ttk.Label(frmGrades, text = "1/1", foreground = 'green').grid(column = 2, row = previousRow + 1)
            else:
                ttk.Label(frmGrades, text = "-1/1", foreground = 'red').grid(column = 2, row = previousRow + 1)
        elif mode == 2:
            ttk.Label(frmGrades, text = "With balanced points").grid(column = 2, row = previousRow)
            if isCorrect:
                ttk.Label(frmGrades, text = str(round((amountAnswers/amountTrueAnswers), 2)) + "/" + str(round((amountAnswers/amountTrueAnswers), 2)), foreground = 'green').grid(column = 2, row = previousRow + 1)
            else:
                ttk.Label(frmGrades, text = "-1/" + str(round((amountAnswers/amountTrueAnswers), 2)), foreground = 'red').grid(column = 2, row = previousRow + 1)
        elif mode == 3:
            ttk.Label(frmGrades, text = "Without negative points").grid(column = 2, row = previousRow)
            if isCorrect:
                ttk.Label(frmGrades, text = "1/1", foreground = 'green').grid(column = 2, row = previousRow + 1)
            else:
                ttk.Label(frmGrades, text = "0/1", foreground = 'red').grid(column = 2, row = previousRow + 1)
            ttk.Label(frmGrades, text = "With negative points").grid(column = 3, row = previousRow)
            if isCorrect:
                ttk.Label(frmGrades, text = "1/1", foreground = 'green').grid(column = 3, row = previousRow + 1)
            else:
                ttk.Label(frmGrades, text = "-1/1", foreground = 'red').grid(column = 3, row = previousRow + 1)
            ttk.Label(frmGrades, text = "With balanced points").grid(column = 4, row = previousRow)
            if isCorrect:
                ttk.Label(frmGrades, text = str(round((amountAnswers/amountTrueAnswers), 2)) + "/" + str(round((amountAnswers/amountTrueAnswers), 2)), foreground = 'green').grid(column = 4, row = previousRow + 1)
            else:
                ttk.Label(frmGrades, text = "-1/" + str(round((amountAnswers/amountTrueAnswers), 2)), foreground = 'red').grid(column = 4, row = previousRow + 1)
        for j in range(questions[i].choices):
            if input[i] == answerOrder[i][j]:
                if questions[i].answers[answerOrder[i][j]][1]:
                    ttk.Label(frmGrades, text = questions[i].answers[answerOrder[i][j]][0] + " : " + questions[i].answers[answerOrder[i][j]][2], foreground = 'green').grid(column = 1, row = previousRow + 2 + j)
                else:
                    ttk.Label(frmGrades, text = questions[i].answers[answerOrder[i][j]][0] + " : " + questions[i].answers[answerOrder[i][j]][2], foreground = 'red').grid(column = 1, row = previousRow + 2 + j)
            else:
                if questions[i].answers[answerOrder[i][j]][1]:
                    ttk.Label(frmGrades, text = questions[i].answers[answerOrder[i][j]][0] + " : " + questions[i].answers[answerOrder[i][j]][2], foreground = 'green').grid(column = 1, row = previousRow + 2 + j)
                else:
                    ttk.Label(frmGrades, text = questions[i].answers[answerOrder[i][j]][0] + " : " + questions[i].answers[answerOrder[i][j]][2]).grid(column = 1, row = previousRow + 2 + j)
        for j in range(questions[i].choices):
            if (questions[i].answers[answerOrder[i][j]][1]):
                ttk.Label(frmGrades, text = "Correct", foreground = 'green').grid(column = 0, row = previousRow + 2 + j)
            else:
                ttk.Label(frmGrades, text = "Incorrect", foreground = 'red').grid(column = 0, row = previousRow + 2 + j)
        ttk.Label(frmGrades, text = "").grid(column = 1, row = previousRow + 2 + questions[i].choices)
        ttk.Label(frmGrades, text = "").grid(column = 0, row = previousRow + 2 + questions[i].choices)
        previousRow += 3 + questions[i].choices
    if mode == 0 or mode == 1 or mode == 2:
        ttk.Label(frmGrades, text = "Total : " + str(results[0][mode]) + "/" + str(maxPoints[mode])).grid(column = 2, row = previousRow)
    elif mode == 3:
        for i in range(3):
            ttk.Label(frmGrades, text = "Total : " + str(results[0][i]) + "/" + str(maxPoints[i])).grid(column = 2 + i, row = previousRow)
    return previousRow

#This function initializes the grade-displaying window with a scrollbar so every answer can be displayed
#details
def displayGrades(mode):
    rootGrades = tk.Tk()
    rootGrades.title("Grades")
    canvas = tk.Canvas(rootGrades, width=1000, height=500)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = ttk.Scrollbar(rootGrades, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=scrollbar.set)
    frmGrades = ttk.Frame(canvas, padding=10)
    canvas.create_window((0, 0), window=frmGrades, anchor="nw")
    def on_canvas_scroll(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    canvas.bind_all("<MouseWheel>", on_canvas_scroll)

    thisRow = 0
    if(mode == 0 or mode == 1):
        ttk.Label(frmGrades, text = "Here is your corrected submission:").grid(column = 1, row = 0)
        ttk.Label(frmGrades, text = "").grid(column = 1, row = 1)
        ttk.Label(frmGrades, text = "").grid(column = 1, row = 2)
        thisRow = showAll(2, mode, frmGrades)
    elif (mode == 2):
        ttk.Label(frmGrades, text = "Here is your corrected submission:").grid(column = 1, row = 0)
        ttk.Label(frmGrades, text = "").grid(column = 1, row = 1)
        ttk.Label(frmGrades, text = "").grid(column = 1, row = 2)
        thisRow = showAll(2, mode, frmGrades)
    elif (mode == 3):
        ttk.Label(frmGrades, text = "Here is your corrected submission:").grid(column = 1, row = 0)
        ttk.Label(frmGrades, text = "").grid(column = 1, row = 1)
        ttk.Label(frmGrades, text = "").grid(column = 1, row = 2)
        thisRow = showAll(2, mode, frmGrades)
    ttk.Label(frmGrades, text = "").grid(column = 1, row = thisRow + i)
    ttk.Button(frmGrades, text = "Finish", command = rootGrades.destroy).grid(column = 1, row = thisRow + 4)

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", on_configure)

#When the user wants to submit his answers and get graded, a click on the "submit" button calls this function.
#This function displays buttons that make the user choose the way he wants his grades to be displayed (three modes + a comparative one)
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
    ttk.Button(frm, text = "Finish", command = root.destroy).grid(column = 0, row = 8)

#This is the main function that displays every single question, answers in a random order, buttons to go to the previous or next question and final submission button.
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

#This function call starts the entire program by launching the display of the questionnaire.
showQuestion()

#this command makes the program loop until stopped.
root.mainloop()
