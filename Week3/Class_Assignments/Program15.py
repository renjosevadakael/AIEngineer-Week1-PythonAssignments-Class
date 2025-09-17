""" Assignment Details: 
    Create three classes: 
1. Person → Base class with attribute name. 
2. Employee → Inherits from Person, adds employee_id. 
3. Manager → Inherits from Employee, adds team_size and method show_details(). 
Requirements: 
 Create Person with __init__() to store name. 
 Create Employee extending Person with employee_id. 
 Create Manager extending Employee with team_size. 
 Demonstrate by creating a Manager object and printing all attributes. """

class Person:
    def __init__(self,name):
        self.name=name
        

class Employee(Person):
    def __init__(self,name,employee_id):
         super().__init__(name)
         self.employee_id=employee_id

class Manager(Employee):
    def __init__(self,name,employee_id,team_size):
         super().__init__(name,employee_id)
         self.team_size=team_size
    def show_details(self):
        print(f"Name is {self.name} , Employee_Id is {self.employee_id} and  Team Size is {self.team_size}")


m1=Manager('Renju', 197101, 6)
m1.show_details()
