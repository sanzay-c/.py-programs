import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error 


df = pd.read_csv('insurance.csv')

# select the specific column to normalize for (X)
X = df[['age', 'bmi', 'children']]

# target variable meaning which is used for the predection
y = df['charges']

# scale the data (normalize the data)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# split the data into train and test, 80% i.e 0.8 is for training and 20% i.e 0.2 for testing
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# set up the model
model = LinearRegression()
model.fit(X_train, y_train)

# predict the model
y_predict = model.predict(X_test)

# print the predections and the actual value for the comparison
print(f'The Predicted Values are: {y_predict[:5]}')
print(f'The Actual Values are: {y_test.values[:5]}')

# calculate the error part of the model
# mse is mean squared error
mse = mean_squared_error(y_test, y_predict)
print(f"Mean Squared Error is: {mse}")

# root mean squared error (rmse)
rmse = mse ** 2
print(f"Root Mean Squared Error is: {rmse}")