def draw_triangle(height):
    for i in range(height):
        # Dessiner les espaces à gauche du triangle
        print(" " * (height - i - 1), end="")
        # Dessiner la partie supérieure du triangle
        if i == 0:
            print("/\\")
        elif i == height - 1:
            print("/" + "_" * (2 * height - 3) + "\\")
        else:
            print("/" + " " * (2 * i - 1) + "\\ ")


# Appeler la fonction draw_triangle() avec la hauteur 7
draw_triangle(7)
