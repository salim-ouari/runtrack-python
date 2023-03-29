# Créer un programme qui parcourt le contenu du fichier “data.txt” et qui compte le
# nombre de mots (sans caractère spéciaux) qui s’y trouvent.

import re

# Ouvrir le fichier en mode lecture
with open('data.txt', 'r') as file:
    text = file.read()

# Remplacer tous les caractères spéciaux par des espaces
text = re.sub(r'[^\w\s]', ' ', text)

# Séparer le texte en une liste de mots
words = text.split()

# Afficher le nombre de mots
print("Nombre de mots : ", len(words))

#   1176525
