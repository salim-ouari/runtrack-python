# Vous allez créer dans ce Job un jeu de puissance 4 sur plateau de taille variable ainsi
# qu’un algorithme qui sera capable de jouer des coups mesurés.
# Commencez par créer une classe “Board” prenant en paramètres de construction deux
# entiers i et j. Créez un attribut, sous la forme d’un tableau à 2 dimensions, représentant
# un plateau de jeu en deux dimensions de taille i x j. Ce tableau représente:
# - les cases vides par des O
# - les jetons jaunes par des J
# - les jetons rouges par des R
# Créez une méthode “play” qui prend en paramètres un nombre entier ainsi qu’une chaine
# de caracteres pouvant être “rouge” ou “jaune”. Le nombre entier correspond à la colonne
# dans laquelle un jeton de jeu est inséré et la couleur correspond à la couleur du joueur
# jouant ce jeton. Après un coup, tenez à jour votre plateau de jeu en plaçant le jeton le
# plus bas possible dans la colonne où il a été joué.
# Ajouter une méthode “print” affichant dans le terminal l’état du plateau de jeu.
# Implémentez le déroulement d’une partie en demandant aux joueurs humains de jouer à
# tour de rôle en choisissant la colonne dans laquelle ils souhaitent insérer leurs jetons.
# Le premier joueur à aligner 4 jetons de sa couleur gagne la partie et reçoit 100 000 euros

class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.board = [['O' for _ in range(j)] for _ in range(i)]

    def play(self, col, color):
        if col < 0 or col >= self.j:
            print("Colonne invalide, veuillez choisir une colonne entre 0 et 6")
            return False
        for row in range(self.i-1, -1, -1):
            if self.board[row][col] == 'O':
                self.board[row][col] = color[0]
                return True
        print("Colonne pleine !!")
        return False

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def check_win(self, color):
        # check horizontal
        for row in range(self.i):
            for col in range(self.j-3):
                if self.board[row][col] == color[0] and self.board[row][col+1] == color[0] and self.board[row][col+2] == color[0] and self.board[row][col+3] == color[0]:
                    return True

        # check vertical
        for row in range(self.i-3):
            for col in range(self.j):
                if self.board[row][col] == color[0] and self.board[row+1][col] == color[0] and self.board[row+2][col] == color[0] and self.board[row+3][col] == color[0]:
                    return True

        # check diagonal
        for row in range(self.i-3):
            for col in range(self.j-3):
                if self.board[row][col] == color[0] and self.board[row+1][col+1] == color[0] and self.board[row+2][col+2] == color[0] and self.board[row+3][col+3] == color[0]:
                    return True
                if self.board[row+3][col] == color[0] and self.board[row+2][col+1] == color[0] and self.board[row+1][col+2] == color[0] and self.board[row][col+3] == color[0]:
                    return True

        return False


board = Board(6, 7)  # créer un plateau de 6 lignes et 7 colonnes
current_player = 'rouge'  # le joueur rouge commence la partie
winner = None  # variable pour stocker le gagnant de la partie

while not winner:
    # demander à l'utilisateur de saisir une colonne
    col = int(input(
        f"{current_player}, dans quelle colonne voulez-vous insérer votre jeton ? de 0 à 6 "))

    # insérer le jeton sur le plateau
    if board.play(col, current_player):
        board.print()  # afficher l'état actuel du plateau
        # vérifier si le joueur a gagné
        if board.check_win(current_player):
            winner = current_player
        # passer le tour au joueur suivant
        current_player = 'jaune' if current_player == 'rouge' else 'rouge'

# afficher le gagnant
print(
    f"Félicitations, {winner} a gagné la partie voici le chèque 100.000 euros !")
