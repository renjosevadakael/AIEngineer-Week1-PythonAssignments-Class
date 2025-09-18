""" Assignment Details: 
 
        Create a Python program to represent employees in an IT organization using inheritance. 
 
Requirements: 
 
a) Create a base class Employee with the following attributes: 
 name → string 
 emp_id → string 
 department → string 
b) Add a method display_info() in Employee to print employee details. 
c) Create a subclass Manager that inherits from Employee and adds an attribute: 
 team_size → integer 
Override display_info() to also show team size. 
d) Create another subclass Developer that inherits from Employee and adds an attribute: 
 programming_language → string 
Override display_info() to also show programming language. 
e) In the main section (if __name__ == "__main__":): 
 Create one Manager and one Developer object with different details. 
 Call their display_info() methods to demonstrate inheritance and method overriding. 
Hints: 
1. Use super().__init__() in subclasses to call the parent constructor. 
2. Method overriding allows you to extend the functionality of the parent’s display_info(). 
3. Demonstrate how both roles reuse common properties (name, emp_id, department).  """


class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")

class Manager(Employee):
    def __init__(self, name, emp_id, department, team_size):
        super().__init__(name, emp_id, department)
        self.team_size = team_size

    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")

class Developer(Employee):
    def __init__(self, name, emp_id, department, programming_language):
        super().__init__(name, emp_id, department)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

# Main execution block
if __name__ == "__main__":
    # Create Manager and Developer objects
    manager = Manager("Renju Thomas", "M102", "QA Automation", team_size=8)
    developer = Developer("Aarav Nair", "D205", "Backend Development", programming_language="Python")

    # Display their info
    print(" Manager Info:")
    manager.display_info()

    print("Developer Info:")
    developer.display_info()