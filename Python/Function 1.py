# 1. Function that prints “TasiNCoder”
def print_name():
    print("TasiNCoder")
print_name()  # Output: TasiNCoder

# 2. Function that expects two arguments and prints them
def print_two(a, b):
    print(a, b)
print_two(10, 20)  # Output: 10 20

# 3. Function that expects an unknown number of arguments
def print_args(*args):
    print(*args)
print_args(1, 2, 3, 4)  # Output: 1 2 3 4

# 4. Function that expects keyword arguments (kwargs)
def print_kwargs(**kwargs):
    print(*[f"{k}:{v}" for k, v in kwargs.items()])
print_kwargs(name="Shray", age=21)  # Output: name:Shray age:21

# 5. Function that expects a list as an argument
def print_list(lst):
    print(*lst)
print_list([1, 2, 3, 4])  # Output: 1 2 3 4

# 6. Function to find maximum of four numbers
def max_of_four(a, b, c, d):
    print(max(a, b, c, d))
max_of_four(10, 25, 7, 15)  # Output: 25

# 7. Function to sum all numbers in a list
def sum_list(lst):
    print(sum(lst))
sum_list([1, 2, 3, 4, 5])  # Output: 15

# 8. Function to multiply all numbers in a list
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    print(result)
multiply_list([1, 2, 3, 4])  # Output: 24

# 9. Function to check whether a number falls in a given range
def check_range(num, start, end):
    print("Number is in range" if start <= num <= end else "Number is not in range")
check_range(10, 1, 20)  # Output: Number is in range

# 10. Function to check whether a number is even or odd
def even_odd(num):
    print("Even" if num % 2 == 0 else "Odd")
even_odd(7)  # Output: Odd