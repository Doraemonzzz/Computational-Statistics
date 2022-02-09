import numpy as np

def mean_iter(arr):
    x_mean = arr[0]
    n = len(arr)
    for k in range(2, n + 1):
        x_mean = (k - 1) / k * x_mean + 1 / k * arr[k - 1]

    return x_mean

arr = np.random.rand(10)
print(mean_iter(arr))
print(np.mean(arr))