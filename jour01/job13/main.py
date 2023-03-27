# Demander à l'utilisateur de saisir cinq nombres entiers
nombres = []
for i in range(5):
    nombre = int(input("Entrez un nombre entier : "))
    nombres.append(nombre)

# Trier la liste de nombres par ordre croissant
nombres.sort()

# Afficher les nombres triés dans le terminal
print("Les nombres triés par ordre croissant sont : ")
for nombre in nombres:
    print(nombre)
