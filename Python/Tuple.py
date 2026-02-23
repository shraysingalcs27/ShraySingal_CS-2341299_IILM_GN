# 1. Store multiple items in a single variable using tuple
items = ("Java", "Python", "SQL", "C")
print(items)

# 2. Store only one item using tuple
single_item = ("Python",)
print(single_item)

# 3. Reverse a tuple
t = (1, 2, 3, 4, 5)
reversed_tuple = t[::-1]
print(reversed_tuple)

# 4. Swap two tuples
t1 = (1, 2)
t2 = (3, 4)
t1 = t2
t2 = t1
print(t1, t2)

# 5. Check if all items in the tuple are the same
t = (5, 5, 5, 5)
result = all(item == t[0] for item in t)
print(result)

# 6. Divide the tuple into four variables
t1 = (100, 200, 300, 400)
a, b, c, d = t1
print(a, b, c, d)

# 7. Copy elements 4 and 5 into a new tuple
tuple1 = (1, 2, 3, 4, 5, 6)
new_tuple = tuple1[3:5]
print(new_tuple)

# 8. Sort a tuple of tuples by the second item
tuple1 = (('a', 21), ('b', 37), ('c', 11), ('d', 29))
sorted_tuple = tuple(sorted(tuple1, key=lambda x: x[1]))
print(sorted_tuple)

# 9. Print the value 20 from a nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])

# 10. Change first item (22) of a list inside a tuple to 222
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)
