numbers = [10, 10, 10, 20, 20, 30, 30, 30, 40, 40, 50, 50, 50]
x = set()
i = 0
while i < len(numbers):
    if numbers[i] not in x:
        x.add(numbers[i])
    i += 1
print (numbers)
print("Final set values:", x)
