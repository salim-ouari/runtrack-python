# Écrire un programme qui parcourt le fichier “data.txt” et qui compte le nombre de mots
# de chaque taille. A l’aide du module MatPlotLib, générer un histogramme représentant
# le pourcentage d’apparition de chaque taille de mot.

import matplotlib.pyplot as plt

# Ouvrir le fichier et lire son contenu
with open('data.txt', 'r') as file:
    content = file.read()

# Séparer le contenu en mots en utilisant les espaces comme séparateurs
words = content.split()

# Initialiser un dictionnaire pour stocker le nombre de mots de chaque taille
word_counts = {}

# Compter le nombre de mots de chaque taille
for word in words:
    length = len(word)
    if length in word_counts:
        word_counts[length] += 1
    else:
        word_counts[length] = 1

# Calculer le pourcentage d'apparition de chaque taille de mot
total_words = len(words)
percentages = [count/total_words*100 for count in word_counts.values()]

# Générer l'histogramme
plt.bar(word_counts.keys(), percentages)
plt.xlabel('Taille des mots')
plt.ylabel('Pourcentage d\'apparition')
plt.title('Histogramme de la taille des mots')
plt.show()
