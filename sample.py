from sklearn.linear_model import Ridge
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

boston = load_boston()

x = boston.data
y = boston.target

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=123)

model = Ridge()
model.fit(x_train, y_train)

pred = model.predict(x_test)
print(r2_score(y_test, pred))
