#Data Alignment Issue in Series Addition 
#Two Series: S1 = pd.Series([10, 20, 30], index=["a", "b", "c"]) S2 = pd.Series([5, 15, 25], index=["b", "c", "d"]) 
#Task: ● Add both Series ● Explain why some values become NaN ● Replace NaN with 0 and compute final result

import pandas as pd

# Create two Series
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

# 1. Add both Series
result = S1 + S2

print("Result after addition:")
print(result)

# 2. Replace NaN values with 0
final_result = result.fillna(0)

# 3. Print final result
print("\nFinal Result:")
print(final_result)
