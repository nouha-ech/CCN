def approx_e(epsi):
    n = 0
    u_n = 1.0
    factorielle = 1
    while True:
        err_approx = 3.0 / factorielle
        if err_approx < epsi:
            return u_n
        n += 1
        factorielle *= n
        u_n += 1.0 / factorielle
s = approx_e(54)
print(s)