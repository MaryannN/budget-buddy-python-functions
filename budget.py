# Define your functions here

# Here's a function that's already been defined, but it's just a skeleton. It takes one argument (total) that we will pass to the function as an integer when we call it.

# 1. Replace "return" with code such that this function RETURNS the message "WARNING: Budget exceeded" if the total is over 100 dollars.

# def simple_budget_checker(total):
#   if total > 100:
#     return "Warning: Budget exceeded"
#   else:
#     return "You are on budget"
# print(simple_budget_checker(101))


# 2. Define a function called budget_checker that checks to make sure the total is less than 100 dollars.
#    If the total is over 100 dollars, return the message "WARNING: Budget exceeded"
#    If the total is under 100 dollars, return the message "You're under budget!"

# def budget_checker(total):
#   if total > 100:
#     return "Warning: Budget exceeded"
#   else:
#     return "You're under budget!"
# print(budget_checker(101))

# 3. Define a function called precise_budget_checker that checks to make sure the total is less than 100 dollars.
#    It should do exactly what the budget checker does, but it should ALSO return the message "STOP! Maximum reached" if the total is EXACTLY 100 dollars

# def precise_budget_checker(total):
#   if total > 100:
#     return "Warning: Budget exceeded"
#   elif total == 100:
#     return "STOP! Maximum reached"
#   else:
#     return "You're under budget!"
# print(precise_budget_checker(100))  

# 4. Write a function called ultimate_budget_checker that checks to make sure the total is less than 100 dollars.
#    If the total is under that amount, let the user know how many dollars they have left to spend.
#    If the total is over that amount, let the user know how many dollars worth of items they need to put back.

# def ultimate_budget_checker(total):
#   if total > 100:
#     over = total - 100
#     return f"put back ${over} " 
#   else:
#     under = 100 - total
#     return f"you have ${under} left to spend!"
# print(ultimate_budget_checker(101))
# print(ultimate_budget_checker(80))

# 5. Below is a function called flexible_budget_checker. It hasn't been fully defined yet, but you can see it takes two arguments.
#    It should be exactly like the ultimate_budget_checker, except it will check your total against a budget YOU enter into the function.
#    For example, the code flexible_budget_checker(40, 50) should return the message "WARNING: budget exceeded by 10 dollars."

# def flexible_budget_checker(total):
#   budget = int(input("Enter a budget: "))
#   if total > budget:
#     over = total - budget
#     return f"WARNING: budget exceeded by ${over}."
#   else:
#     under = budget-total
#     return f"You still have ${under}."
# print(flexible_budget_checker(50)) 

# 6. CHALLENGE: The trouble with the first four functions is that they only work for a budget of 100 dollars.
#    The trouble with the fifth function is that it makes the test provide the budget every time.
#    The best solution to this would be to have a global variable called budget before you start defining functions, and then use that variable in place of the number 100.
#    GOAL: Refactor (rewrite) the first four functions, but change the literal 100 to a global variable.
#    Then test out the functions to see if they still work if the budget (stored in the global variable) is cut down to 40 dollars.

budget = 100

#1
def simple_budget_checker(total):
  if total > budget:
    return "Warning: Budget exceeded"
  else:
    return "You are on budget"
print(simple_budget_checker(101))

#2
def budget_checker(total):
  if total > budget:
    return "Warning: Budget exceeded"
  else:
    return "You're under budget!"
print(budget_checker(101))

#3
def precise_budget_checker(total):
  if total > budget:
    return "Warning: Budget exceeded"
  elif total == budget:
    return "STOP! Maximum reached"
  else:
    return "You're under budget!"
print(precise_budget_checker(100))  

#4
def ultimate_budget_checker(total):
  if total > budget:
    over = total - budget
    return f"put back ${over} " 
  else:
    under = budget - total
    return f"you have ${under} left to spend!"
print(ultimate_budget_checker(101))
print(ultimate_budget_checker(80))

#5
def flexible_budget_checker(total):
  # budget = int(input("Enter a budget: "))
  if total > budget:
    over = total - budget
    return f"WARNING: budget exceeded by ${over}."
  else:
    under = budget - total
    return f"You still have ${under}."
print(flexible_budget_checker(50))
