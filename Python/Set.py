# 1. Store all programming languages known using a Set
languages = {"Python", "Java", "C++", "JavaScript", "SQL"}
print("Programming Languages Set:", languages)

# 2. Store your own information
my_info = {"name": "Shray Singal", "age": 22, "gender": "Male", "city": "Hisar"}
print("My Information:", my_info)

# 3. Get the data type of a Set
print("Data type of languages set:", type(languages))

# 4. Check if "Python" is present in the set
set = {"Java", "Python", "Django"}
print("Is Python present?", "Python" in set)

# 5. Add items from another set to the current set
this = {"Java", "Python", "SQL"}
secondset = {"C", "Cpp", "NoSQL"}
this.update(secondset)
print("Updated Set after adding another set:", this)

# 6. Add elements of a list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset.update(mylist)
print("Set after adding list elements:", thisset)

# 7. Remove last item of the given set
# Note: Sets are unordered, so "last item" is ambiguous; we can use pop()
thisset = {"Python", "Django", "JavaScript", "SQL"}
removed_item = thisset.pop()  # removes an arbitrary item
print("Removed item:", removed_item)
print("Set after removing an item:", thisset)

# 8. Delete the set completely
del thisset
print("Set deleted.")
# print(thisset)  # This would raise an error because the set is deleted

# 9. Loop through a set and print values
thisset = {"Python", "Django", "JavaScript", "SQL"}
print("Looping through set values:")
for item in thisset:
    print(item)

# 10. Find the maximum and minimum value in a set
num_set = {10, 20, 5, 35, 2}
print("Maximum value:", max(num_set))
print("Minimum value:", min(num_set))
