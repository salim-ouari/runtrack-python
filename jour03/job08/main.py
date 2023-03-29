# Écrire un programme qui parcourt le fichier “data.txt” et qui compte le nombre
# d'occurrence de chaque lettre (Minuscules et Capitales comptent pour la même lettre)
# en début de mot. A l’aide du module MatPlotLib, générer un histogramme représentant
# le pourcentage de présence de chaque lettre en début de mot.

import matplotlib.pyplot as plt
import string

# Ouvrir le fichier et lire son contenu
with open('data.txt', 'r') as file:
    content = file.read()

# Séparer le contenu en mots en utilisant les espaces comme séparateurs
words = content.split()

# Initialiser un dictionnaire pour stocker le nombre d'occurrences de chaque lettre en début de mot
letter_counts = {}
for letter in string.ascii_lowercase:
    letter_counts[letter] = 0

# Compter le nombre d'occurrences de chaque lettre en début de mot
total_words = len(words)
for word in words:
    if word[0].isalpha() and word[0].lower() in letter_counts:
        letter_counts[word[0].lower()] += 1

# Calculer le pourcentage de présence de chaque lettre en début de mot
percentages = [count/total_words*100 for count in letter_counts.values()]

# Générer l'histogramme
plt.bar(letter_counts.keys(), percentages)
plt.xlabel('Lettres')
plt.ylabel('Pourcentage de présence en début de mot')
plt.title('Histogramme de la présence des lettres en début de mot')
plt.show()
