nmax = 9999
exact = 1 - 1 / (nmax + 1)
direct = 0
for n in range(1, nmax + 1):
    direct += 1 / (n * (n + 1))

print(direct)
print(direct - exact)
