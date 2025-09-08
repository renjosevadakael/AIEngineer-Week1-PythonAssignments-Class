""" Assignment Details: 
Create a Python class named Book with the following: 
 Attributes: title, author, and publication_year. 
 A method get_age() that calculates and returns the age of the book in years (current year – publication_year). 
Requirements: 
  Define a class named Book. 
  Use the __init__ method to initialize attributes. 
  Define the get_age() method inside the class. 
  Create an object of the Book class and call the method to display the book’s age. """

from datetime import datetime

class Book:
    def __init__(self,title, author, publication_year):
        self.title=title
        self.author=author
        self.publication_year=publication_year

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.publication_year
    def get_title(self):
        return self.title

book = Book("ABC Maths", "Dr. S. Raman" , 2012)
bookAge= book.get_age()
print(f"Age of Book {book.get_title()} is {bookAge}.")
