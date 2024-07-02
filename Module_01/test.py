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
