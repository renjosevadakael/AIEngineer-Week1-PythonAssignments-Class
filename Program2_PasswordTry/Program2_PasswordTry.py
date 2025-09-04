"""
Assignment: Password Retry System

This Python program implements a simple password retry mechanism.
- The correct password is set as "openAI123".
- The user is allowed up to 3 attempts to enter the correct password.
- If the correct password is entered within the allowed attempts, the program prints "Login Successful".
- If all 3 attempts fail, the program prints "Account Locked".

Requirements:
- Store the correct password in a variable.
- Use a loop (for or while) to allow 3 attempts.
- Compare the entered password with the correct one using string comparison (==).
- Stop the loop immediately if the user enters the correct password.
"""

correct_password="openAI123"
match_found=False
MAX_ATTEMPTS=3

for i in range(1,MAX_ATTEMPTS+1):
    entered_password= input("Attempt " + str(i) +" : Enter the password  :" )
    if(entered_password == correct_password):
        match_Found=True
        break
    else:
        match_Found=False

if(match_Found):
    print("Login Successful")
else:
    print("Account Locked")
     
    

