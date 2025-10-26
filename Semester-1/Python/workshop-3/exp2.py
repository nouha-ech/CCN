from collections import Counter

def occurence2(lettre,mot):
    dic= Counter(mot)
    return dic.get(lettre)
l="n"
mot="nouha"
ff= occurence2(l,mot)
print("occurence de ", l, "dans", mot,"est",ff, "fois")
