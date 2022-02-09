import numpy as np

def var_iter(arr):
    n = len(arr)
    xm = arr[0]
    ss = 0
    for k in range(2, n + 1):
        ss = (k - 2) / (k - 1) * ss + (arr[k - 1] - xm) ** 2 / k
        xm = (k - 1) / k * xm + arr[k - 1] / k

    return ss

arr = np.random.rand(10)
print(var_iter(arr))
print(np.var(arr, ddof=1))