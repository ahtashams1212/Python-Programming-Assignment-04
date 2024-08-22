'''
   **Task**

You are tasked with creating a Python program that serves as an interactive tool for a friend who enjoys exploring numbers. 
The program should begin by prompting the user to enter their name and then ask them for three of their favorite numbers. 
After gathering this information, the program should greet the user with a personalized message that includes their name. 
The three numbers provided by the user should be stored in a list. The program should then check if any of the numbers are even or odd, 
and store this information in a separate list of tuples, where each tuple contains the number and a string indicating whether it is "even" or "odd". 
Following this, the program should use a for loop to iterate over the list of numbers, and for each number, it should create a tuple containing the 
number and its square. These tuples should be printed in a creative and engaging format. Additionally, the program should calculate the sum of the 
three numbers and print the result, accompanied by an encouraging message. Finally, the program should determine if the sum is a prime number and 
notify the user with an appropriate message. The goal is to make the tool both enjoyable and informative, allowing the user to explore their favorite 
numbers in a fun and interactive way, while also introducing some interesting logical checks.'''

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Step 1: Get user input
name = input("Enter your name: ")
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))

# Step 2: Store the numbers in a list
numbers = [num1, num2, num3]

# Step 3: Check if numbers are even or odd
even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

# Step 4: Greet the user
print(f"\nHello, {name}! Let's explore your favorite numbers:")

# Step 5: Print if the numbers are even or odd
for num, eo in even_odd_info:
    print(f"The number {num} is {eo}.")

# Step 6: Create and print tuples of numbers and their squares
print("\nHere are your numbers and their squares:")
for num in numbers:
    print(f"The number {num} and its square: ({num}, {num ** 2})")

# Step 7: Calculate the sum of the numbers
sum_numbers = sum(numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {sum_numbers}")

# Step 8: Check if the sum is a prime number
if is_prime(sum_numbers):
    print(f"Wow, {sum_numbers} is a prime number!")
else:
    print(f"{sum_numbers} is not a prime number, but it's still pretty cool!")
