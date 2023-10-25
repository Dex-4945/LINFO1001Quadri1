#In main:

#store a list of answers as unanswered (value = -1)
answers = []
for i in questions:
  answers[i] = -1

if ("""button1 2 or 3 checked"""):
  #pass value 0, 1 or 2 to answers[number of the question]
if ("""button unchecked"""):
  #pass value -1 to answers[number of the question]

"when user hits "evaluate" button, call evaluate function
if ("""button trigger"""):
  markME(evalMode, answers, questions);

#my function
#Function calculates points 
def doTheMath(mode, question, answer):
  isCorrect == False
  if answer >= 0:
    isCorrect = question[1][answer][2];
  if isCorrect:
    if mode == 1:
      if isCorrect
  return 0
#Stores points according to each marking method in list
def markMe(evalMode, answers, questions):
  #marks[] contains three values, one for each marking method
  marks = []
  for i in questions:
    #evalMode 1
    marks[0] += doTheMath(1, questions[i], answers[i])
    #evalMode 2
    marks[1] += doTheMath(2, questions[i], answers[i])
    #evalMode 3
    marks[2] += doTheMath(3, questions[i], answers[i])
  return marks
