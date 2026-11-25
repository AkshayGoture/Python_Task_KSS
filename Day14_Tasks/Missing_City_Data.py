#Missing City Data (NaN Handling) 
#A dataset contains city populations: cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000} 
#Scenario: You want data for: ["Delhi", "Chennai", "Bangalore"] 
#Task: ● Create a Series with the above index ● Identify which cities have missing values (NaN)

import pandas as pd

# Create dictionary
cities = {
    "Delhi": 2000000,
    "Mumbai": 3000000,
    "Chennai": 1500000
}

# Create Series with required city index
S = pd.Series(cities, index=["Delhi", "Chennai", "Bangalore"])

# Display Series
print("City Population:")
print(S)

# Identify missing values
print("\nMissing Values:")
print(S[S.isna()])

# Identify city names with missing values
print("\nCities with Missing Population:")
print(S.index[S.isna()].tolist())
