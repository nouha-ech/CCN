def suite(n):
    if n == 0:
        return 1
    uk = suite(n - 1)
    return uk / (uk + 1)
s = suite(8)
print(s)