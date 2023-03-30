# Créer un programme demandant à l’utilisateur de renseigner un nombre entier. Votre
# programme devra calculer x^n, où n est le nombre fourni par l’utilisateur, sans utiliser de
# fonction autre que les vôtres. Attention, vous ne devez utiliser ni while, ni for, ni foreach
# ni ... boucle. Seulement de la récursivité.

def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x, n//2) * power(x, n//2)
    else:
        return x * power(x, n-1)


x = int(input("Entrez la valeur de x : "))
n = int(input("Entrez la valeur de n : "))
print(x, "^", n, "=", power(x, n))
