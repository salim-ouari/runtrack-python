#
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)


class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        print("Oeuvre de :", self.nom, self.prenom)
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre


auteur = Auteur("Hugo", "Victor")
livre1 = auteur.ecrireUnLivre("Les Misérables")
livre2 = auteur.ecrireUnLivre("Notre-Dame de Paris")

livre1.print()
livre2.print()

auteur.listerOeuvre()
