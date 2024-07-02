product = 1
for n in range(1,10):
  product = product * n

print(product)


product = 1
n = 1
while n < 10:
  #print(product)
  product = product * n
  n += 1
print(product)

product = 1
n = 1           # Initialize n
while n < 10:   # Correct loop condition
    product = product * n
    n += 1
print(product)



for i in range (0, 100, 10):
   print(i)