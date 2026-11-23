#Splitting Student Scores Across Servers 
#A dataset: [50, 60, 70, 80, 90, 100, 110, 120] 
#Scenario: A distributed system needs to divide this data among 4 servers. 
#Task: ● Convert to NumPy array. ● Split the array into 4 equal parts using array_split().

import numpy as np
scores = [50, 60, 70, 80, 90, 100, 110, 120]

# Convert list into NumPy array
arr = np.array(scores)

# Split array into 4 equal parts
servers = np.array_split(arr, 4)

# Display the results
for i, server in enumerate(servers):
    print("Server", i + 1, ":", server)
