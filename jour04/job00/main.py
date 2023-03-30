#
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)


number = int(input("Entrez un nombre entier : "))
print("La factorielle de", number, "est", recursive_factorial(number))
