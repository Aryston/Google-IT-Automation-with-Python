def is_power_of_two(number):
    # Base case: 0 is not a power of two
    if number == 0:
        return False
    while number % 2 == 0:
        number //= 2  # Use floor division (//) to ensure integer results

    # If after dividing, number is 1, it's a power of two
    return number == 1


# Calls to the function
print(is_power_of_two(0))  # False
print(is_power_of_two(1))  # True
print(is_power_of_two(8))  # True
print(is_power_of_two(9))  # False
