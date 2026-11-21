 #Two sensors record readings during a test. Scenario: Sensor1 = [10, 20, 30] Sensor2 = [40, 50, 60] 
#Task: ● Store both readings in NumPy arrays. ● Combine them into one array using NumPy concatenation.

import numpy as np
# Readings from two sensors
Sensor1 = [10, 20, 30]
Sensor2 = [40, 50, 60]

# Convert readings into NumPy arrays
array1 = np.array(Sensor1)
array2 = np.array(Sensor2)

# Combine both arrays using concatenation
combined_array = np.concatenate((array1, array2))

# Print the combined array
print("Combined Sensor Readings:", combined_array)
