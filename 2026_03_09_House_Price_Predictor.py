from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1000],[1500],[2000]])  # square feet
y = np.array([100000,150000,200000])  # price

model = LinearRegression()
model.fit(X,y)
print("Predicted price for 1200 sq ft:", model.predict([[1200]])[0])

