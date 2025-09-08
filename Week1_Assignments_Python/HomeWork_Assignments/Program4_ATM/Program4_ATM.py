"""
Assignment: ATM Withdrawal Simulation

This Python program simulates a basic ATM withdrawal process.

Steps:
1. Prompt the user to enter a withdrawal amount.
2. The ATM dispenses cash only in multiples of ₹100.
3. If the entered amount is divisible by 100, print "Dispensing <amount>".
4. Otherwise, print "Invalid amount".

Requirements:
- Use input() to read the withdrawal amount.
- Convert the input to an integer.
- Use the modulo operator (%) to check divisibility by 100.
- Print the appropriate message based on the condition.
"""

amount= int(input("Enter the Withdrawal Amount : "))
if(amount%100 == 0):
    print(f"Dispensing {amount}")
else:
    print("Invalid amount")