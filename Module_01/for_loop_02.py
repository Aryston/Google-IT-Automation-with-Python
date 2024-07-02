teams = ['Milan', 'Inter', 'Juventus', 'Roma']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team, "vs", away_team)

print("-----------------------------------------")

greeting = 'Hello'
for char in greeting:
    print(char)

print("-----------------------------------------")

string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”

print("-----------------------------------------")


def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends("Barry")

print("-----------------------------------------")

greeting = 'Barry'
for char in greeting:
     print("Hi", char)
print("-----------------------------------------")

for x in ['1','2','3']:
    print(x)


