#Generator-based Log Reader 
#Scenario: A large log file needs to be processed. 
#Task: ● Create a generator to read file line by line ● Use loop to process logs ● Use condition to filter errors ● Count occurrences using a dictionary 

# Generator to read file line by line
def read_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

# Dictionary to count errors
error_count = {}

try:
    # Process logs
    for log in read_logs("log.txt"):

        if "ERROR" in log:
            error_count[log] = error_count.get(log, 0) + 1

    # Display error counts
    print("Error Report:")
    for error, count in error_count.items():
        print(error, ":", count)

except FileNotFoundError:
    print("Log file not found!")
