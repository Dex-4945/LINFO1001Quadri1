import qcm
import os

#Stores points according to each marking method in list
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

if __name__ == '__main__':
    filename = "QCM.txt"
    questions = qcm.build_questionnaire(filename)
    answers = []
    for q in range(len(questions)):
        os.system("cls")
        print("Question " + str(q + 1) + ":\n" + questions[q][0] + "\n")
        for a in range(len(questions[q][1])):
            print("Answer " + str(a + 1) + " : " + questions[q][1][a][0])
        answers.append(int(input("\nType in the number of the answer you think is correct : ")))
        if questions[q][1][answers[q] - 1][2]:
            print(questions[q][1][answers[q] - 1][2])
        if q != len(questions) - 1:
            input("\nHit Enter for the next question")
        else:
            input("\nHit enter to display your points")
            os.system("cls")
    results = markMe(answers, questions)
    print("Comparative Mode :" + "\nMode 1: " + str(results[0][0]) + "\nMode 2: " + str(results[0][1]) + "\nMode 3: " + str(results[0][2]))
    input("\n\nHit Enter to exit questionnaire")
    os.system("cls")
