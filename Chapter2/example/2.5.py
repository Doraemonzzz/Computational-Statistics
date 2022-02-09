import numpy as np

x = 8
y1 = 1 - 1 / (1 + np.exp(-x))
y2 = 1 / (1 + np.exp(x))

print(y1)
print(y2)
