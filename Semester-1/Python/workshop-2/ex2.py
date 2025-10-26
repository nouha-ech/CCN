# a/ generer liste
L= [a + b for a in "abc" for b in "de"]
print(L)

# b/ simplifions utilisant map() et product()
from itertools import product

L = list(map(lambda t: t[0] + t[1], product("abc", "de")))
print(L)
