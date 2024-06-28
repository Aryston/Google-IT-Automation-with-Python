for left in range(7):
    for right in range(left, 7):
        print("[", str(left), "|", str(right), "]", end=" ")
    print()


# star-pattern

for vertical in range(4):
    for horizontal in range(5):
        print("*", end=" ")
    print()

#rignt angled triangle

for vertical in range(4):       # Outer loop: Controls the rows (0, 1, 2, 3)
    for horizontal in range(vertical, 4):  # Inner loop: Controls columns, starting from the current row value
        if vertical < horizontal:    # Conditional print
            print(" ", end=" ")
        print("*", end=" ")       # Unconditional print
    print()                         # Newline after each row
print("---------------------------------------- ")



for vertical in range(4):
    for horizontal in range(vertical + 1):  # Start at 0 and go up to the current row value
        print("*", end=" ")
    print()



teams = [ 'AC Milan', 'Inter', 'Juventus', 'AS Roma']
for home_team in teams:
     for away_team in teams:
          if home_team != away_team:
               print(home_team, "vs", away_team)

greeting = 'Hello'
for char in greeting:
     print(char)

greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1
     
print("---------------------------------------- ")

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")