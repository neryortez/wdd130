# Also calculated the average cost per person after tax

child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

subtotal = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)

print()
print(f"Subtotal: ${subtotal:,.2f}")
print()

sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = subtotal * (sales_tax_rate / 100)
total = subtotal + sales_tax

total_people = number_of_children + number_of_adults
average_cost_per_person = total / total_people

print(f"Sales Tax: ${sales_tax:,.2f}")
print(f"Total: ${total:,.2f}")
print(f"Average Cost Per Person: ${average_cost_per_person:,.2f}")
print()

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total

print(f"Change: ${change:,.2f}")
