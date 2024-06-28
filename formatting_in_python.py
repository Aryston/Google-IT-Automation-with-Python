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

print("----------------------------------------------------")

fruit = "apple"
quantity = 5
print(f"I have {quantity} {fruit}")

print("----------------------------------------------------")

width = 10
height = 5
area = width * height
print(f"The area is {area}")
print("----------------------------------------------------")
#custom formatting

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __format__(self, format_spec):
        return f"{self.name} (Age: {self.age})"  # Custom formatting for Person objects

person = Person("Alice", 30)
print(f"{person}")  # Output: Alice (Age: 30)

print("----------------------------------------------------")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __format__(self, format_spec):
        if format_spec == "salary":
            return f"{self.name}'s salary is ${self.salary:.2f}"
        else:
            return f"{self.name} is an employee"  # Default format

emp = Employee("Alice", 65000)
print(f"{emp}")                  # Output: Alice is an employee
print(f"{emp:salary}")           # Output: Alice's salary is $65000.00
