""" Assignment Details: 
ou are analyzing execution durations (in seconds) for 50 automated test cases across 5 cycles. 
a) Generate synthetic data using NumPy: 
 Create a 5x50 matrix (5 cycles × 50 tests) with random execution times between 5 and 
50 seconds. 
b) Perform the following analyses: 
1. Statistical Analysis 
o Calculate the average execution time per cycle. 
o Identify the test case with the maximum execution time in the entire dataset. 
o Find the standard deviation of execution times for each cycle to measure 
consistency. 
2. Slicing Operations 
o Extract the first 10 test execution times from Cycle 1. 
o Extract the last 5 test execution times from Cycle 5. 
o Extract every alternate test from Cycle 3. 
3. Arithmetic Operations 
o Perform element-wise addition and subtraction between Cycle 1 and Cycle 2. 
o Perform element-wise multiplication and division between Cycle 4 and Cycle 5. 
4. Power Functions 
o Square and cube all execution times. 
o Apply a square root transformation on the dataset. 
o Apply logarithmic transformation (np.log(array+1)) to normalize skewed data. 
5. Copy Operations 
o Create a shallow copy of the dataset and modify one cycle. Observe if the original 
changes. 
o Create a deep copy using .copy() and modify it. Confirm the original remains 
unchanged. 
6. Filtering with Conditions 
o Extract all test cases in Cycle 2 that take more than 30 seconds. 
o Identify tests that consistently (in every cycle) take more than 25 seconds. 
o  
o Replace all execution times below 10 seconds with 10 (minimum thresholding). 
Hints : 
  Use np.random.randint(5, 51, size=(5, 50)) to generate the dataset. 
  Use slicing (array[start:end:step]) for extracting subsets. 
  Use +, -, *, / directly on NumPy arrays for arithmetic. 
  Use np.power(), np.sqrt(), and np.log() for transformations. 
  Use .view() for shallow copy and .copy() for deep copy. 
  Use boolean indexing for filtering: array[array > 30].  """

import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate 5x50 matrix with execution times between 5 and 50 seconds
execution_data = np.random.randint(5, 51, size=(5, 50))
print("Generated Execution Data:\n", execution_data)


# Average exe time 
avg_per_cycle = np.mean(execution_data, axis=1)
print("\nAverage execution time per cycle:\n", avg_per_cycle)

# Test case with maximum execution time
max_time = np.max(execution_data)
max_test_index = np.unravel_index(np.argmax(execution_data), execution_data.shape)
print("\nMaximum execution time:", max_time)
print("Location of max time (cycle, test):", max_test_index)


# Standard deviation per cycle
std_per_cycle = np.std(execution_data, axis=1)
print("\nStandard deviation per cycle:\n", std_per_cycle)


first_10_cycle1 = execution_data[0, :10]
print("\nFirst 10 test times from Cycle 1:\n", first_10_cycle1)

last_5_cycle5 = execution_data[4, -5:]
print("\nLast 5 test times from Cycle 5:\n", last_5_cycle5)

alternate_cycle3 = execution_data[2, ::2]
print("\nAlternate tests from Cycle 3:\n", alternate_cycle3)


add_c1_c2 = execution_data[0] + execution_data[1]
print("\nAddition (Cycle 1 + Cycle 2):\n", add_c1_c2)

sub_c1_c2 = execution_data[0] - execution_data[1]
print("\nSubtraction (Cycle 1 - Cycle 2):\n", sub_c1_c2)


mul_c4_c5 = execution_data[3] * execution_data[4]
print("\nMultiplication (Cycle 4 * Cycle 5):\n", mul_c4_c5)

div_c4_c5 = execution_data[3] / execution_data[4]
print("\nDivision (Cycle 4 / Cycle 5):\n", div_c4_c5)


squared = np.power(execution_data, 2)
print("\nSquared execution times:\n", squared)

cubed = np.power(execution_data, 3)
print("\nCubed execution times:\n", cubed)

sqrt_transformed = np.sqrt(execution_data)
print("\nSquare root transformation:\n", sqrt_transformed)

log_transformed = np.log(execution_data + 1)
print("\nLogarithmic transformation:\n", log_transformed)


# Shallow copy
shallow_copy = execution_data.view()
shallow_copy[0, 0] = 999  # Modifies original
print("\nOriginal after shallow copy modification:\n", execution_data)


# Deep copy
deep_copy = execution_data.copy()
deep_copy[0, 0] = 888  # Original remains unchanged
print("\nDeep copy (modified independently):\n", deep_copy)


# Cycle 2 tests > 30s
cycle2_gt30 = execution_data[1][execution_data[1] > 30]
print("\nCycle 2 tests > 30s:\n", cycle2_gt30)


# Tests >25s in all cycles
consistent_gt25 = np.all(execution_data > 25, axis=0)
print("\nTests consistently >25s across all cycles:\n", consistent_gt25)


# Apply minimum thresholding
thresholded_data = execution_data.copy()
thresholded_data[thresholded_data < 10] = 10
print("\nThresholded data (min 10s):\n", thresholded_data)
