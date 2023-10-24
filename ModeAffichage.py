
#Code pour choisir le mode d'affichage
#On attribue des variables à des valeurs. 
cotation_1 = 3 
cotation_2 = 2
cotation_3 = 4

#Cette fonction demande à l'utilisateur de choisir un mode d'affichage et en fonction de sa réponse, un mode lui sera affiché  
def selection_1():
    reponse = input("Choisissez un mode d'affichage: ")
    if reponse == "mode comparatif":
        return(0, cotation_1, cotation_2, cotation_3)
    elif reponse == "mode evaluation":
        lequel = input("Quel mode de cotation voulez-vous choisir? ")
        if lequel == "cotation 1":
            return(1, cotation_1)
        elif lequel == "cotation 2":
            return(2, cotation_2)
        elif lequel == "cotation 3":
            return(3, cotation_3)
selection_1()
