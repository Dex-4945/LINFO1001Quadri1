
#Code pour choisir le mode d'affichage
#Cette fonction demande à l'utilisateur de choisir un mode d'affichage et en fonction de sa réponse, 
#le mode sera stocké dans une variable afin de savoir quel mode utiliser lors de la visualisation des points.

#in main: have a variable "evalMode" containing the defalut value 0 (comparative mode)
#in main: evalMode = selection()
def EvaluationModeSelection()
    reponse = input("Choisissez un mode d'affichage: ")
    if reponse == "mode comparatif":
        return(0)
    elif reponse == "mode evaluation":
        lequel = input("Quel mode de cotation voulez-vous choisir? ")
        if lequel == "cotation 1":
            return(1)
        elif lequel == "cotation 2":
            return(2)
        elif lequel == "cotation 3":
            return(3)
    else:
        print("Choisissez un mode d'affichage valide.")
selection_1()
