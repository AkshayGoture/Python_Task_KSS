  
#A dataset: arr = np.array([12, 45, 22, 67, 34]) 
#Task: ● Convert to Pandas Series ● Find the maximum value

import numpy as np
import pandas as pd

# Create NumPy array
arr = np.array([12, 45, 22, 67, 34])

# Convert NumPy array into Pandas Series
S = pd.Series(arr)

# Find maximum value
maximum = S.max()

# Print maximum value
print("Maximum value:", maximum)
