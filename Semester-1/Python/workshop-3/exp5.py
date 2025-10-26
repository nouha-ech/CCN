from random import randint
from collections import Counter
jetons = { "a" :9 , "b" :2, "c" :2 , "d" :3 , "e" :15 , "f" :2 , "g" :2 , "h" :2 , "i" :8 , "j":1,
 "k" :1 , "l" :5 , "m" :3 , "n" :6 , "o" :6 , "p" :2 , "q" :1, "r" :6 , "s" :6 , "t" :6 ,
"u" :6 , "v" :2 , "w" :1 , "x" :1 , "y" :1, "z" :1}
#jetons
L=[]
for l in jetons:
    L= L + [l] * jetons[l]
def pioch():
    Pio=[]
    for i in range(7):
        n=randint(0,99)
        Pio.append(L[n])
    n= Counter(Pio)
    return dict(n)
    
pioch()


    
    


