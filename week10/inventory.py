# Reflection 1:
# The most surprising thing about Python lists is that one list can be changed
# in place by adding, removing, or sorting its items. I also found negative
# indices useful because they let me access items from the end of the list.
#
# Reflection 2:
# In an accounting class, a Python list could help me work with daily sales
# figures instead of manually repeating calculations in Excel. I could use
# the same code to calculate totals and averages and identify high-sales days
# whenever I receive a new set of numbers.

# Exercise 1: Build the list.
print("Exercise 1")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Use positive and negative indices.
print("\nExercise 2")
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3: Slice the list.
print("\nExercise 3")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4: Modify the list and print after each operation.
print("\nExercise 4")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5: Catch an attempt to modify a tuple.
print("\nExercise 5")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: tuples cannot be changed after creation.")
    print("Tuples are useful for coordinates because they prevent accidental changes.")
print(coords)

# Exercise 6: Calculate sales statistics.
print("\nExercise 6")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7: Build a new list using an accumulator loop.
print("\nExercise 7")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))
print("Original:", prices)
print("Discounted:", discounted)

# Exercise 8: Filter sales above 300 and calculate their average.
print("\nExercise 8")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print("Count:", len(high_sales))
print(f"Avg: {sum(high_sales) / len(high_sales):.2f}")
