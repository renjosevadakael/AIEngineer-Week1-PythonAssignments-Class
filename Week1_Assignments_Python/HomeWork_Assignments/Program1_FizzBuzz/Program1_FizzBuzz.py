"""
Assignment: FizzBuzz Program

This Python program defines a function called fizzbuzz(n) that takes an integer n as input.
For every positive integer i from 1 to n, the function applies the following rules:
- Prints "FizzBuzz" if i is divisible by both 3 and 5.
- Prints "Fizz" if i is divisible by 3 but not 5.
- Prints "Buzz" if i is divisible by 5 but not 3.
- Prints the number itself (as a string) if none of the above conditions are met.

The program also prompts the user to enter a positive integer,
validates the input, and calls the fizzbuzz function with the given value.
"""
def fizzbuzz(n):
        if(n%3==0 and n%5==0):
            print("FizzBuzz")
        elif(n%3==0 and n%5!=0):
            print("Fizz")
        elif(n%3!=0 and n%5==0):
            print("Buzz")
        else :
            print(str(n))


user_input = int(input("Enter a positive integer: "))
if(user_input>0):
    fizzbuzz(user_input)
else:
    print("Enter positive integer")

