def PileVide():
    return []

def EstVide(pile):
    return len(pile) == 0

def Empiler(pile, element):
    pile.append(element)
    return pile

def Depiler(pile):
    if not EstVide(pile):
        return pile.pop()
    return None

def SommetPile(pile):
    if not EstVide(pile):
        return pile[-1]
    return None
    
def EstChiffre(c):
    if c >= '0' and c <= '9':
        return 1
    return 0

def Convertir(c):
    return int(c)

def Evaluer(expression):
    pile = PileVide()
    elements = expression.split()
    for element in elements:
        if element not in ['+', '-', '*', '/']:
            nombre = int(element)
            Empiler(pile, nombre)
        else:
            operande2 = Depiler(pile)
            operande1 = Depiler(pile)
            if element == '+':
                resultat = operande1 + operande2
            elif element == '-':
                resultat = operande1 - operande2
            elif element == '*':
                resultat = operande1 * operande2
            elif element == '/':
                resultat = operande1 / operande2
            Empiler(pile, resultat)
    return SommetPile(pile)
exp = "17 10 -"
print(f"Résultat: {Evaluer(exp)}")

def EvaluerTexte(Fsrc, Fdest):
    with open(Fsrc, "r") as src, open(Fdest, "w") as dest:
        for ligne in src:
            expr = ligne.strip()
            if expr:
                resultat = Evaluer(expr)
                dest.write(str(resultat) + "\n")


with open('expressions.txt', 'w') as f:
    f.write("17 10 -\n")
    f.write("3 28 7 / +\n")
    f.write("19 6 * 7 -\n")

EvaluerTexte('expressions.txt', 'resultats.txt')
print("\nContenu de 'resultats.txt':")
with open('resultats.txt', 'r') as f:
    print(f.read())




















    
    
    
    