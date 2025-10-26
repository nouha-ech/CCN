def somme(n):
    s= 0
    k = 1
    while k <= n:
        s = s + 1/k
        k = k + 1
    return s
#test avec 9
res = somme(9)
# print(res)

# partie 2
#trouvons pls petit entier dont la somme
sum = 0
n = 0
while sum <= 8:
        n = n + 1
        sum = sum + 1/n
print(n)
# testons avec somme
test = somme(1673)
test2 = somme(1674)
print(test)
print(test2)