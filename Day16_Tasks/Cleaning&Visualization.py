# Data Cleaning + Visualization 
#Scenario: data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
#Task: 1. Convert to Pandas Series 2. Replace NaN with mean 3. Plot: 
#○ Line graph of cleaned data ○ Bar chart of values > average

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

# Convert and clean data
s = pd.Series(data)
s = s.fillna(s.mean())
print(s)

# Line Graph
plt.plot(s, marker='o')
plt.title("Cleaned Data")
plt.show()

# Bar Chart (Above Average)
avg = s.mean()
filtered = s[s > avg]

plt.bar(filtered.index, filtered.values)
plt.title("Values Above Average")
plt.show()
