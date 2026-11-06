#Write a program to check whether a key exists in a dictionary.
my_dict = {
    "name": "Akshay",
    "age": 24,
    "city": "Karnataka"
}
key = "age"

if key in my_dict:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")
