from random import randint
goal = randint(1, 1000)
print(goal)
while True:
        essai = int(input("Entrer un nombre entre 1 et 1000:"))
        if essai > goal:
            print("Le nombre est plus petit")
            print("Nouvel essai:", end="")
        elif essai < goal:
            print("Le nombre est plus grand")
            print("Nouvel essai:", end="")
        else:
            print("Bravo")
            break