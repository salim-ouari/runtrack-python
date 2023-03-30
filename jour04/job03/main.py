# Créer un programme qui modélise un plateau de jeu, carré, de n x n cases. Placez sur ce
# plateau n dames de jeu d'échecs, de manière à ce qu’aucune dame ne puisse se
# “prendre”, quand cela est possible. La valeur de n est renseignée par l’utilisateur. Quand
# cela est possible, le programme devra afficher dans le terminal le plateau de jeu avec le
# caractère ‘O’ pour les cases vides et le caractère ‘X’ pour représenter les dames.

def can_place(board, row, col):
    # Vérifier la colonne
    for i in range(row):
        if board[i][col] == 'X':
            return False

    # Vérifier la diagonale supérieure gauche
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'X':
            return False
        i -= 1
        j -= 1

    # Vérifier la diagonale supérieure droite
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'X':
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if can_place(board, row, col):
            board[row][col] = 'X'
            if solve_n_queens(board, row+1):
                return True
            board[row][col] = 'O'

    return False


n = int(input("Entrez la taille du plateau de jeu : "))

# Créer un plateau de jeu vide
board = [['O' for j in range(n)] for i in range(n)]

# Résoudre le problème des n reines
if solve_n_queens(board, 0):
    # Afficher le plateau de jeu avec les reines
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
else:
    print("Aucune solution possible")
