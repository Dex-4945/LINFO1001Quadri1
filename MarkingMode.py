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
def doTheMath(mode, question, answer, totalQ, totalA):
  isCorrect == False
  if answer >= 0:
    isCorrect = question[1][answer][2];
  if isCorrect:
    if mode == 1 or mode == 2:
      return 1
    if mode == 3:
      return ((totalA/totalQ) - 1)
  else:
    if mode == 2 or mode == 3:
      return -1
  return 0
  
#Stores points according to each marking method in list
def markMe(answers, questions):
  #marks[] contains three values, one for each marking method
  marks = []
  totalQ = len(questions)
  totalA = 0
  for q in range(len(questions)):
    totalA += len(questions[q][1])
  for i in range(len(questions)):
    #evalMode 1
    marks[0] += doTheMath(1, questions[i], answers[i])
    #evalMode 2
    marks[1] += doTheMath(2, questions[i], answers[i])
    #evalMode 3
    marks[2] += doTheMath(3, questions[i], answers[i], totalQ, totalA)
  return marks
