# HW4: Arithmetic Operations in Daily Life

# Task 1: Grocery Store Math
    # Calculate the total cost of three items you'd commonly find in 
    # a grocery store, given their individual prices. For example, 
    # what would be the cost of bread, peanut butter, and jelly be? 
    # Prices don't need to be realistic

price_bread = 1.99
price_peanut_butter = 4.50
price_jelly = 4.99

total_cost = price_bread + price_peanut_butter + price_jelly

# print(total_cost)
# print("The total cost is $", total_cost)
print("The total cost is $" + str(total_cost))


# Task 2: Bank Interest
    # If you have a savings account with a particular initial amount and 
    # a fixed yearly interest rate, calculate the total amount in your 
    # account after a year. So if you had $10,000 at a 7% interest write 
    # code that would tell us the amount at the end of the year. For the 
    # example the expected outcome would be $10,700.

initial_amount = input("How much was your initial amount at the begining of year? ")
initial_amount = float(initial_amount)
total_amount = (initial_amount * .07) + initial_amount

# print(total_amount)
print("Your total amount at the end of year will be $" + str(total_amount))
