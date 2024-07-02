def multiplication_table(number):
    # Initialize the multiplier variable
    multiplier = 1

    # Complete the while loop condition
    while multiplier <= 5:  # Loop until multiplier reaches 6 (for 1 through 5)
        result = number * multiplier

        # If the result is greater than 25, stop the loop
        if result > 25:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the multiplier
        multiplier += 1


# Call the function with different numbers
multiplication_table(3)
multiplication_table(5)
multiplication_table(8)
