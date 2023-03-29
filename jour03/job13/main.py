# Écrire un programme qui parcourt le fichier “data.txt” et qui, pour chaque lettre, compte
# le nombre d'occurrence de la lettre suivante. Générer, ensuite, un graphique de courbes
# superposées, une courbe par lettre, montrant le pourcentage d’apparition de chaque
# lettre la suivant.
# Par exemple, pour le a: a(2%), b(5%), c(2.3%) .... pour le b: a(3%), b(0%), c(1%), ...

import collections
import matplotlib.pyplot as plt

# Chaîne de texte à analyser
texte = "Ce texte est un exemple d'analyse de lettres suivantes."

# Comptage des lettres suivantes
resultats = {}
for i in range(len(texte)-1):
    lettre = texte[i].lower()
    suivante = texte[i+1].lower()
    if lettre not in resultats:
        resultats[lettre] = collections.Counter()
    resultats[lettre][suivante] += 1

# Génération du graphique
plt.figure(figsize=(10, 6))
data = []
labels = []
for lettre, compte in resultats.items():
    total = sum(compte.values())
    pourcentages = [count/total * 100 for lettre2, count in compte.items()]
    data.append(pourcentages)
    labels.append(lettre)
plt.boxplot(data, labels=labels, showmeans=True)
plt.xlabel("Lettres")
plt.ylabel("Pourcentage d'apparition de la lettre suivante")
plt.show()
