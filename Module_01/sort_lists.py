# Sort a list of numbers in ascending order
numbers = [4, 2, 6, 7, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 4, 6, 7]

# Print the original list of names
names = ['Carlos', 'Igor', 'Alice']
print(names)  # Output: ['Carlos', 'Igor', 'Alice']

# Sort the list of names in ascending order
print(sorted(names))  # Output: ['Alice', 'Carlos', 'Igor']

# Sort the list of names in ascending order based on the length of each name
print(sorted(names, key=len))  # Output: ['Alice', 'Igor', 'Carlos']
