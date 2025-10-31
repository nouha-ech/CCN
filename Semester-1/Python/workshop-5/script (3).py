import numpy as np
import numpy.random as rd
def T(n):
    S = 0        
    T = 0        
    
    while S < n:
        tirage = rd.randint(1, n+1) 
        S = S + tirage              
        T = T + 1 
        print(f"Tirage {T}: {tirage}, Somme actuelle: {S}")
    return T

#pour n=14
resultat = T(14)
print(resultat)

resultat = T(40)
print(resultat)

