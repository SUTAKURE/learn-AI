import numpy as np
import matplotlib.pyplot as plt

x = np.array([-1.2, -0.6, 0.0, 0.6, 1.2, 1.8, 2.4, 3.0, 3.6, 4.2])
y = np.cos(x)

# 3次元（y=a0+a1x1+a2x^2+a3x^3)まで考えた回帰分析
z = np.polyfit(x, y, 3)
print(z)
p = np.poly1d(z)
print(p)

# 30次元（y=a0+a1x1+a2x^2+...+a30x^30)まで考えた回帰分析
z30 = np.polyfit(x, y, 30)
p30 = np.poly1d(z30)

# ２から５で等間隔に100等分した値を配列に格納
xp = np.linspace(-2, 5, 100)

# プロットする
# テストデータは緑の線、　pは青の点、　p30は*で記す
plt.plot(xp, np.cos(xp), '.', xp, p(xp), '-', xp, p30(xp), '*')
plt.ylim(-3, 3)
plt.grid(True)  # grid線
plt.show()
plt.savefig('image.png')
