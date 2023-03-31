# Importation des modules nécessaires
import pygame
from pygame.locals import *

# Initialisation de Pygame
pygame.init()

# Définition des variables globales
WINDOW_SIZE = (600, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CROSS_IMAGE = pygame.image.load("cross.png")
CROSS_IMAGE = pygame.transform.scale(
    CROSS_IMAGE, (WINDOW_SIZE[0] // 3, WINDOW_SIZE[1] // 3))
CIRCLE_IMAGE = pygame.image.load("circle.png")
CIRCLE_IMAGE = pygame.transform.scale(
    CIRCLE_IMAGE, (WINDOW_SIZE[0] // 3, WINDOW_SIZE[1] // 3))

# Création de la grille du jeu
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

# Création de la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TicTacToe1337")

# Fonction pour vérifier si un joueur a gagné


def check_win(player):
    # Vérifier les lignes
    for row in grid:
        if row.count(player) == 3:
            return True

    # Vérifier les colonnes
    for col in range(3):
        if grid[0][col] == player and grid[1][col] == player and grid[2][col] == player:
            return True

    # Vérifier les diagonales
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True

    return False

# Fonction pour vérifier si la grille est pleine


def check_draw():
    for row in grid:
        if 0 in row:
            return False
    return True


# Boucle principale
running = True
player = 1
while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            # Détection d'un clic de souris
            x, y = event.pos
            row = y // (WINDOW_SIZE[1] // 3)
            col = x // (WINDOW_SIZE[0] // 3)
            if grid[row][col] == 0:
                # Mise à jour de la grille
                grid[row][col] = player
                # Changement de joueur
                if player == 1:
                    player = 2
                else:
                    player = 1

                # Affichage du joueur courant
                print(f"C'est au tour du joueur {player} de jouer.")

                if check_win(player):
                    print(f"Le joueur {player} a gagné !")
                    running = False
                elif check_draw():
                    print("Match nul !")
                    running = False

    # Dessin de la grille
    screen.fill(WHITE)
    for i in range(1, 3):
        # Dessin des lignes horizontales
        pygame.draw.line(
            screen, BLACK, (0, i * WINDOW_SIZE[1] // 3), (WINDOW_SIZE[0], i * WINDOW_SIZE[1] // 3), 5)
        # Dessin des lignes verticales
        pygame.draw.line(
            screen, BLACK, (i * WINDOW_SIZE[0] // 3, 0), (i * WINDOW_SIZE[0] // 3, WINDOW_SIZE[1]), 5)

    # Dessin des croix et des ronds
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 1:
                # Affichage de la croix
                x = col * (WINDOW_SIZE[0] // 3)
                y = row * (WINDOW_SIZE[1] // 3)
                screen.blit(CROSS_IMAGE, (x, y))
            elif grid[row][col] == 2:
                # Affichage du rond
                x = col * (WINDOW_SIZE[0] // 3)
                y = row * (WINDOW_SIZE[1] // 3)
                screen.blit(CIRCLE_IMAGE, (x, y))

    # Rafraîchissement de l'écran
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
