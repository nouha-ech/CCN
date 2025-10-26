def Empiler_Fact(n, P1):
    for i in range(n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        P1.append(fact)
    return P1
num=5
p=[]
fac = Empiler_Fact(num, p)
print(fac)



def Empiler_Puiss(n, x, P2):
    for i in range(n + 1):
        puiss = x ** i
        P2.append(puiss)
    return P2

puis=5
x=3
p2=[]
puissance= Empiler_Puiss(puis,x,p2)
print(puissance)




def Empiler_Frac(P1, P2):
    P3 = list(map(lambda puiss, fact: puiss / fact, P2, P1))
    return P3
frac = Empiler_Frac(p,p2)
print(frac)






def Somme(n, x):
    P1 = []  
    P2 = []  
    P1 = Empiler_Fact(n, P1)
    P2 = Empiler_Puiss(n, x, P2)
    P3 = Empiler_Frac(P1, P2)
    S = sum(P3)
    return S
S= Somme(5,3)
print(S)


    
    
    
    
    
    
    