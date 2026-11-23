#An IoT device records a single sensor reading = 75. 
#Task: ● Create a 0-D NumPy array with this value. ● Print the value and check its number of dimensions.import numpy as np

# Single sensor reading
sensor_value = 75

# Create a 0-D NumPy array
arr = np.array(sensor_value)

# Print the value
print("Sensor Value:", arr)

# Check the number of dimensions
print("Number of Dimensions:", arr.ndim)
