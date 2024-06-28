# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).
#
basket = [
    ("Peaches", 3.0, 2.99),
    ("Pears", 5.0, 1.66),
    ("Plums", 2.5, 3.99)
    ]


# Calculate the total price for each item (weight times price per pound)
# and add them up to get a subtotal.
#
subtotal = 0.00
for item in basket:
    fruit, weight, unit_price = item
    subtotal += (weight * unit_price)

# Now calculate the sales tax and total bill.
#
tax_rate = 0.06625 # 6.625% sales tax in New Jersey
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt


# Print the receipt for the customer.
#
print("Subtotal:", subtotal)
print("Sales Tax:", tax_amt)
print("Total:", total)


fruit = "peaches"
weight = 3.0
per_pound = 2.99


output = "You are buying {} pounds of {} at {} per pound.".format(weight, fruit, per_pound)
print(output)


output = "{1} are {2} per pound, and you have {0} pounds of {1}.".format(weight, fruit, per_pound)
print(output)


output = "{fruit} are {price} per pound, and you have {weight} pounds of {fruit}.".format(weight=weight, fruit=fruit, price=per_pound)
print(output)


# Print the receipt for the customer. The format string ":10,.2f" 
# works as follows:
#   - ":10" makes the output 10 characters wide.
#   - "," inserts thousands separators between groups of digits.
#   - ".2" limits the output to two digits after the decimal.
#   - "f" tells Python to expect a floating-point number.
#
print("Subtotal:     ${:10,.2f}".format(subtotal))
print("Sales Tax:    ${:10,.2f}".format(tax_amt))
print("Total:        ${:10,.2f}".format(total))