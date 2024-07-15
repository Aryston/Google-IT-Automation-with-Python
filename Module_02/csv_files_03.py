import csv

# Read software.csv
with open('software.csv', mode='r') as software_file:
    reader = csv.DictReader(software_file)  # Added 'mode='r'' explicitly
    for row in reader:
        print(f"{row['name']} has {row['users']} users")  # Using f-string for formatting

# Write by_department.csv
users = [
    {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
    {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"},
]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w', newline='') as by_department_file:  # Added newline='' for Windows compatibility
    writer = csv.DictWriter(by_department_file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users) 
