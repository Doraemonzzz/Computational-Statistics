def naive_poly(a, x):
    p = 1
    u = 0
    n = len(a)
    for i in range(n):
        u += p * a[i]
        p *= x
    
    return u

def fast_poly(a, x):
    n = len(a) - 1
    u = a[-1]
    for i in range(n - 1, -1, -1):
        u = u * x + a[i]

    return u

a = [1, 8, 9, 11]
x = 13
print(naive_poly(a, x))
print(fast_poly(a, x))