#Data Analysis Tool (NumPy + Pandas) 
#Scenario: Analyze student marks. 
#Task: ● Generate marks using NumPy ● Convert into Pandas DataFrame ● Use conditions to filter passing students ● Calculate mean using math/NumPy ● Use loop to print results

import numpy as np
import pandas as pd

# Generate random marks
names = ["A", "B", "C", "D", "E"]
marks = np.random.randint(0, 101, size=5)

# Convert into DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

# Filter passing students
passed = df[df["Marks"] >= 40]

# Calculate mean
average = np.mean(marks)

# Display results using loop
print("Student Results:")
for i, row in df.iterrows():
    status = "Pass" if row["Marks"] >= 40 else "Fail"
    print(row["Name"], row["Marks"], status)

# Display passing students
print("\nPassing Students:")
print(passed)

# Display average marks
print("\nAverage Marks:", round(average, 2))
