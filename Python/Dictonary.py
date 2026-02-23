# 1. Create and print a dictionary which stores your information
my_info = {
    "name": "Shray Singal",
    "age": 21,
    "gender": "Male",
    "city": "Hisar"
}
print("1. My Information Dictionary:", my_info)

# 2. Access the items of a dictionary by referring to its key name
print("\n2. Access Name:", my_info["name"])
print("   Access Age:", my_info["age"])

# 3. Get a list of the values from a dictionary
values_list = list(my_info.values())
print("\n3. List of Values:", values_list)

# 4. Change the value of a specific item by referring to its key name
my_info["age"] = 20
print("\n4. Updated Age:", my_info)

# 5. Print all key names in the dictionary, one by one
print("\n5. Keys in Dictionary:")
for key in my_info.keys():
    print(key)

# 6. Create a dictionary that contains three dictionaries (nested)
nested_dict = {
    "dict1": {"a": 1, "b": 2},
    "dict2": {"x": 10, "y": 20},
    "dict3": {"name": "Shray", "age": 21}
}
print("\n6. Nested Dictionary:", nested_dict)

# 7. Create three dictionaries, then create one dictionary that will contain the other three
dict_a = {"A": 1}
dict_b = {"B": 2}
dict_c = {"C": 3}
combined_dict = {"first": dict_a, "second": dict_b, "third": dict_c}
print("\n7. Combined Dictionary:", combined_dict)

# 8. Convert two lists into a dictionary
list1 = ["name", "age", "city"]
list2 = ["Shray", 21, "Hisar"]
dict_from_lists = dict(zip(list1, list2))
print("\n8. Dictionary from Lists:", dict_from_lists)

# 9. Merge two dictionaries into one
dict1 = {"x": 1, "y": 2}
dict2 = {"y": 3, "z": 4}  # 'y' will be overwritten
merged_dict = {**dict1, **dict2}
print("\n9. Merged Dictionary:", merged_dict)

# 10. Get the key of lowest value from a dictionary
sample_dict = {'C': 92, 'Java': 66, 'Python': 85}
key_lowest_value = min(sample_dict, key=sample_dict.get)
print("\n10. Key with Lowest Value:", key_lowest_value)
