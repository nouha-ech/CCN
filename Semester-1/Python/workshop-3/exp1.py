# 1/a
def occurences(lettre,mot):
 m=[m for m in mot]
 f = m.count(lettre)
 return f
mot="south"
t=occurences("s",mot)
print("l'occurence de s dans le mot est ",t, "fois")
