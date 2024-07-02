class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"

honeycrisp = Apple()
print(honeycrisp.color)

# prints "red"

print("-------------------------------------------------")

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor)
print(fuji.flavor)

# prints "sweet" and "tart"

print("-------------------------------------------------")

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)

honeycrisp = Apple("red", "sweet")
print(honeycrisp)

# prints "an apple which is red and sweet"

print("-------------------------------------------------")

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
jonagold = Apple("red", "sweet")
print(jonagold.color)

print("-------------------------------------------------")

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
jonagold = Apple("red", "sweet")
print(jonagold)

# Suggested code may be subject to a license. Learn more: ~LicenseLog:3093312095.
# prints "This apple is red and its flavor is sweet "

print("-------------------------------------------------")

class piglet:
    def speak(self):
        print("oink oinkey")
Hamlet = piglet().speak()

print("-------------------------------------------------")

class piglet:
    name = "piglet"
    def speak(self):
        return "Oink, I am {}.".format(self.name)
print("-------------------------------------------------")
Hamlet = piglet().speak()

print("-------------------------------------------------")
# Suggested code may be subject to a license. Learn more: ~LicenseLog:2062798286.
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __add__(self, other):
        if isinstance(other, Triangle):
            return self.area() + other.area()
        else:
            raise TypeError("Invalid operand type")

triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)

print("-------------------------------------------------")

numbers = [4, 2, 6, 7, 1]
numbers.sort()
print(numbers)

print("-------------------------------------------------")

names = ['Carlos', 'Igor', 'Alice']
print(names)
print(sorted(names))
print(sorted(names, key=len))