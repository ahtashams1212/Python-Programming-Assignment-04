
# 1. Print Statements
# In Python, print() is used to display output.
print("Hello, World!")

#  2. Strings
# Strings are sequences of characters enclosed in quotes (single, double, or triple).
greeting = "Hello"
name = "Yasar"
message = greeting + ", " + name + "!"
print(message)

# 3. f-Strings
# f-Strings (formatted string literals) allow you to embed expressions inside string literals.
name = "Yasar"
age = 25
print(f"My name is {name} and I am {age} years old.")

# 4. Operators
# Operators are used to perform operations on variables and values. They include arithmetic, comparison, logical, and more.
a = 10
b = 5
print(a + b)  # Addition
print(a > b)  # Comparison
print(a > 0 and b < 10)  # Logical AND

# 5. Lists
# Lists are ordered, mutable collections of items.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Access second item
fruits.append("date")  # Add an item
print(fruits)

# 6. Tuples
#Tuples are ordered, immutable collections of items.
point = (10, 20)
print(point[0])  # Access first item
# Tuples can't be modified, e.g., point[0] = 15 would raise an error.

# 7. For Loops
# For loops allow you to iterate over a sequence (like a list, tuple, or string).
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
  
# 8. Input Handling
# The input() function allows you to capture user input.
name = input("Enter your name: ")
print(f"Hello, {name}!")
