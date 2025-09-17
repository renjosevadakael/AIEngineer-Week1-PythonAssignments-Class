""" Assignment Details: 
Create a Python program to represent students with attributes and actions, and manage multiple  
student records using classes and objects. 
Requirements: 
a) Create a class named Student. 
b) Inside the class, define the following attributes: 
1. name → string 
2. grade → string 
3. department → string 
c) Implement the following methods: 
1. print_info() → prints all details of the student. 
2. update_grade(new_grade) → updates the student’s grade. 
d) In the main section (if __name__ == "__main__":): 
 Create at least three Student objects with different details. 
 Print each student’s information. 
 Update the grade of one student and print the updated details. 
 Manage and display multiple student records separately. """

class Student:
    def __init__(self,name,grade,department):
        self.name=name
        self.grade=grade
        self.department=department

    def print_info(self):
        print(f"Student Details are - Name : {self.name} , Grade :{self.grade} , Department :{self.department}")

    def update_grade(self,newGrade):
        self.grade=newGrade
        print(f"Updated Grade for Student {self.name} and New Grade is {self.grade}")

if __name__=="__main__":
    # Create multiple records for student
    student1 = Student("Renju","C", "CSE")
    student2 = Student("Anup","C", "ECE")
    student3 = Student("Joege","C", "EEE")
    #Store into a list
    students =[student1,student2,student3]
    # Print Individual Student Info
    print("Printing Individual Student Info")
    student1.print_info()
    student2.print_info()
    student3.print_info()

    # Print All Students Info iterating the List
    print("Printing Individual Student Info By Iterating List of Students")
    for student in students:
        student.print_info()

    # Update Grade for Student
    print("Update Grade for Student")
    print("Before")
    student1.print_info()
    student1.update_grade("A")
    print("After")
    student1.print_info()
 