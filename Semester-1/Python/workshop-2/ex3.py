def grands(L, x):
     return len(list(filter(lambda i: i > x, L)))

L = [1, 4, 3, 9]
s = grands(L, 2)
print(s)


# c) Fonction petits
def petits(L, x):
    return len(list(filter(lambda i: i < x, L)))
ss = petits(L, 2)
print(s)


def median(L):
    n = len(L)
    for i in range(n):
        x = L[i]
        if grands(L, x) <= n // 2 and petits(L, x) <= n // 2:
            return x
m = median(L)
print(m)

