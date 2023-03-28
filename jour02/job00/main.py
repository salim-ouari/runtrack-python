# Créez une classe “Personne” avec les attributs “nom”, “prenom”. Ajoutez une méthode
# “SePresenter()” qui affichera dans le terminal le nom et le prénom de la personne.
# Ajoutez aussi un constructeur prenant en paramètres de quoi donner des valeurs
# initiales aux attributs “nom” et “prenom”. Instanciez plusieurs personnes avec les
# valeurs de construction de votre choix et faites appel à la méthode “SePresenter()” afin
# de vérifier que tout fonctionne correctement. Ajouter un “accesseur” et un “mutateur”
# pour chacun des attributs.

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je m'appelle", self.nom, self.prenom)

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getPrenom(self):
        return self.prenom

    def setPrenom(self, prenom):
        self.prenom = prenom


# Instancier plusieurs personnes
personne1 = Personne("Dupont", "Jean")
personne2 = Personne("Martin", "Julie")
personne3 = Personne("Lefebvre", "Luc")

# Appeler la méthode SePresenter() pour chaque personne
personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()

# Utiliser les mutateurs pour changer les valeurs des attributs nom et prenom
personne1.setNom("Durand")
personne2.setPrenom("Sophie")


# Utiliser les accesseurs pour afficher les nouvelles valeurs des attributs nom et prenom
print(personne1.getNom())  # Durand
print(personne2.getPrenom())  # Sophie
