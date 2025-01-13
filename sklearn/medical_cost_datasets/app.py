import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# The App title
st.title("Medical Cost Dataset Visuaization")

uploaded_file = st.file_uploader('Upload Your CSV File', type=['csv'])

if uploaded_file is not None:

    # read data
    df = pd.read_csv(uploaded_file)

    # Display First Five Rows Of The Dataset
    st.subheader('Display First Five Rows Of The Dataset')
    st.write(df.head())

    # To check if the data has any null values or not 
    st.subheader('Check Null')
    st.write(f'The total sum of null values is: {df.isnull().sum().sum()}')

    # select columns for analysis
    df = df[['age', 'bmi', 'children', 'charges']]

    # Dataset summary
    st.subheader('Dataset Summary')
    st.write(df.describe())

    # correlation matrix of the selected data (columns)
    st.subheader('Correlation Matrix')
    correlation_matrix = df.corr()
    st.write(correlation_matrix)

    st.subheader('Correlation Matrix Visualization')
    plt.figure(figsize=(10,6))
    sns.heatmap(data=correlation_matrix, annot=True)
    st.pyplot(plt)

    # This is for sklearn
    st.header('Sklearn')
    # select the specific column to normalize for (X)
    X = df[['age', 'bmi', 'children']]
    st.write(f"The Defined Data For X is:")
    st.write(X)

    # target variable meaning which is used for the predection
    y = df['charges']
    st.write(f"The Defined Data For y is:")
    st.write(y)

    # for min max scaler to normalize the data
    st.subheader('Scaling The Data Using MinMaxScaler')
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    st.write(f"Data of X after scaled:")
    st.write(X_scaled)

    # split the data for train test model
    X_train, X_test, y_trian, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # setup the model Linear Regression
    model = LinearRegression()
    model.fit(X_train, y_trian) # fit only takes train data

    # make the predections
    st.subheader('Make the predection')
    y_pred = model.predict(X_test)
    st.write(f'The Predicted Values are:')
    st.write(y_pred[:5])
    st.write(f'The Actual Values are:')
    st.write(y_test.values[:5])

    # for calculating the errors
    st.subheader('Calculating The Mean Squared Error')
    mse = mean_squared_error(y_test, y_pred)
    st.write(f"The Result For Mean Squared Error is: {mse}")

    st.subheader('Calculating The Root Mean Squared Error')
    rmse = mse ** 2
    st.write(f"The Result For Root Mean Squared Error is: {rmse}")

    st.subheader("Scatter plot To Visulaize the Actal and Predicted price")
    plt.figure(figsize=(10,6))
    plt.scatter(y_test, y_pred, alpha=0.6, color="green", edgecolor='black')
    plt.title('Actual vs Predicted Charges')
    plt.xlabel('Actual Charges')
    plt.ylabel('Predicted Charges')
    plt.grid(True)
    st.pyplot(plt)


else:
    st.write("Please Upload CSV File To Proceed.")