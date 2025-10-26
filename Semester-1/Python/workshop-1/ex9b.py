from random import randint
goal = randint(1, 1000)
print(goal)
max_essais = 8
nb_essais = 0

print(f"Entrer un nombre entre 1 et 1000 (max {max_essais} essais):", end="")

while nb_essais < max_essais:
    essai = int(input())
    nb_essais += 1
    if essai > goal:
        print("Le nombre est plus petit")
        if nb_essais < max_essais:
            print("Nouvel essai:", end="")
    elif essai < goal:
        print("Le nombre est plus grand")
        if nb_essais < max_essais:
            print("Nouvel essai:", end="")
    else:
        print(f"Bravo! Vous avez trouvé en {nb_essais} essais")
        break
if nb_essais == max_essais and essai != goal:
    print(f"game over! Le nombre était {goal}")