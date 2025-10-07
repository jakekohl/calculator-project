# starting variables
meal_cost = 44.50
tax_rate = 6.75 / 100
tip_rate = 15.0 / 100

# calculate the cost after tax
meal_with_tax = meal_cost + meal_cost * tax_rate

# calculate the total cost
total_cost = round(meal_with_tax + meal_with_tax * tip_rate, 2)

print(f"Total cost of the meal: ${total_cost:.2f}")