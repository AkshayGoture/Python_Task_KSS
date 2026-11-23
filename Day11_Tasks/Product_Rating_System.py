 
#An e-commerce website stores product ratings: [4, 5, 3, 4, 2] 
#Task: ● Convert it to a NumPy array. ● Print the first and last rating using indexing. 

import numpy as np 
# Product ratings
ratings = [4, 5, 3, 4, 2]

# Convert the list into a NumPy array
arr = np.array(ratings)

# Print the NumPy array
print("Product Ratings:", arr)

# Print the first rating
print("First Rating:", arr[0])

# Print the last rating
print("Last Rating:", arr[-1])
