
def factorielle(n):
    if n==0 | n==1:
        return 1
    return n * factorielle(n-1)

nombre = int(input("entrer un nombre"))
fac = factorielle(nombre)
print(f"le factorielle de {nombre} est : {fac}")