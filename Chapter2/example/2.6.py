import numpy as np

x = 100

y1 = np.sqrt(x ** 2 + 1) - np.abs(x)
y2 = 1 / (np.sqrt(x ** 2 + 1) + np.abs(x))

print(y1)
print(y2)