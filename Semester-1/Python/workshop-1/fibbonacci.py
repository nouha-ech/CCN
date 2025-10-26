def fibo(n):
    if n == 0 or n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def v(n):
    un_moins1 = fibo(n - 1)
    un = fibo(n)
    un_plus1 = fibo(n + 1)
    return un_plus1 * un_moins1 - un ** 2

imp = v(3)
print(imp)
p = v(4)
print(p)
imp = v(5)
print(imp)
p = v(6)
print(p)