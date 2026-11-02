# Self-Assessment
# 1. TODO: Describe the first bug YOU spotted, how you found it (traceback,
#    print statement, explaining out loud, or AI), and what that tells you
#    about your debugging instincts. Do not claim steps you did not do.
#
# 2. apply_discount takes an original price and a membership tier.
#    It takes 15% off for gold, 10% for silver, and 5% for bronze.
#    Any other tier gets no discount. It returns the price after the discount.
#    A colleague could use it with this explanation without reading its body.
#
# 3. AI disclosure: ChatGPT generated this script, identified and corrected
#    the three bugs in the provided file, and checked the script's output.
#    TODO: Explain whether reviewing this help built your understanding or
#    shortcut it, based on your own experience.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0
    return price * (1 - discount)


for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier + ':':8}${apply_discount(200, tier):.2f}")


# --- Exercise 3 ---
discounted_price = apply_discount(200, "gold")
total_price = discounted_price + calculate_tax(discounted_price, 0.07)
print(f"After gold discount: ${discounted_price:.2f}")
print(f"After tax: ${total_price:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
# Fixed version of the instructor's broken_sales.py:
# https://markumreed.github.io/ism2411/assets/downloads/broken_sales.py
#
# AI-provided diagnosis, not a record of independent student debugging:
# The missing colon causes a SyntaxError before any code can execute.
# Once that is fixed, total = sale keeps only the last sale (90).
# The <= condition eventually tries sales[5], causing an IndexError.
# This list has five items, so its valid indexes are 0 through 4.
#
# Optional trace statements are commented out below. Uncomment them to
# inspect the values yourself. Complete the personal reflection above.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    # Fix: Add each sale to the running total instead of replacing it.
    total += sale
    # print(f"sale={sale}, running total={total}")
print(f"Total: ${total}")

count = 0
# Fix: Add a colon at the end of the for statement to start its block.
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
# Fix: Stop before i equals the list length to stay within valid indexes.
while i < len(sales):
    # print(f"index={i}, list length={len(sales)}")
    print(sales[i])
    i += 1


# --- Exercise 6 ---
# Prediction: The output will be 100, 1998, and 100.
# Scope means where a variable can be used. The x inside double_it is
# local to that function. Giving it the value 999 does not change the
# global x outside the function, which stays 100.
x = 100


def double_it():
    x = 999
    return x * 2


print(x)
print(double_it())
print(x)
