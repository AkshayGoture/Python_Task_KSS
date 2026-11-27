# Pie Chart with Conditional Data 
#Scenario: scores = np.array([40, 60, 80, 30, 90]) 
#Task: ● Categorize into: ○ Pass (>50) ○ Fail (<=50) 
#● Count using NumPy/Pandas ● Plot pie chart for Pass vs Fail


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

# count
passed = np.sum(scores > 50)
failed = np.sum(scores <= 50)

print("Pass:", passed)
print("Fail:", failed)

# Pie Chart
plt.pie([passed, failed],
        labels=["Pass", "Fail"],
        autopct='%1.1f%%',
        colors=['green', 'red'])

plt.title("Pass vs Fail")
plt.show()
