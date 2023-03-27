# Créer un programme qui demandera à l’utilisateur de renseigner un mot et un seul, sans
# espace ni aucun autre caractère que les 26 lettres de l’alphabet (sans accent ni
# majuscule).
# Votre programme devra modifier ce mot, en y changeant de place certains caractères
# (ou tous) afin de donner un mot plus “loin” dans l’ordre alphabétique que le mot
# renseigné par l'utilisateur.
# Attention: Le nouveau mot doit être le mot le plus proche possible, dans l’ordre
# alphabétique, du mot original !
# Par exemple, “abcde” donnerait “abced”. “acedb” est aussi “valide” mais n’est PAS le
# plus proche du mot original dans l’ordre alphabétique.

def changer_mot(original):
    # Vérifier que le mot est valide
    if not original.isalpha() or not original.islower():
        return "Le mot doit être composé uniquement de lettres minuscules de l'alphabet."

    # Convertir le mot en une liste de lettres
    lettres = list(original)

    # Parcourir la liste de droite à gauche pour trouver la première paire de lettres
    # où la première lettre est inférieure à la suivante
    i = len(lettres) - 2
    while i >= 0 and lettres[i] >= lettres[i+1]:
        i -= 1

    # Si on a parcouru toute la liste, le mot est déjà le plus grand possible
    if i < 0:
        return "Le mot est déjà le plus grand possible dans l'ordre alphabétique."

    # Parcourir la fin de la liste à la recherche de la plus petite lettre supérieure à lettres[i]
    j = len(lettres) - 1
    while lettres[j] <= lettres[i]:
        j -= 1

    # Échanger lettres[i] et lettres[j]
    lettres[i], lettres[j] = lettres[j], lettres[i]

    # Inverser l'ordre des lettres après i
    lettres[i+1:] = lettres[:i:-1]

    # Convertir la liste de lettres en un mot et le renvoyer
    return ''.join(lettres)


# Demander à l'utilisateur de renseigner un mot
mot = input("Entrez un mot : ")

# Changer le mot
nouveau_mot = changer_mot(mot)

# Afficher le nouveau mot
print("Le nouveau mot est :", nouveau_mot)
