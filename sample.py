import numpy as np
import matplotlib.pyplot as plt

x = np.array([-1.2, -0.6, 0.0, 0.6, 1.2, 1.8, 2.4, 3.0, 3.6, 4.2])
y = np.cos(x)

# 3次元（y=a0+a1x1+a2x^2+a3x^3)まで考えた回帰分析
z = np.polyfit(x, y, 3)
print(z)
p = np.poly1d(z)
print(p)
