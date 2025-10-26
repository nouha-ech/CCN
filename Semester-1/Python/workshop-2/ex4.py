def Occur(text, lettre):
    compt = 0
    for i in range(len(text)):
        if text[i] == lettre:
            compt += 1
    return compt

def Occur2(text, lettre):
    if text == "":
        return 0
    compte = 1 if text[0] == lettre else 0
    return compte + Occur2(text[1:], lettre)

texte = "bonjour"
lettre = "o"

print(Occur(texte, lettre))
print(Occur2(texte, lettre))
