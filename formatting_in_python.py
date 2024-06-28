# F-strings

name = "Alice"
age = 30
message = f"Hello, my name is {name} and I'm {age} years old."

print(message)

print("--------------------------------------------------")


# format() method

name = "Bob"
age = 25
message = "Hello, my name is {} and I'm {} years old.".format(name, age)

print(message)

print("--------------------------------------------------")

name = "Ivan"
city = "Zagreb"
street = "Krapinska 8"
print("Hello, my name is {} and I live in grad {}, {}.".format(name, city, street)   )


print("----------------------------------------------------")

# alignment

number = 123
print(f"{number:05}")
print(f"{number:<5}")
print(f"{number:>5}")
print(f"{number:\"^5}")
print(f"{number:-^5}")

print("----------------------------------------------------")

price = 19.99
print(f"The price is £{price:.2f}")
print(f"The price is £{price:,.2f}")