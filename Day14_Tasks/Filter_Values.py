#A dataset: arr = np.array([10, 25, 30, 15, 40]) 
#Task: ● Convert to Pandas Series ● Filter values greater than 20

import numpy as np
import pandas as pd

# Create NumPy array
arr = np.array([10, 25, 30, 15, 40])

# Convert NumPy array into Pandas Series
S = pd.Series(arr)

# Filter values greater than 20
filtered = S[S > 20]

# Display filtered values
print(filtered)
