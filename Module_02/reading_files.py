file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()

file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()

file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()

file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()


with open("spider.txt") as file:
    for line in file:
        print(line.upper())

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)