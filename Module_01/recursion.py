def factorial(n):
    """
    Recursive Factorial Calculation Manual

    Definition:
    - A recursive function is a function that calls itself within its own body.
    - It's a powerful technique for solving problems that can be broken down into smaller, self-similar subproblems.

    Components of a Recursive Function:
    1. Base Case:
        - The simplest possible input for which the solution is known directly.
        - It prevents the function from calling itself indefinitely.
        - It's the stopping point for the recursion.

    2. Recursive Case:
        - The function calls itself with a modified version of the input, moving closer to the base case.
        - This breaks the problem down into smaller subproblems.

    When to Use Recursion:
    - When a problem can be naturally divided into smaller, self-similar subproblems.
    - When the problem has a clear base case that can be easily defined.
    - When you want to write concise, elegant code (though sometimes at the cost of efficiency).

    When NOT to Use Recursion:
    - When the problem doesn't lend itself to a recursive structure.
    - When efficiency is critical, as recursive calls can sometimes be slower due to function call overhead.
    - When the recursion depth could be very large, as it might lead to stack overflow errors.

    Example: Factorial Calculation
    """

    # Base Case:
    if n < 2:  
        return 1  # Factorial of 0 or 1 is 1

    # Recursive Case:
    else:
        return n * factorial(n - 1)  
        # Calculate n! by multiplying n with (n-1)!

# Example Usage:
print(factorial(5))  # Output: 120



def factorial(n):
    if n < 2:
        return(1)
    return(n * factorial(n-1))
print(factorial(5))

def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factorial(4)


# My first recursive function

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


# Max recursion is 999

def factorial(n):
  if n < 2:
    return 1
  return n * factorial(n-1)

print(factorial(999))

#this will produce an error