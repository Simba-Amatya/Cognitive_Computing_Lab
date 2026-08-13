my_dict = {
    "name": "Amatya Simba",
    "roll_no": "1024170346",
    "branch": "CSE",
    "age": 20,
    "city": "Patiala"
}

print("Original dictionary:")
print(my_dict)

my_dict["location"] = my_dict.pop("city")

print("\nAfter renaming city to location:")
print(my_dict)

my_dict["cgpa"] = 7.97

print("\nAfter adding CGPA:")
print(my_dict)

my_dict["age"] = my_dict["age"] + 1
print("\nAfter increasing age by 1:")
print(my_dict)

dict_pop = my_dict.copy()

removed_branch = dict_pop.pop("branch")

print("\nUsing pop() to delete branch:")
print(dict_pop)

print("Value returned by pop():", removed_branch)

dict_del = my_dict.copy()

del dict_del["branch"]

print("\nUsing del to delete branch:")
print(dict_del)

print("\nKey-value pairs:")

for key, value in my_dict.items():

    print(key, "-->", value)

print("\nChecking for email:")

if "email" in my_dict:

    print("Email:", my_dict["email"])

else:

    print("Email key does not exist in the dictionary.")

friend_dict = {
    "name": "ABCD",
    "roll_no": "1234567890",
    "branch": "ECE",
    "age": 20,
    "city": "Chandigarh"
}

print("\nFriend dictionary:")
print(friend_dict)

merged_dict = {**my_dict, **friend_dict}

print("\nMerged dictionary:")
print(merged_dict)

string_values = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("\nDictionary containing only string value:")
print(string_values)