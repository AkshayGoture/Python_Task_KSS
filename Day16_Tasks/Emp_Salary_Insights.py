#Employee Salary Insights 
#Scenario: salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 
#Task: ● Convert into DataFrame ● Plot: 
#○ Line graph → salary trend ○ Bar chart → department-wise salary comparison ○ Pie chart → department distribution ○ Histogram
#→ salary distribution ○ Scatter plot → index vs salary

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# DataFrame
df = pd.DataFrame({
    "Department": departments,
    "Salary": salaries
})
print(df)

# Graphs
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(salaries, marker='o')
plt.title("Salary Trend")

plt.subplot(2, 3, 2)
df.groupby("Department")["Salary"].mean().plot(
    kind='bar', color='orange')
plt.title("Department-wise Salary")

plt.subplot(2, 3, 3)
df["Department"].value_counts().plot(
    kind='pie', autopct='%1.1f%%')
plt.title("Department Distribution")

plt.subplot(2, 3, 4)
plt.hist(salaries, bins=5, color='green',
         edgecolor='black')
plt.title("Salary Distribution")

plt.subplot(2, 3, 5)
plt.scatter(range(len(salaries)), salaries, color='red')
plt.title("Index vs Salary")
plt.xlabel("Index")
plt.ylabel("Salary")

plt.tight_layout()
plt.show()

# Analysis
print("Average Salary:", np.mean(salaries))
print("Maximum Salary:", np.max(salaries))
print("Minimum Salary:", np.min(salaries))
print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())
