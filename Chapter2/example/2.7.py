import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

arr = np.arange(-1, -21, -1)
hvec = 10.0 ** arr
yp = (np.exp(hvec) - 1) / hvec - 1.0
plt.scatter(arr, yp)
plt.xlabel("h")
plt.ylabel("误差")
plt.title("数值方法估计的导数的误差")
plt.show()