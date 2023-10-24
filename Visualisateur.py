from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


class Question():
    name = ""
    reponse = []
    Choix = 0
    def __init__(self, name, reponse):
        name = self.name
        reponse = self.reponse
        return

class Questionnaire():
    listQuestion = []

    index = 0

    def __init__(self):
        ttk.Button(frm, text="<-", command=self.PrevQuestion).grid(column=0, row=0)
        ttk.Button(frm, text="->", command=self.NextQuestion).grid(column=2, row=0)


        self.ReadFile("QCM.txt")
        self.ShowQuestion(self.index)


        print(self.listQuestion[1].name)


        return

    def NextQuestion(self):
        self.index+=1
        self.ShowQuestion(self.index)
    def PrevQuestion(self):
        if(self.index !=0):
            self.index-=1
        self.ShowQuestion(self.index)


    def ShowQuestion(self, index):
        ttk.Label(frm, text=self.listQuestion[index].name).grid(column=1, row=0)
        for i in range(len(self.listQuestion[index].reponse)):
            ttk.Label(frm, text=self.listQuestion[index].reponse[i]).grid(column=1, row=i+1)



    def ReadFile(self, filename):
        f = open(filename, "r")
        q = Question("name", "question")
        for line in f:
            if(line.startswith("Q")):
                q.name = line
            elif(line.startswith("A")):
                q.reponse.append(line)
            else:
                self.listQuestion.append(q)
                print(q.name)


            
            

                



questionnaire = Questionnaire()





root.mainloop()
