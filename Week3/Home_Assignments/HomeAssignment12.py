""" Assignment Details: 
You are simulating different QA roles analyzing test cycle data using NumPy. 
Requirements: 
a) Create three classes: ManualTester, AutomationTester, and PerformanceTester. 
b) Each class should have a method analyze(data) that takes a NumPy array of test execution 
times. 
 ManualTester → prints the first 5 test execution times (data[:5]). 
 AutomationTester → prints the fastest test case (data.min()). 
 PerformanceTester → prints the 95th percentile execution time (np.percentile(data, 
95)). 
c) Write a function show_analysis(tester, data) that calls the analyze() method. 
d) In the main section: 
 Create a NumPy array with at least 12 execution times. 
 Create objects of all three tester roles. 
 Call show_analysis() for each tester object. 
Hints to Solve: 
 
  Use NumPy slicing for ManualTester. 
  Use np.min() for AutomationTester. 
  Use np.percentile() for PerformanceTester. 
  Demonstrate polymorphism by calling the same analyze() method on different objects.  """

import numpy as np
class ManualTester:
   
    def analyze(self,data):
        print("First 5 test execution times", data[:5])

class AutomationTester:

    def analyze(self,data):
        print("Fastest test case ", data.min())

class PerformanceTester:
   
    def analyze(self,data):
        print("95th percentile execution time", np.percentile(data,95))

def show_analysis(tester, data):
    tester.analyze(data)

if __name__=="__main__":
     times = np.array([1.2, 3.5, 2.1, 4.8, 0.9, 2.7, 3.3, 1.8, 5.0, 2.4,1.3,2.8])

manual = ManualTester()
automation = AutomationTester()
performance = PerformanceTester()

show_analysis(manual, times)
show_analysis(automation, times)
show_analysis(performance, times)



    
