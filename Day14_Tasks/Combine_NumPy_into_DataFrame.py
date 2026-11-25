#Combine NumPy Arrays into DataFrame 
#Two arrays: names = np.array(["A", "B", "C"]) marks = np.array([80, 90, 70]) 
#Task: ● Create a DataFrame with columns "Name" and "Marks" ● Filter students with marks above 75

import numpy as np
import pandas as pd

# Create NumPy arrays
names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

# Filter students with marks above 75
filtered = df[df["Marks"] > 75]

# Display complete DataFrame
print("Student Data:")
print(df)

# Display filtered students
print("\nStudents with marks above 75:")
print(filtered)
