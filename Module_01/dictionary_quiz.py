def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(f"{user}@{domain}")
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

print("----------------------------------------------------")

def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(f"{user}@{domain}")
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

print("----------------------------------------------------")

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():  
        # Now go through the users in the group
        for user in users:  
            # Check if the user is already in user_groups
            if user not in user_groups:
                # Create an empty list for the user's groups
                user_groups[user] = []  
            # Add the group to the user's list of groups
            user_groups[user].append(group)  
    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
        "public":  ["admin", "userB"],
        "administrator": ["admin"] }))

print("----------------------------------------------------")

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)



def add_prices(basket):
    total = 0
    # Iterate through the dictionary items
    for item_price in basket.values():  
        # Add each price to the total calculation
        total += item_price
    # Limit the return value to 2 decimal places
    return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Output: 28.44
