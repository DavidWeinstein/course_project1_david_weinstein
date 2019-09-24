"""
This program is a WiFi diagnostic tree to do some basic troubleshooting for a bad WiFi connection.

Programmer: David Weinstein
Date: 9/23/2019
Filename: wifi_diagnostics_tree_weinstein.py

Pseudocode:
1. Set answer variable equal to no, to use with while loop.
2. Make list of possible diagnosis.
3. Set variable for user input of "Did that fix the problem?".
4. Set count to 0 in order to index through the diagnostics.
5. While answer is equal to "no"
    5.1 Print the current diagnosis from list.
    5.2 Ask user if that fixed the problem.
    5.3 Iterate count by one.
        5.3.1 if answer is yes print "glad to be of help"
        5.3.2 if answer remains "no" loop back through to second diagnosis until answer == "yes" or we come to final solution of "Get a new router"
"""

# Set answer to no for while loop
answer = "no"

# List of diagnostic steps, and final step if nothing works.
diagnosis = ["Reboot the computer and try to connect.",
    "Reboot the router and try to connect.",
    "Make sure the cables between the router & modem are plugged in firmly.",
    "Move the router to a new loaction and try to connect."
]
finalStep = "Get a new router."

# Variable for user input string
fixInput = "Did that fix the problem? "

# Count to be iterated by one to use for indexing through list
count = 0

# While loop will loop through diagnosis list until a soluion is found or we come to the final step.
while answer == "no" and count < len(diagnosis):
    print(diagnosis[count])
    answer = input(fixInput)
    count += 1
    if answer == "yes":
        print("Glad to be of help.")
    elif count == len(diagnosis) and answer == "no":
        print(finalStep)
