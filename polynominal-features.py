from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
x = np.linspace(-2, 2, 30)
y = 2 + 2 * x + 2 * x ** 2 - 2 * x ** 3 + \
    np.random.normal(scale=10, size=x.shape)
X = x.reshape(-1, 1)

_x = PolynomialFeatures(degree=3)

model1 = LinearRegression()
X = _x.fit_transform(X)
model1.fit(X, y)

pred = model1.predict(X)
plt.scatter(x, y, c="blue", alpha=0.3)
plt.plot(x, pred, c="blue")

print("切片: ", model1.intercept_)
print("傾き", model1.coef_)

plt.show()
