# Écrire un programme qui demande à l’utilisateur de fournir une première chaîne de
# caractères, puis une seconde. Le programme affiche 1 si les 2 chaines sont identiques
# ou 0 si les chaînes ne sont pas identiques. Les chaînes ne sont constituées que de
# lettres minuscules. La deuxième chaîne de caractères peut contenir un ou plusieurs ‘ * ‘.
# Chaque ‘ * ‘ peut remplacer 0 ou plusieurs caractères. Par exemple, si la chaîne 1 est
# “laplateforme” et la chaine 2 “lap*”, le programme affiche 1 car l’ ‘ * ‘ remplace ‘
# lateforme ‘. Si la chaîne 1 est “laplateforme” et la chaîne 2 “l*a*pla*te*form***e” le
# programme renvoie 1 car les ‘ * ‘ ne remplace rien.

chaine1 = input(
    "Entrez la première chaîne de caractères (lettres minuscules uniquement) : ")
chaine2 = input(
    "Entrez la deuxième chaîne de caractères (lettres minuscules et/ou caractères * uniquement) : ")

# Vérification des caractères autorisés dans les chaînes
if not all(c.islower() or c == '*' for c in chaine1+chaine2):
    print("Les chaînes doivent être constituées uniquement de lettres minuscules et/ou du caractère *")
else:
    # Remplacement des caractères * par des expressions régulières pour la recherche
    chaine2_regex = chaine2.replace('*', '.*')

    # Recherche de correspondance
    import re
    if re.fullmatch(chaine2_regex, chaine1):
        print(1)
    else:
        print(0)
