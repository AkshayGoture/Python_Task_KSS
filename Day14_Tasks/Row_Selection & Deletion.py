#Row Selection & Deletion 
#A DataFrame: df = pd.DataFrame({ "A": [10, 20, 30], "B": [5, 15, 25] }, index=["x", "y", "z"]) 
#Task: ● Select row with index "y" ● Delete row "x" ● Print updated DataFrame

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [5, 15, 25]
}, index=["x", "y", "z"])

# 1. Select row with index "y"
print("Selected Row:")
print(df.loc["y"])

# 2. Delete row "x"
df = df.drop("x")

# 3. Print updated DataFrame
print("\nUpdated DataFrame:")
print(df)
