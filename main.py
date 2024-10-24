from random import shuffle


class Questionnaires:
    datas = [("Quel est la capitale de Madagascar ?", ['Fianarantsoa', 'Toamasina', 'Antananarivo', 'Toliara'],
              'Antananarivo'),
             ("Qui est le président de la republique à Madagascar ?",
              ['Andry Rajoelina', 'Philibert Tsiranana', 'Donald Trump', 'Marc Ravalomanana'], 'Andry Rajoelina'),
             ("Trouvez l'intru...", ['oeil', 'dent', "langue", "peau", 'oreil', 'nez'], 'dent'),
             ("Quel est le contraire de \"inflammable\" ?",
              ["flammable", "ininflammable", "imperméable", "ininflammable", "incombustible"], "incombustible"),
             ("en quel année le Stephen Hawking est décédé ?", ["2018", "2015", "2013", "2020"], "2018"),
             ("dans quel équipe Paul Pogba n'a pas joué", ["Juventus", "Manchester United", "Chelsea"], "Chelsea"),
             ("laquelle de ces maladies est incurable ?", ["SIDA", 'Tuberculose', "Peste", "Choléra", "Corona virus"],
              "SIDA"),
             ("Quelle est le premier langage de programmation ?",["python","Langage C","Ruby", "Java"],"Langage C"),
             ("Quel âge a la terre ?",["1,4 Milliards d'année","100 Millions d'année","60 Milliards d'année","4 Milles ans"],"1,4 Milliards d'année")

             ]


    def __init__(self):
        self.stop = False
        shuffle(self.datas)
        self.nb_points = 0
        self.nb_parties= 0
        for data in self.datas:
            if not self.stop:
                self.nb_parties +=1
                self.poser_question(data[0], data[1],data[2])
                print("points : "+str(self.nb_points)+"/"+str(self.nb_parties))
    def poser_question(self,question,liste_reponses,reponse):
        shuffle(liste_reponses)
        num_reponse = liste_reponses.index(reponse)
        print(question.title())
        i = 1
        for item in liste_reponses:
            print(f"\t{i} - {item}")
            i+=1
        reponse_utilisateur = self.recuperer_reponse_utililisateur() #pour récuperer l'input en 'int'
        if reponse_utilisateur ==-1:print("le jeux a été quitté")
        elif reponse_utilisateur-1 == num_reponse:
            print("vrai\n")
            self.nb_points+=1
        else:print("faux\n")

    def recuperer_reponse_utililisateur(self):
        reponse = input("votre réponse :")
        if reponse =="q":
            self.stop = True
            return -1
        else:

            while not reponse.isdigit():reponse = input("votre réponse :")
            return int(reponse)


Questionnaires()

