size = 10
height = 5.5
#formatted_string = "The size is {} and the height is {:.2f}".format(size, height)
formatted_string = "The size is {size} and the height is {height:.2f}".format(size=size, height=height)
print(formatted_string)

# palindrome

def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

#Testing the function
word = "level"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


#miles to kilometers

def miles_to_kilometers(distance_in_miles):
    conversion_factor = 1.60934
    distance_in_kilometers = distance_in_miles * conversion_factor
    return distance_in_kilometers

#Testing the function
distance_in_miles = 10
distance_in_kilometers = miles_to_kilometers(distance_in_miles)
print(f"{distance_in_miles} miles is equal to {distance_in_kilometers} kilometers.")