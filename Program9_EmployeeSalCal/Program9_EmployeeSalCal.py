""" Assignment Details: 
Write a Python program that calculates the total salary of an employee using a function. 
1. Define a function calculate_salary(basic, hra, da, bonus=0). 
o basic, hra, and da are positional arguments. 
o bonus is a default argument (default = 0). 
2. The function should return the total salary = basic + hra + da + bonus. 
3. Call the function with and without passing the bonus argument.  """


def calculate_salary(basic, hra, da, bonus=0):
    return basic + hra + da + bonus

# Calling without bonus 
salary1 = calculate_salary(30000, 8000, 5000) 
print("Salary (without bonus):", salary1) 
# Calling with bonus 
salary2 = calculate_salary(30000, 8000, 5000, 2000) 
print("Salary (with bonus):", salary2) 