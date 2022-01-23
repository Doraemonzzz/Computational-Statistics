# https://stackoverflow.com/questions/19141432/python-numpy-machine-epsilon

import numpy as np

def lhs(z, x1, x2):
    return z ** 2 - x1 * z + x2

def z11(x1, x2):
    return (x1 + np.sqrt(x1 ** 2 - 4 * x2)) / 2

def z21(x1, x2):
    return (x1 - np.sqrt(x1 ** 2 - 4 * x2)) / 2

def z22(x1, x2):
    return 2 * x2 / (x1 + np.sqrt(x1 ** 2 - 4 * x2))

# 条件数
def kapa(x1, x2):
    return z11(x1, x2) / (z11(x1, x2) - z22(x1, x2))

EPS = np.finfo(float).eps

x1 = 1
x2 = 0.5 * EPS
# 方法1
print(z21(x1, x2))
# 方法2
print(z22(x1, x2))
# 差值
print(z21(x1, x2) - z22(x1, x2))

# 扰动
dx2 = 0.1 * EPS
# 方法1
print(z21(x1, x2 + dx2))
# 方法2
print(z22(x1, x2 + dx2))
# 差值
print(z21(x1, x2 + dx2) - z22(x1, x2 + dx2))

# 条件数
print(kapa(x1, x2))
# 实际变化率
# 方法1
print((z21(x1, x2 + dx2) - z21(x1,x2)) /z21(x1, x2))
# 方法2
print((z22(x1, x2 + dx2) - z22(x1,x2)) /z22(x1, x2))
# 理论值
print(kapa(x1, x2) * dx2 / x2)