""" Assignment Details: 
You are working on a QA analytics system. The system stores test execution times (in seconds) using 
NumPy arrays. 
Requirements: 
a) Create a base class TestReport with an attribute execution_times (NumPy array). 
b) In TestReport, implement methods: 
1. average_time() → returns the mean execution time. 
2. max_time() → returns the maximum execution time. 
c) Create a subclass RegressionReport that inherits from TestReport. 
 Add a method slow_tests(threshold) that returns all test cases taking more than the 
threshold time. 
d) In the main section: 
 Create a NumPy array with 10 execution times. 
 Create a RegressionReport object using this array. 
 Display average, max, and slow tests using the implemented methods. 
Hints to Solve: 
  Use np.mean() and np.max() for calculations. 
  Use boolean indexing in NumPy to filter slow tests, e.g., array[array > threshold]. 
  Use super().__init__() to pass the array to the parent class. """



import numpy as np

class TestReport:
    def __init__(self,execution_times):
        self.execution_times = np.array(execution_times)
    def average_time(self):
        print("Average Time " , np.mean(self.execution_times))
    def max_time(self):
        print("Max Time " , np.max(self.execution_times))

class RegressionReport(TestReport):
    def __init__(self,execution_times):
        super().__init__(execution_times)
      

    def slow_tests(self, threshold):
        slow_tests = self.execution_times[self.execution_times > threshold]
        print("Slow tests:", slow_tests)


if __name__ == "__main__":
    
    times = np.array([1.2, 3.5, 2.1, 4.8, 0.9, 2.7, 3.3, 1.8, 5.0, 2.4])
    
    report = RegressionReport(times)
    report.average_time()
    report.max_time()
    report.slow_tests(3)



