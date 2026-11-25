#Complex DataFrame Transformation 
#A DataFrame: 
#df = pd.DataFrame({ "Name": ["A", "B", "C", "D"], "Marks": [50, 80, 30, 90] }) 
#Scenario: ● Students scoring below 50 failed 
#Task: 1. Create a column Status ("Pass"/"Fail") 2. Filter only passed students 3. Calculate average marks of passed students

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

# Create Status column
df["Status"] = df["Marks"].apply(
    lambda x: "Fail" if x < 50 else "Pass"
)

# Filter only passed students
passed = df[df["Status"] == "Pass"]

# Calculate average marks of passed students
avg_marks = passed["Marks"].mean()

# Display complete DataFrame
print("Student Results:")
print(df)

# Display passed students
print("\nPassed Students:")
print(passed)

# Display average marks
print("\nAverage Marks of Passed Students:", avg_marks)
