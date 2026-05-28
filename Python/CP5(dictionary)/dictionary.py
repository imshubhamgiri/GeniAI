marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
}

# Accessing values
# print(marks["Alice"])  # Output: 85
# print(marks["Bob"])    # Output: 92
# print(marks["Charlie"])  # Output: 78

# Adding a new key-value pair

marks["David"] = 88
# print(marks)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 88}

# Updating an existing value
marks["Charlie"] = 80
# print(marks)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 80, 'David': 88}

# print(marks.items())  # Output: dict_items([('Alice', 85), ('Bob', 92), ('Charlie', 80), ('David', 88)])

length = marks.keys()
print(length , "ye hai length")


#method 1
for key in marks.keys():
    print(key, ":", marks[key])

#method 2
for key, value in marks.items():
    print(key, ":", value)

