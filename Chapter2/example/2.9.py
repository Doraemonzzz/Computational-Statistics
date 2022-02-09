import  numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

print(365 ** 120)
print(365 ** 121)

days = 365
nvec = np.arange(days)
pvec = 1 - np.cumproduct((days - nvec) / days)
plt.scatter(nvec + 1, pvec)
plt.xlabel("人数")
plt.ylabel("概率")
plt.title("n个人中存在生日同月日的概率")
plt.show()