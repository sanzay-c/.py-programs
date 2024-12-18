from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv(r"D:\python_programmes\python_programs\programs\pandas_program\titanic.csv")

df = pd.DataFrame(data)
print(df)
print(df.info()) # to see the list of the information

# -- titanic data to see the survival count
# -- bar-plot
#    here, figsize=(width, height)
survival_count = df['Survived'].value_counts()

plt.figure(figsize=(8,6))
plt.bar(['Did Not Survived', 'Survived'], survival_count, color=['red', 'green'])
plt.title('Titanic Survival Index')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.grid(True)
plt.show()


# -- titanic data to see passenger class distribution
# -- pie-chart plot
#    in pie plot labels=[''] help identify what each slice represents.
pclass_distribution = df['Pclass'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(pclass_distribution, labels=['3rd class', '1st class', '2nd class'], autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'gold'])
plt.title('Passenger class distribution')
plt.show()


# -- titaic data survival rate by age group
#    here, 'bar(x, height)' required ones like x-axis and y-axis
survival_rate_age_group = df.groupby('Age')['Survived'].mean()

plt.figure(figsize=(8, 6))
plt.bar(survival_rate_age_group.index, survival_rate_age_group, color='lightblue')
plt.title('Survival Rate Age Group')
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Survived Rate', fontsize=12)
plt.grid(True)
plt.show()


# -- subplots
# here, in the plt.subplots(1,2) => (1,2) means 1 row 2 columns, if (2,2) then 2 rows and 2 columns and so on..
# here, axes[0] is the 0 index and axex[1] is first index

# survival_rate_age_group = df.groupby('Age')['Survived'].mean()

fig, axes = plt.subplots(1,2, figsize=(14, 6))
# first subplot: for survial rate by age group 
axes[0].bar(survival_rate_age_group.index, survival_rate_age_group, color='lightblue')
axes[0].set_title('Survival rate age group')
axes[0].set_xlabel('Age group', fontsize=12)
axes[0].set_ylabel('Survival rate', fontsize=12)
axes[0].grid(True)

# second subplot: for Passenger class distribution
pclass_distribution = df['Pclass'].value_counts()

# Pie chart
axes[1].pie(pclass_distribution, labels=['3rd Class', '1st Class', '2nd Class'], autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'gold'])
axes[1].set_title('Passenger Class Distribution', fontsize=14)

# display the plot
plt.tight_layout() #-- Adjust the layout to prevent overlap
plt.show()

