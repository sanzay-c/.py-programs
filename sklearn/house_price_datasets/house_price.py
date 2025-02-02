import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error 

df = pd.read_csv('train.csv')

# define X 
X = df[['GrLivArea', 'OverallQual', 'GarageCars', 'YearBuilt']]

# define y 
y = df['SalePrice']

# scale the data normaliza the data 
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# split the data into training => 80% i.e 0.8 and testing => 20% i.e 0.2
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# set up the model
model = LinearRegression()
model.fit(X_train, y_train)

# predict the model
y_predict = model.predict(X_test)

# print the predicted part
print(f'Predection Value: {y_predict[:5]}')
print(f'Actual Value: {y_test.values[:5]}')

# calculate the error of test and the predict
# mean squared error
mse = mean_squared_error(y_test, y_predict)
print(f"Mean Squared Error is: {mse}")

# root mean squared error
rmse = mse ** 2
print(f"Root mean Squared Error: {rmse}")
