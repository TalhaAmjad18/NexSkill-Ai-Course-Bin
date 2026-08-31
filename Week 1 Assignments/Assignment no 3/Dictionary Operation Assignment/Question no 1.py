# Python Program to Check if a Key Exists in a Dictionary or Not[This is a Python Program to check 
# if a given key exists in a dictionary or not.]

d = {
    "name": "Talha",
    "age": 21,
    "city": "Lahore"
}

key = input("Enter key you want to find in dictionary: ")

if key in d.keys():

    print(f"{key} exists in dictionary")

else:

    print(f"{key} does not exist in dictionary")