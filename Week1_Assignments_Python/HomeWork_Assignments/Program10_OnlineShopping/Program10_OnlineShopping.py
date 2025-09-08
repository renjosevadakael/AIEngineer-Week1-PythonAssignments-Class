""" Define a function calculate_bill(item_cost, quantity, tax=0.05, discount=0) 
where: 
o item_cost and quantity are positional arguments. 
o tax and discount are keyword arguments with default values. 
2. Formula: 
3. total = (item_cost * quantity) + (item_cost * quantity * tax) - discount 
4. Call the function in the following ways: 
o With only positional arguments. 
o With positional + keyword arguments (e.g., custom tax or discount).  """

def calculate_bill(item_cost, quantity, tax=0.05, discount=0):
    total = (item_cost * quantity) + (item_cost * quantity * tax) - discount 
    return total

print("Bill 1:", calculate_bill(500, 2)) 
# With custom tax 
print("Bill 2:", calculate_bill(500, 2, tax=0.1)) 
# With custom discount 
print("Bill 3:", calculate_bill(500, 2, discount=50)) 
# With custom tax and discount 
print("Bill 4:", calculate_bill(500, 2, tax=0.08, discount=100))

