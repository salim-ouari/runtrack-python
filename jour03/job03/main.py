# Écrire un programme qui parcourt le fichier “data.txt” et qui compte le nombre
# d'occurrence de chaque lettre (Minuscules et Capitales comptent pour la même lettre).
# A l’aide du module MatPlotLib, générer un histogramme représentant le pourcentage
# d’apparition de chaque lettre.

import matplotlib.pyplot as plt


# Ouvrir le fichier en mode lecture
with open('data.txt', 'r') as f:
    data = f.read()

# Convertir toutes les lettres en minuscules
data = data.lower()

# Initialiser un dictionnaire vide pour stocker le nombre d'occurrences de chaque lettre
occurrences = {}

# Parcourir chaque lettre dans la chaîne de caractères
for letter in data:
    # Si la lettre est une lettre de l'alphabet
    if letter.isalpha():
        # Si la lettre est déjà dans le dictionnaire, incrémenter son compteur
        if letter in occurrences:
            occurrences[letter] += 1
        # Sinon, initialiser son compteur à 1
        else:
            occurrences[letter] = 1

# Calculer le nombre total de lettres
total = sum(occurrences.values())

# Initialiser deux listes pour stocker les lettres et leurs pourcentages d'apparition
letters = []
percentages = []

# Parcourir chaque lettre dans le dictionnaire d'occurrences
for letter, count in occurrences.items():
    # Ajouter la lettre à la liste des lettres
    letters.append(letter)
    # Calculer le pourcentage d'apparition de la lettre et l'ajouter à la liste des pourcentages
    percentage = (count / total) * 100
    percentages.append(percentage)

# Créer un histogramme des pourcentages d'apparition de chaque lettre
plt.bar(letters, percentages)
plt.title('Pourcentage d\'apparition de chaque lettre')
plt.xlabel('Lettre')
plt.ylabel('Pourcentage')
plt.show()
