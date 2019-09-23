"""
This program is a change-counting game where the goal is for the suer to enter the number of coins to make exactly one dollar.
Constants for penny, nickel, dime, and quarter values, and total pennies in dollar.

Programmer: David Weinstein
Date: 9/23/2019
File Name: money_counting_game_weinstein.py

Pseudocode:
1. Define constant variables: penny value, nickel value, dime value, quarter value, and total pennies in a dollar
2. Initial user input for number of coins
3. Check if any negative integers input
    3.1 If any negative intgers, have user choose new inputs
4. If no negative integers, continue on to check if total value of coins > one dollar
    4.1 If total value of coins > one dollar, print "the amount was more than one dollar"
5. If total value of coins < one dollar
    5.1 Print "the amount was less than one dollar"
6. Else print winning message, total value of coins must equal 0
"""

# Define constants.
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

# User prompt for number of coins
pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

# Error message for negative integer, rerun inputs if negative
while pennies < 0 or nickels < 0 or dimes < 0 or quarters < 0:
    print("The number should be a positive integer!")
    pennies = int(input("Enter the number of pennies: "))
    nickels = int(input("Enter the number of nickels: "))
    dimes = int(input("Enter the number of dimes: "))
    quarters = int(input("Enter the number of quarters: "))

# Check if more than one dollar
if pennies * PENNY_VALUE + nickels * NICKEL_VALUE + dimes * DIME_VALUE + quarters * QUARTER_VALUE > PENNIES_IN_DOLLAR:
    print("Sorry, the amount you entered was more than one dollar.")
# Check if less than one dollar
elif pennies * PENNY_VALUE + nickels * NICKEL_VALUE + dimes * DIME_VALUE + quarters * QUARTER_VALUE < PENNIES_IN_DOLLAR:
    print("Sorry, the amount you entered was less than one dollar.")
# Else print winning message
else:
    print("Congratulations!\nThe amount you entered was exactly one dollar!\nYou win the game!")
