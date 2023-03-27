# Écrire un programme qui affiche dans le terminal un rectangle avec des ‘-’ et des ‘|’ en
# fonction des paramètres d’entrées, (width, height), par exemple :draw_rectangle(10, 3)

# |--------|
# |        |
# |--------|


def draw_rectangle(width, height):
    # Dessiner la première ligne du rectangle avec des "-"
    print("-" * width)

    # Dessiner les lignes suivantes avec des "|" à gauche et à droite et des espaces au milieu
    for i in range(height - 2):
        print("|" + " " * (width - 2) + "|")

    # Dessiner la dernière ligne du rectangle avec des "-"
    print("-" * width)


# Appeler la fonction draw_rectangle() avec une largeur de 10 et une hauteur de 3
draw_rectangle(10, 3)
