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


