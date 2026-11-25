#Student Marks Analysis (NumPy → Pandas) 
#Marks data: arr = np.array([ [80, 90], [70, 60], [85, 95] ]) 
#Task: ● Convert into DataFrame with columns "Math", "Science" ● Add a new column Total ● Find student with highest total 

import numpy as np
import pandas as pd

arr = np.array([
    [80, 90],
    [70, 60],
    [85, 95]
])

# Convert NumPy array into DataFrame
df = pd.DataFrame(arr, columns=["Math", "Science"])

# Add Total column
df["Total"] = df["Math"] + df["Science"]

# Find student with highest total
highest = df["Total"].idxmax()

# Display DataFrame
print("Student Marks:")
print(df)

# Display student with highest total
print("\nStudent with highest total:")
print("Student", highest + 1)
print("Total Marks:", df.loc[highest, "Total"])
