# Créer un programme qui demande à l'utilisateur de renseigner une chaîne de caractères
# et qui écrit cette chaine de caractère dans un fichier “output.txt”.

# Demander à l'utilisateur de renseigner une chaîne de caractères
chaine = input("Entrez une chaîne de caractères : ")

# Ouvrir le fichier "output.txt" en mode écriture
with open("output.txt", "w") as fichier:
    # Écrire la chaîne de caractères dans le fichier
    fichier.write(chaine)

print("La chaîne a été écrite dans le fichier 'output.txt'.")
