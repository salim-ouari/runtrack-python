#
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        print(f"Liste des livres écrits par {self.nom} {self.prenom}:")
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return self.titre


class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        print(f"Liste des livres en possession de {self.nom} {self.prenom}:")
        for livre in self.collection:
            print(livre.titre)


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite
                print(
                    f"{quantite} exemplaire(s) du livre '{titre}' de l'auteur {auteur.nom} ont été ajouté(s) au catalogue de la bibliothèque.")
                return
        print(
            f"Le livre '{titre}' de l'auteur {auteur.nom} n'existe pas dans son oeuvre.")

    def inventaire(self):
        print(f"Catalogue de la bibliothèque '{self.nom}':")
        for livre, quantite in self.catalogue.items():
            print(f"{livre}: {quantite} exemplaires")

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            self.catalogue[titre] -= 1
            livre = Livre(titre, None)
            client.collection.append(livre)
            print(f"{client.nom} {client.prenom} a loué le livre '{titre}'.")
        else:
            print(f"Le livre '{titre}' n'est pas disponible en ce moment.")

    def rendreLivres(self, client):
        for livre in client.collection:
            if livre.titre in self.catalogue:
                self.catalogue[livre.titre] += 1
            else:
                self.catalogue[livre.titre] = 1
        print(f"{client.nom} {client.prenom} a rendu tous ses livres.")


class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)


class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        for livre in self.collection:
            print(livre.titre)


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite
                return True
        return False

    def inventaire(self):
        for titre, quantite in self.catalogue.items():
            print(titre, quantite)

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            livre = Livre(titre, self)
            self.catalogue[titre] -= 1
            client.collection.append(livre)
            return True
        else:
            return False

    def rendreLivres(self, client):
        for livre in client.collection:
            if livre.titre in self.catalogue:
                self.catalogue[livre.titre] += 1
            else:
                self.catalogue[livre.titre] = 1
        client.collection.clear()


# Création d'auteurs et de leurs livres
auteur1 = Auteur("Martin", "George R. R.")
livre1 = auteur1.ecrireUnLivre("Game of Thrones")
livre2 = auteur1.ecrireUnLivre("A Clash of Kings")

auteur2 = Auteur("Rowling", "J.K.")
livre3 = auteur2.ecrireUnLivre("Harry Potter and the Philosopher's Stone")
livre4 = auteur2.ecrireUnLivre("Harry Potter and the Chamber of Secrets")

# Création de bibliothèques
biblio1 = Bibliotheque("Bibliothèque municipale")
biblio2 = Bibliotheque("Bibliothèque universitaire")

# Achat de livres par les bibliothèques
biblio1.acheterLivre(auteur1, "Game of Thrones", 5)
biblio1.acheterLivre(auteur1, "A Clash of Kings", 3)
biblio2.acheterLivre(auteur2, "Harry Potter and the Philosopher's Stone", 2)
biblio2.acheterLivre(auteur2, "Harry Potter and the Chamber of Secrets", 1)

# Création de clients
client1 = Client("Dupont", "Jean")
client2 = Client("Durand", "Marie")

# Location de livres par les clients
biblio1.louer(client1, "Game of Thrones")
biblio1.louer(client1, "A Clash of Kings")
biblio2.louer(client2, "Harry Potter and the Philosopher's Stone")
biblio2.louer(client2, "Harry Potter and the Chamber of Secrets")

print("nombre de livre à rendre", len(
    client1.collection) + len(client2.collection))
biblio1.rendreLivres(client1)
biblio2.rendreLivres(client2)

print("nombre de livres total dans les bibliothèques", biblio1.catalogue["Game of Thrones"] + biblio1.catalogue["A Clash of Kings"] +
      biblio2.catalogue["Harry Potter and the Philosopher's Stone"] + biblio2.catalogue["Harry Potter and the Chamber of Secrets"])
biblio1.inventaire()
biblio2.inventaire()


client1.inventaire()
client2.inventaire()
