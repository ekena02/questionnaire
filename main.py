class Questionnaires:
    def __init__(self,question,liste_reponses,reponse):
        self.question = question
        self.liste_reponse = liste_reponses
        self.reponse = reponse
        self.poser_question(self.question, self.liste_reponse,self.reponse)

    def poser_question(self,question,liste_reponses,reponse):
        num_reponse = liste_reponses.index(reponse)
        print(question)
        i = 1
        for item in liste_reponses:
            print(f"\t{i} - {item}")
            i+=1
        reponse_utilisateur = self.recuperer_reponse_utililisateur() #pour récuperer l'input en 'int'
        if reponse_utilisateur-1 == num_reponse:print("vrai\n")
        else:print("faux\n")

    def recuperer_reponse_utililisateur(self):
        reponse = input("votre réponse :")
        while not reponse.isdigit():reponse = input("votre réponse :")
        return int(reponse)




questionnaire1 = Questionnaires("quel est la capitale de Madagascar ?",
                               ('Fianarantsoa','Toamasina','Antananarivo','Toliara'),'Antananarivo')

questionnaire2 = Questionnaires("Qui est le président de la republique à Madagascar ?",
                               ('Andry Rajoelina','Philibert Tsiranana','Donald Trump','Marc Ravalomanana'),'Andry Rajoelina')

