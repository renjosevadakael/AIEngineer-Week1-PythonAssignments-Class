""" Assignment Details: 
You are given a list of the first ten prime numbers: - prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] 
       Perform the following operations using list slicing and indexing techniques: 
a) Extract the middle five primes: Create a new list containing the five primes in the middle 
of the original list. 
b) Get every second prime: Create a new list containing every second number from the 
original list, starting from the beginning. 
c) Use negative indexing: Create a new list containing the last three primes of the list. 
d) Reverse the list: Create a new list that contains all the elements of the original list in 
reverse order. 
e) Descending Order: Sort the list in descending order and store it in a new list.  """



# Original list of prime numbers
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print("Original prime_numbers:", prime_numbers)

# a) Extract the middle five primes using slicing (indexes 2 to 6)
middle_five_primes = prime_numbers[2:7]
print("Middle five primes:", middle_five_primes)

# b) Get every second prime using step in slicing
every_second_number = prime_numbers[::2]
print("Every second prime:", every_second_number)

# c) Use negative indexing to get the last three primes
last_three_primes = prime_numbers[-3:]
print("Last three primes:", last_three_primes)

# d) Reverse the list using slicing with negative step
reverse_list_prime_numbers = prime_numbers[::-1]
print("Reversed prime_numbers:", reverse_list_prime_numbers)

# e) Sort the list in descending order using sorted() (returns a new list)
descending_order_sort = sorted(prime_numbers, reverse=True)
print("Sorted in descending order (new list):", descending_order_sort)

# f) Sort the original list in-place using .sort()
prime_numbers.sort(reverse=True)
print("Sorted in descending order (in-place):", prime_numbers)