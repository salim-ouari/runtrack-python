# Créer un programme qui lit le contenu du fichier “output.txt” et qui l’affiche dans le
# terminal.

with open("output.txt", "r") as f:
    content = f.read()
    print(content)
