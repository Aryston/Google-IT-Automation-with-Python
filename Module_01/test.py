def fizzbuzz():
    for number in range(1, 101):  # Loop from 1 to 100
        if number % 15 == 0:      # Check if divisible by 3 and 5 (15)
            print("FizzBuzz")
        elif number % 3 == 0:     # Check if divisible by 3
            print("Fizz")
        elif number % 5 == 0:     # Check if divisible by 5
            print("Buzz")
        else:
            print(number)          # Print the number if no other conditions met

# Call the function
fizzbuzz()


number = 1
while number <= 100:
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1  


for i in range(1, 101):
    if i % 2 == 0:
        print(i)
print("------------------------------------------------")


# Prompt the user to enter a number
number = input("Enter a number: ")

# Check if the input is an integer (isdigit() is a string method that returns True if all characters in the string are digits, False otherwise)

try:
    # Attempt to convert the input to an integer
    number = int(number)
    if number.isdigit():
        print("The number {} is an integer.".format(number))
    else:
        print("The number {} is not an integer.".format(number))
except ValueError:
    # If the conversion fails, check if the input contains letters
    if number.isalpha():
        # Print an error message if the input contains letters
        print("Error: The input must be a number, not letters.")
    else:
        # Print an error message if the input contains special characters
        print("Error: The input must be an integer, not special characters.")
    # Exit the program
    exit()



# Check if the number is odd or even
if number % 2 == 0:
    print("The number {} is an even number.".format(number))
else:
    print("The number {} is an odd number.".format(number))


print("-------------------------------------------------")
