""" Assignment Details: 
Create three classes: 
1. Employee → Base class with name. 
2. AutomationSkills → Class with method write_script(). 
3. AutomationTester → Inherits from both Employee and AutomationSkills, adds 
execute_tests(). 
Requirements: 
 Create Employee with __init__() for name. 
 Create AutomationSkills with method write_script() that prints "Writing Selenium 
scripts". 
 Create AutomationTester inheriting from both, with method execute_tests(). 
 Demonstrate by creating an AutomationTester object and calling all methods.  """

class Employee:
    def __init__(self,name):
        self.name=name

class AutomationSkills:
    def write_script(self):
        print("Writing Selenium scripts")

class AutomationTester(AutomationSkills,Employee):
    def __init__(self,name):
       super().__init__(name)
    def execute_tests(self):
        print(f"{self.name} is executing Tests")

at = AutomationTester('Renju')
at.write_script()
at.execute_tests()
