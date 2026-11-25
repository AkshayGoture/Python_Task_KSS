# Add Constant to Series (NumPy Operation on Pandas) 
#A Series: S = pd.Series([5, 10, 15]) 
#Task: ● Add 5 to each element using NumPy-style operation ● Print updated Series

import pandas as pd

# Create Pandas Series
S = pd.Series([5, 10, 15])

# Add 5 to each element
S = S + 5

# Print updated Series
print(S)
