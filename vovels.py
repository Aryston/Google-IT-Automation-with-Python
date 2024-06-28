input_string = "Hello, how are you?"
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_list = []

for char in input_string:
    if char.lower() in vowels:
        vowel_list.append(char)

print(vowel_list)

print("------------------------------------------")

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

print("------------------------------------------")

my_string = "Hello, World!"
lowercase_string = my_string.lower()
print(lowercase_string)

print("------------------------------------------")

for n in range(6,18+1,3):
  print(n*2)
#should print 2, 18, 24, 30, 36?
print("------------------------------------------")
for n in range(19):
    if n % 2 == 0:
        print(n)
print("------------------------------------------")
for n in range(0,18+1,2):
  print(n*2)

print("------------------------------------------")
for n in range(0,18+1,2):
  print(n*2)

print("------------------------------------------")
input = "Four score and seven years ago"
for c in input:
  if c.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(c, end=" ")
print()

