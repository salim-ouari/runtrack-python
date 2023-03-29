# Créer un programme qui demande à l’utilisateur de renseigner un nombre entier. Le
# programme devra alors parcourir le contenu du fichier “data.txt” compter le nombre de
# mots de la taille renseignée qui s’y trouvent.

# Demander à l'utilisateur de renseigner un nombre entier
n = int(input("Entrez un nombre entier : "))

# Ouvrir le fichier "data.txt" en mode lecture
with open("data.txt", "r") as f:
    # Initialiser un compteur pour le nombre de mots de taille n
    count = 0
    # Parcourir toutes les lignes du fichier
    for line in f:
        # Séparer la ligne en mots
        words = line.split()
        # Parcourir tous les mots de la ligne
        for word in words:
            # Vérifier si le mot a une longueur de n caractères
            if len(word) == n:
                # Si oui, incrémenter le compteur
                count += 1

# Afficher le nombre de mots de taille n trouvés dans le fichier
print("Le fichier contient", count, "mots de", n, "caractères.")
