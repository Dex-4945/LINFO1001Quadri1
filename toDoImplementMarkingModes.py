#In main:

#store a list of answers as unanswered (value = -1)
answers = []
if ("""button1 2 or 3 checked"""):
  #pass value 0, 1 or 2 to answers[number of the question]
if ("""button unchecked"""):
  #pass value -1 to answers[number of the question]

"when user hits "evaluate" button, call evaluate function
if ("""button trigger"""):
  markME(evalMode, answers, questions);







#my function
#Stores points in list and sums them up according to each marking method.
def markMe(answers, questions):
  #marks[] contains three values, one for each marking method
  totalQ = len(questions)
  totalA = 0
  for q in range(len(questions)):
    totalA += len(questions[q][1])
  print(str(totalA) + " " + str(totalQ))
  marks = [[0, 0, 0], []]
  for q in range(len(questions)):
    isCorrect = False
    if answers[q] >= 0:
      isCorrect = questions[1][answers[q]][2];
    if isCorrect:
      marks[0][0] += 1
      marks[0][1] += 1
      marks[0][2] += ((totalA/totalQ) - 1)
      marks[1].append(True)
    else:
      marks[0][1] -= 1
      marks[0][2] -= 1
      marks[1].append(False)
  return marks
