""" Assignment Details: 
Create two classes: 
1. Employee → Base class with attributes name and employee_id. 
2. Tester → Child class inheriting from Employee, with an additional method run_tests() 
that prints "<name> is running automation tests". 
Requirements: 
 Create an Employee class with __init__() to store employee name and ID. 
 Create a Tester class that inherits from Employee. 
 Add a method run_tests() in Tester. 
 Create an object of Tester and demonstrate both parent and child methods """

class Employee:
    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id

class Tester(Employee):
    def __init__(self,name,employee_id):
         super().__init__(name,employee_id)
    def run_tests(self):
        print(f"{self.name} is running automation tests")

t1= Tester('Renju',197101)
t1.run_tests()