# 1. Function that returns unique elements of a list
def unique_list(l):
    result = list(set(l))
    print(result)
unique_list([1, 2, 2, 3, 4, 4, 5])

# 2. Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        print(False)
        return
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(False)
            return
    print(True)
is_prime(7) 

# 3. Function to print even numbers from a list
def even_from_list(l):
    result = [i for i in l if i % 2 == 0]
    print(result)
even_from_list([1,2,3,4,5,6,7,8,9])

# 4. Function to check if a string is palindrome
def palindrome(s):
    result = s == s[::-1]
    print(result)
palindrome("madam")

# 5. Function to find min of three numbers
def min_of_three(a, b, c):
    result = min(a, b, c)
    print(result)
min_of_three(10, 5, 8)

# 6. Function to print squares of numbers 1 to 30
def square_list():
    result = [i*i for i in range(1, 31)]
    print(result)
square_list()

# 7. Accessing a function inside a function
def outer():
    def inner():
        print("Inner function")
    inner()
outer()

# 8. Function to count upper and lower case letters
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print(upper, lower)
count_case("TasINcoder")

# 9. Function to check if a string is pangram
def pangram(s):
    result = set("abcdefghijklmnopqrstuvwxyz") <= set(s.lower())
    print(result)
pangram("The quick brown fox jumps over the lazy dog")

# 10. Function to check if two strings are anagrams
def anagram(s1, s2):
    result = sorted(s1) == sorted(s2)
    print(result)
anagram("listen", "silent")