from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
t2 = ttk.Frame(root, padding=10)
t2.grid()

class Question:
    name = ""
    reponse = []
    def __init__(self, name):
        name = self.name
        reponse = []
        return

class Questionnaire:
    listQuestion = []
    label_List = []

    point_Bonne = 1
    point_Mauvais = -0.5

    choix = [0,3,1]

    index = 0

    def __init__(self):
        ttk.Button(frm, text="<-", command=self.PrevQuestion).grid(column=0, row=0)
        ttk.Button(frm, text="->", command=self.NextQuestion).grid(column=2, row=0)


        self.ReadFile("QCM.txt")
        self.ShowQuestion(self.index)

        
        for question in self.listQuestion:
            print(question.name)
            for reponse in question.reponse:
                print(reponse)



        self.moyenneCalculator()

        return


    def moyenneCalculator(self):
        moyenne = 0
        for index in range(len(self.listQuestion)-1):
            print(self.listQuestion[index].reponse[self.choix[index]][1] == 'V')
            if(self.listQuestion[index].reponse[self.choix[index]][1] == 'V'):
                moyenne += self.point_Bonne
            else:
                moyenne += self.point_Mauvais
        print(moyenne)
        return 




    def NextQuestion(self):
        
        self.index+=1
        self.ShowQuestion(self.index)
    def PrevQuestion(self):
        if(self.index !=0):
            self.index-=1
        self.ShowQuestion(self.index)


           
            
        

    def ShowQuestion(self, index):
        self.label_List = []
        ttk.Label(t2, text=self.listQuestion[index].name).grid(column=1, row=0)

        for i in range(len(self.listQuestion[index].reponse)):
            ttk.Label(t2, text=self.listQuestion[index].reponse[i]).grid(column=1, row=i+1)





    def ReadFile(self, filename):
        f = open(filename, "r")
        for line in f:
            if(line.startswith("Q")):
                q = Question("name")
                line = line.strip("\n")
                line = line.split("|")

                q.name = line[1]
                q.reponse = []
            elif(line.startswith("A")):
                line = line.strip("\n")
                line = line.split("|")
                
                q.reponse.append(line[1:])
            elif(line.startswith("\n")):
                self.listQuestion.append(q)
                


            



questionnaire = Questionnaire()





root.mainloop()
