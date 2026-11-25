#Decorator-based Access Control 
#Scenario: Restrict access to certain functions. 
#Task: ● Create a decorator to check user role ● Use condition inside decorator ● Apply decorator to multiple functions ● Store roles in a dictionary

# Store user roles in dictionary
users = {
    "Alice": "admin",
    "Bob": "user",
    "Charlie": "manager"
}

# Current user
current_user = "Alice"

# Decorator for role checking
def check_role(required_role):
    def decorator(func):
        def wrapper():
            role = users.get(current_user)

            if role == required_role:
                print("Access Granted!")
                func()
            else:
                print("Access Denied!")

        return wrapper
    return decorator

# Apply decorator to functions
@check_role("admin")
def delete_data():
    print("Data deleted successfully.")

@check_role("manager")
def view_report():
    print("Report displayed successfully.")

# Call functions
delete_data()
view_report()
