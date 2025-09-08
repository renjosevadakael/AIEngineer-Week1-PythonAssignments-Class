"""
Assignment: Employee List Printer

This Python program maintains a hardcoded list of 5 employee names and prints each name in order,
numbered from 1 to 5.

Steps:
1. Create a list containing 5 employee names.
2. Use a for loop to iterate over the list.
3. Print each name with its corresponding number in the format:
   1. Name
   2. Name
   3. Name

Hints:
- Use a list such as: employees = ["Alice", "Bob", "Charlie", "David", "Eve"]
- Use the built-in enumerate() function to get both index and name.
"""

employees = ["Alice", "Bob", "Charlie", "David", "Eve"]

for index, employee in enumerate(employees, start=1):
    print(f"{index}. {employee}")

