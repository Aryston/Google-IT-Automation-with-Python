input_string = "Hello, how are you?"  # Initialize the input string
vowels = ['a', 'e', 'i', 'o', 'u']  # Initialize the list of vowels
vowel_list = []  # Initialize the list to store the vowels

for char in input_string:  # Iterate through each character in the input string
    if char.lower() in vowels:  # Check if the character is a vowel
        vowel_list.append(char)  # Add the vowel to the list

print(vowel_list)  # Print the list of vowels

print("------------------------------------------")

my_list = [1, 2, 3]  # Initialize the list
my_list.append(4)  # Add the element 4 to the end of the list
print(my_list)  # Print the list

print("------------------------------------------")

my_string = "Hello, World!"  # Initialize the string
lowercase_string = my_string.lower()  # Convert the string to lowercase
print(lowercase_string)  # Print the lowercase string

print("------------------------------------------")

for n in range(6,18+1,3):  # Iterate through the range from 6 to 18, incrementing by 3
  print(n*2)  # Print the value of n multiplied by 2

print("------------------------------------------")

for n in range(19):  # Iterate through the range from 0 to 18
    if n % 2 == 0:  # Check if the value of n is even
        print(n)  # Print the value of n

print("------------------------------------------")

for n in range(0,18+1,2):  # Iterate through the range from 0 to 18, incrementing by 2
  print(n*2)  # Print the value of n multiplied by 2

print("------------------------------------------")

for n in range(0,18+1,2):  # Iterate through the range from 0 to 18, incrementing by 2
  print(n*2)  # Print the value of n multiplied by 2

print("------------------------------------------")

input = "Four score and seven years ago"  # Initialize the input string
for c in input:  # Iterate through each character in the input string
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:  # Check if the character is a vowel
        print(c, end=" ")  # Print the vowel with a space
print()  # Print a new line


print("------------------------------------------")
input = "Four score and seven years ago"  # Initialize the input string
for c in input:  # Iterate through each character in the input string
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:  # Check if the character is a vowel
        print(c, end=" ")  # Print the vowel with a space
print()  # Print a new line


