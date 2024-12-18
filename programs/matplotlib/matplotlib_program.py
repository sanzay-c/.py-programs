import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, None, 32],
    'City': ['New York', 'London', 'Berlin', 'Tokyo']
}

df = pd.DataFrame(data)
print(df)

#-- line plot
plt.figure(figsize=(8,6))
plt.plot(df['Age'], df['Name'], color='lightblue')
plt.title('Line Plot')
plt.xlabel('Age')
plt.ylabel('Name')
plt.grid(True)
plt.show()

#-- bar plot
plt.figure(figsize=(8, 5))
plt.bar(df['Age'], df['Name'], color='b')
plt.title("names")
plt.xlabel('Age')
plt.ylabel('Name')
plt.grid(True)
plt.show()

#-- scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['Name'], color='b')
plt.title("names")
plt.xlabel('Age')
plt.ylabel('Name')
plt.grid(True)
plt.show()

#-- pi-chart plot
# Count occurrences of each unique name
name_counts = df['Name'].value_counts()
# Create the pie chart
plt.figure(figsize=(8, 5))
plt.pie(name_counts, labels=name_counts.index, autopct='%1.1f%%', colors=['b', 'g', 'r', 'c', 'm', 'y', 'k'])
# Set the title
plt.title("Name Distribution")
# Show the plot
plt.show()