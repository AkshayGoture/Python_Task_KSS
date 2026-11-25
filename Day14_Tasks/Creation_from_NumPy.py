#Basic DataFrame Creation from NumPy 
#You have: data = np.array([[1, 2], [3, 4], [5, 6]]) 
#Task: ● Convert it into a Pandas DataFrame ● Add column names: "X", "Y" 

import numpy as np
import pandas as pd

# Create NumPy array
data = np.array([[1, 2], [3, 4], [5, 6]])

# Convert NumPy array into Pandas DataFrame
df = pd.DataFrame(data, columns=["X", "Y"])

# Display the DataFrame
print(df)
