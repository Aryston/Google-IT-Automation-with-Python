def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

greeting("Igor", "IT Support")


print(type(int(7)))

#
# algoritam za pretvaranje kilometara u metre
# 1) definiraj funkciju, npr. nek se zove kilometers_to_meters
# 2) definiraj varijable, dakle velicina u kilometrima kao polaziste

def kilometers_to_meters(size):
    size_in_kilometers = float(50000)               #fiksni brojcek
    size_in_meters = size_in_kilometers / 10000     #konvertira kilometre u metre
    return(size_in_meters)

#glavni program, dakle zovem funkciju
size_in_meters = kilometers_to_meters(float(50000))
print("Size in meters is: ", size_in_meters)