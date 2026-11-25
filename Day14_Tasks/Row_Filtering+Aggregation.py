#Row Filtering + Aggregation 
#A dataset: arr = np.array([ [100, 200], [150, 250], [80, 120], [300, 400] ]) 
#Task: ● Convert to DataFrame with columns "Sales", "Profit" ● Filter rows where Sales > 100 ● Find average Profit of filtered rows

import numpy as np
import pandas as pd

# Create NumPy array
arr = np.array([
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
])

# Convert NumPy array into DataFrame
df = pd.DataFrame(arr, columns=["Sales", "Profit"])

# Filter rows where Sales > 100
filtered = df[df["Sales"] > 100]

# Find average Profit of filtered rows
avg_profit = filtered["Profit"].mean()

# Display results
print("Filtered Data:")
print(filtered)

print("\nAverage Profit:", avg_profit)
