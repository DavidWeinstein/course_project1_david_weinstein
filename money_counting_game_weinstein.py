"""
This program is a change-counting game where the goal is for the suer to enter the number of coins to make exactly one dollar.
Constants for penny, nickel, dime, and quarter values, and total pennies in dollar.

Programmer: David Weinstein
Date: 9/23/2019
File Name: money_counting_game_weinstein.py

Pseudocode:
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

