import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, Lasso, Ridge
<< << << < HEAD

boston = load_boston()

x = boston.data
y = boston.target

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

model = LinearRegression()
model.fit(x_train, y_train)

model1 = Lasso()
model1.fit(x_train, y_train)

model2 = Ridge()
model2.fit(x_train, y_train)

pred = model.predict(x_test)
pred1 = model1.predict(x_test)
pred2 = model2.predict(x_test)

print("LinearRegression: ", r2_score(y_test, pred))
print("Lasso: ", r2_score(y_test, pred1))
print("Ridge: ", r2_score(y_test, pred2))

plt.plot(model.predict(x_test), linestyle="solid",
         color="red", label="lr")
plt.plot(model1.predict(x_test), linestyle="solid",
         color="green", label="lasso")
plt.plot(model2.predict(x_test), linestyle="solid",
         color="blue", label='ridge')
plt.title("LinearRegression, Lasso, Ridge")
plt.legend()
plt.show()
