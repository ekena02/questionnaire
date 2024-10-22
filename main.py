from random import shuffle


class Questionnaires:
    datas = [("quel est la capitale de Madagascar ?", ['Fianarantsoa', 'Toamasina', 'Antananarivo', 'Toliara'],
              'Antananarivo'),
             ("Qui est le président de la republique à Madagascar ?",
              ['Andry Rajoelina', 'Philibert Tsiranana', 'Donald Trump', 'Marc Ravalomanana'], 'Andry Rajoelina'),
             ("trouvez l'intru...", ['oeil', 'dent', "langue", "peau", 'oreil', 'nez'], 'dent'),
             ("quel esr le contraire de \"inflammable\" ?",
              ["flammable", "ininflammable", "imperméable", "ininflammable", "incombustible"], "incombustible"),
             ("en quel année le Stephen Hawking est décédé ?", ["2018", "2015", "2013", "2020"], "2018"),
             ("dans quel équipe Paul Pogba n'a pas joué", ["Juventus", "Manchester United", "Chelsea"], "Chelsea"),
             ("laquelle de ces maladies est incurable ?", ["SIDA", 'Tuberculose', "Peste", "Choléra", "Corona virus"],
              "SIDA")]

    def __init__(self):
        self.stop = False
        shuffle(self.datas)
        for data in self.datas:
            if not self.stop:
                self.poser_question(data[0], data[1],data[2])
    def poser_question(self,question,liste_reponses,reponse):
        shuffle(liste_reponses)
        num_reponse = liste_reponses.index(reponse)
        print(question.title())
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





"""datas = [("quel est la capitale de Madagascar ?",['Fianarantsoa','Toamasina','Antananarivo','Toliara'],'Antananarivo'),
         ("Qui est le président de la republique à Madagascar ?",['Andry Rajoelina','Philibert Tsiranana','Donald Trump','Marc Ravalomanana'],'Andry Rajoelina'),
         ("trouvez l'intru...",['oeil','dent',"langue","peau",'oreil','nez'],'dent'),
         ("quel esr le contraire de \"inflammable\" ?",["flammable","ininflammable","imperméable","ininflammable","incombustible"],"incombustible"),
         ("en quel année le Stephen Hawking est décédé ?",["2018","2015","2013","2020"],"2018"),
         ("dans quel équipe Paul Pogba n'a pas joué",["Juventus","Manchester United","Chelsea"],"Chelsea"),
         ("laquelle de ces maladies est incurable ?",["SIDA",'Tuberculose',"Peste","Choléra","Corona virus"],"SIDA")]


shuffle(datas)

for data in datas:Questionnaires(data[0],data[1],data[2])"""
#print(Questionnaires.count)
Questionnaires()

