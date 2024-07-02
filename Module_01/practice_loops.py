def digits(n):
    count = 0
    if n == 0:
        count += 1
    while n != 0:  # Loop until n becomes 0
        n //= 10   # Remove the last digit of n
        count += 1 # Increment the count by 1 for each digit
    return count

print("25:", digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

print("-------------------------------------------")

num1 = 0
num2 = 0

print("Starting outer loop:")
for x in range(5):
    num1 = x
    print(f"  num1 = {num1}")  # Print num1 after updating

    print("    Starting inner loop:")
    for y in range(14):
        num2 = y + 3
        print(f"      num2 = {num2}")  # Print num2 after updating

print("Final values:")
print(f"  num1 = {num1}")
print(f"  num2 = {num2}")
print("Sum:", num1 + num2)
