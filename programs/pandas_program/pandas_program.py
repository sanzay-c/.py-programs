import pandas as pd
import numpy as np

# Create a DataFrame from a dictionary
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, None, 32],
    'City': ['New York', 'London', 'Berlin', 'Tokyo']
}

df = pd.DataFrame(data)
print(df)

#--- df['Age'].mean(): This calculates the mean of the 'Age' column.
#    fillna(): This replaces missing values (NaN) in 'Age' with the mean value.
#    inplace=True: This modifies the original DataFrame directly without creating a new one. ------
# --- df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Age'] = df['Age'].fillna(df['Age'].mean())
print("\nAfter filling missing values:")
print(df)


# Remove duplicates (if any) 
df.drop_duplicates()
print("\nAfter removing duplicates")
print(df)

# filter the data if the 'Age' > 30 and the 'City' == 'Berlin'
filter_df = df[(df['Age'] > 30) & (df['City'] == 'Berlin')]
print(f"After filter: \n{filter_df}")

