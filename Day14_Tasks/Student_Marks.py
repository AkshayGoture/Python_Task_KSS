 Student Marks DataFrame Analysis 
#A DataFrame: 
#data = pd.DataFrame({ "Name": ["A", "B", "C"], "Math": [80, 70, 60], "Science": [90, 60, 70] }) 
#Task: ● Add a new column Total = Math + Science ● Find the student with the highest total marks

import pandas as pd

# Create DataFrame
data = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [90, 60, 70]
})

# Add Total column
data["Total"] = data["Math"] + data["Science"]

# Find student with highest total marks
highest = data["Total"].idxmax()

# Display DataFrame
print("Student Marks:")
print(data)

# Display highest scorer
print("\nStudent with Highest Total Marks:")
print(data.loc[highest])
