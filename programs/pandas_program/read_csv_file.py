import pandas as pd
import numpy as np

data = pd.read_csv(r'D:\python_programmes\python_programs\programs\pandas_program\titanic.csv')

# .head() Display the first 5 rows
print(f"uisng head() method: \n{data.head()}") 

# Show last 5 rows of the DataFrame
print(f"using tail() method: \n{data.tail()}")

#-- .info() way to display this information, including the number of rows, column names, data types
print(f"using info methods: \n{data.info()}") 

#--- group by
survived_list = data.groupby('Age')['Survived'].mean() 
print(survived_list)

Pclass_list = data.groupby('Pclass')['Age'].mean()
print(Pclass_list)

gender_survival = data.groupby('Sex')['Survived'].mean()
print("Gender-wise Survival Rate:\n", gender_survival)

#-- sort 
sort_list = data.sort_values(by='Survived', ascending=True)
print(f"after sorting: \n{sort_list}")

# Sort passengers by fare in descending order
sorted_by_fare = data.sort_values(by='Fare', ascending=False)
print("Top 5 Passengers by Fare:\n", sorted_by_fare.head())

# Passenger count by age group , ['Age'] => refers to column 
# -- .value_counts() counts the number of people of that age. 
#    for example, [Age=22.00 , Count=39]
age_group_counts = data['Age'].value_counts()
print("Passenger Count by Age Group:\n", age_group_counts)

# Access a specific row using .iloc, e.g., the first row
first_row = data.iloc[0]
print(f"first row: \n{first_row}")

# unique name count
unique_name_count = data['Name'].unique()
print(f"unique name count: \n {unique_name_count}")