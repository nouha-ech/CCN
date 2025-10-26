# 1/a
def encrypteLettre(lettre, cle):
    if lettre.isalpha():
        if lettre.isupper():
            code = ord(lettre) - ord('A')
            code = (code + cle) % 26
            return chr(code + ord('A'))
        else:
            code = ord(lettre) - ord('a')
            code = (code + cle) % 26
            return chr(code + ord('a'))
    else:
        return lettre
lettre= "n"
cle=7
print(encrypteLettre(lettre, cle))
# 1/b
def encrypteMot(mot, cle):
    res = ""
    for i in range(len(mot)):
        lettre = mot[i]
        res += encrypteLettre(lettre, cle)
    return res

mot= "nouha"
cle=10
print(encrypteMot(mot, cle))
# 1/c
def encrypte(texte, cle):
    res = ""
    for i in range(len(texte)):
        res += encrypteLettre(texte[i], cle)
    return res

phrase= "je m'appelle nouha"
cle=11
print(encrypte(phrase, cle))

# 2
def decrypte(texteCache, cle):
     return encrypte(texteCache, -cle)
     
text= "up x'laapwwp yzfsl"
print(decrypte(text, 11))

# 3

def devineCle(texte):
    max_e = 0
    topcle = 0
    for cle in range(26):
        decoded = decrypte(texte, cle)
        nb_e = decoded.count('e')
        if nb_e > max_e:
            max_e = nb_e
            topcle = cle
    return topcle
    
print(devineCle("up x'laapwwp yzfsl"))
    
# 4
def letplusfreq(texte):
    texte = texte.lower()
    lettres = [c for c in texte if c.isalpha()]
    return max(set(lettres), key=lettres.count)

def devineCle2(texte):
    lettre = letplusfreq(texte)
    return (ord(lettre) - ord('e')) % 26
    

print(devineCle2("hiobucfuuu"))

    
    
    
    