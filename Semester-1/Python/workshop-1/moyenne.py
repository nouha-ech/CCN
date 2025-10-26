n= int(input("entrer le nombre de note que vous voulez calculer la moyenne: "))
S=0
moy=0
for k in range(1,n+1):
    note = float(input("entrer une note: "))
    S= S+note
moy = S/n
print(f"la moyenne des {n} notes que vous avez entré est {moy:.2f}")


