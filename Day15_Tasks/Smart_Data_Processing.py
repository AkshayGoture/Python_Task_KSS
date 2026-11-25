#Smart Data Processing Pipeline 
#Scenario: A system processes numeric data from file. 
#Task: ● Read numbers from a file ● Use NumPy for calculations (mean, std) ● Convert results to Pandas DataFrame ● Use exception handling for bad data ● Use a generator to stream data ● Apply decorator to measure execution time 

import numpy as np
import pandas as pd
import time

# Decorator to measure execution time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        print("Execution Time:", time.time() - start)
    return wrapper

# Generator to read numbers
def read_data():
    with open("numbers.txt", "r") as file:
        for line in file:
            try:
                yield float(line.strip())
            except ValueError:
                print("Invalid data:", line.strip())

# Main processing function
@timer
def process():

    try:
        # Read data
        data = list(read_data())

        if not data:
            print("No valid data found.")
            return

        # NumPy calculations
        arr = np.array(data)

        mean = np.mean(arr)
        std = np.std(arr)

        # Create DataFrame
        df = pd.DataFrame({"Numbers": arr})

        print("Data:")
        print(df)

        print("\nMean:", mean)
        print("Standard Deviation:", std)

        # Save report
        df.to_csv("report.csv", index=False)
        print("Report saved successfully!")

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("Error:", e)

# Run program
process()
