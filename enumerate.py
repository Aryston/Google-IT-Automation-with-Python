text = "Igor"
for index, char in enumerate(text, 1):
    print(f"Index: {index}, Character: {char}")

print("----------------------------------------------------")

multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)

#isto to ali jednostavnije

print("----------------------------------------------------")

multiples = [x*7 for x in range(1,11)]
print(multiples)
print("----------------------------------------------------")
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)
print("----------------------------------------------------")
#dijeljivi s 3
z = [x for x in range(0,101) if x % 3 == 0]
print(z)
print("----------------------------------------------------")
#list comprehension
print([x*7 for x in range (1,11)])

print("----------------------------------------------------")

def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]

print(odd_numbers(5))  # Output: [1, 3, 5]
print(odd_numbers(10)) # Output: [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Output: [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Output: [1]
print(odd_numbers(-1)) # Output: []

print("----------------------------------------------------")
def squares(start, end):
    return [start**2 for start in range(start, end+1)]


print(squares(2, 3))    # Should print [4, 9]
print(squares(1, 5))    # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))   # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("----------------------------------------------------")

list_of_tuples = [('Orange', 5), ('Banana', 3), ('Plum', 1)]
for tuple in list_of_tuples:
    print(tuple)