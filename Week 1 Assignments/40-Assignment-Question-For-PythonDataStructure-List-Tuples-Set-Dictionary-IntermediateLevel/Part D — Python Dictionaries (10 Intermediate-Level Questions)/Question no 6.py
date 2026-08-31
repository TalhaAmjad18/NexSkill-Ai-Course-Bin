# 6. Given a nested dictionary, safely access a deeply nested key.

nestedDict = {
    101: {
        "name": "mahrukh",
        "age": 20,
        "city": "lahore"
    },
    102: {
        "name": "faakhir",
        "age": 22,
        "city": "chakwal"
    },
}

print(f"Nested dictionary: {nestedDict}")

print(f"Safely access a deeply nested key 'name': {nestedDict[101]['name']}")

print(f"Safely access a deeply nested key 'name' using get(): {nestedDict.get(101).get('name')}")