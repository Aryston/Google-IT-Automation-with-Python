# Practice Questions for Crash Course on Python

# Basic Python Syntax

# Write a Python program to print "Hello, world!"

print("Hello, world!")

print("------------------------------------------------")

# Write a Python program to add two numbers.

# Get the two numbers from the user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
# Add the two numbers.
sum = num1 + num2 + num3

# Print the sum.
print("The sum of {}, {} and {} the three numbers is: {:.2f}".format(num1, num2, num3, sum))
print("------------------------------------------------")
# Write a Python program to find the area of a triangle.

# Suggested code may be subject to a license. Learn more: ~LicenseLog:2726380781.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1115699100.
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
s = a * b * c
print("The area of the triangle is: {:.2f}".format(s))
print("------------------------------------------------")
# Write a Python program to check if a number is even or odd.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("Number {0} is Even".format(num))
else:
   print("Number {0} is Odd".format(num))
print("------------------------------------------------")

# Write a Python program to find the factorial of a number.

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1781963329.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:866330842.
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
)

# Loops

# Write a Python program to print all the numbers from 1 to 10.

for i in range (1, 11):
    print(i)

print("------------------------------------------------")

# Write a Python program to find the sum of all the numbers from 1 to 100.

sum = 0
for i in range(1, 101):
    sum += i
print("The sum of all numbers from 1 to 100 is: {}".format(sum))
print("------------------------------------------------")

# Write a Python program to print all the even numbers from 1 to 10.

for i in range(1, 11):
    if i % 2 == 0:
        print(i)
print("------------------------------------------------")

# Suggested code may be subject to a license. Learn more: ~LicenseLog:2687638707.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:3230927770.
# Write a Python program to print all the odd numbers from 1 to 10.

for i in range(1, 11):
    if i % 2 != 0:
        print(i)
print("------------------------------------------------")

# Suggested code may be subject to a license. Learn more: ~LicenseLog:2687638707.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:3230927770.
# Write a Python program to print all the even numbers from 1 to 100.

for i in range(1, 101):
    if i % 2 == 0:
        print(i)
print("------------------------------------------------")
# Write a Python program to find the factorial of a number using a loop.

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of {} is: {}".format(num, factorial))
print("------------------------------------------------")

# Write a Python program to print the multiplication table of a number.
# Strings

# Write a Python program to find the length of a string.
# Write a Python program to reverse a string.
# Write a Python program to check if a string is a palindrome.
# Write a Python program to find the first and last occurrence of a character in a string.
# Write a Python program to replace all occurrences of a character in a string.
# Lists and Dictionaries

# Write a Python program to create a list of numbers.
# Write a Python program to find the sum of all the elements in a list.
# Write a Python program to find the maximum and minimum element in a list.
# Write a Python program to create a dictionary.
# Write a Python program to find the value of a key in a dictionary.
# Final Project

# Write a Python program to read a file and print its contents.
# Write a Python program to write data to a file.
# Write a Python program to create a class.
# Write a Python program to create a function.
# Write a Python program to use a module.
# These are just a few examples of practice questions that you can use to test your understanding of the concepts covered in the Crash Course on Python. You can find more practice questions online or in textbooks.

# I hope this helps! Let me know if you have any other questions.

# And if you want to continue exploring this topic, try one of these follow-up questions:
