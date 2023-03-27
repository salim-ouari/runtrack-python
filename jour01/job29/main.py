# Luke Skywalker, un professeur de Math, fait passer un test et décide de noter ses élèves
# sur une échelle allant de 0 à 100 inclus.
# Si un étudiant obtient moins de 40 sur 100, il échoue au test.
# S'il a plus de 40, il réussit le test. Luke est un professeur fort sympathique et décide
# donc d’arrondir à la hausse les notes des étudiants ayant réussi le test. Mais Luke n’est
# quand même pas trop gentil. Cet arrondi à la hausse ne bénéficiera qu’aux étudiants
# remplissant certains critères car, tout de même, il ne faut pas exagérer, sans blague.
# Le critère est simple: Si un étudiant a eu une note de moins de strictement 3 points de
# son prochain multiple de 5, alors sa note est arrondie à ce multiple de 5. Par exemple,
# un 83 sera arrondi à 85 alors qu’un 82 restera un 82.
# Pour simplifier le travail de Luke, écrivez une fonction qui prend en paramètre une liste
# de notes et qui renvoie une liste de notes, arrondies comme il se doit, quand cela est
# nécessaire.

def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            prochain_multiple_de_5 = ((note // 5) + 1) * 5
            difference = prochain_multiple_de_5 - note
            if difference < 3:
                notes_arrondies.append(prochain_multiple_de_5)
            else:
                notes_arrondies.append(note)
    return notes_arrondies


notes = [67, 82, 73, 91, 38, 59]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)  # Output: [67, 82, 75, 90, 38, 60]
