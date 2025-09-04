"""
Assignment: Sales Data Analysis

This Python program analyzes a list of sales values and performs the following tasks:
1. Calculates and prints the total sales.
2. Calculates and prints the average sales.
3. Identifies and prints the highest sale.
4. Identifies and prints the lowest sale.

Requirements:
- Store the sales data in a list.
- Use the sum() function to calculate total sales.
- Use len() to determine the number of sales and compute the average.
- Use max() and min() to find the highest and lowest sales values.
"""
sales = [1200, 3400, 560, 4500, 2100] 

total_sales = sum(sales)
number_sales=len(sales)
average_sales=total_sales/number_sales
highest_sales=max(sales)
lowest_sales=min(sales)

print(f"Total Sales:  {total_sales}")
print(f"Average Sales:  {average_sales}")
print(f"Highest Sales:  {highest_sales}")
print(f"Lowest Sales:  {lowest_sales}")

