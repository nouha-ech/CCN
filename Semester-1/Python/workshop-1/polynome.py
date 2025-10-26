x= int(input("enter x: "))
n= int(input("enter n: "))
S=0
for k in range(1,n+1):
    S=S+k*(x**k)
print(f"la valeur de la somme est {S}")