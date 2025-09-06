print("Hello, World!")
print('AI')
list=['Renju', 12, 3.14, True,None]
str=list[0]
print(str[0])
print(list)
dict={'name':'Renju','age':12,'height':3.14,'is_student':True,'address':None}
print(dict)

name = input("Enter your name: ")
print(type(name))
print("Hello, " + name + "!")
age = int(input("Enter your age: "))
print(type(age))
print("Your age is " , (age) )

Fruits = ['Apple', 'Banana', 'Mango', 'Orange']
for fruit in Fruits:
    print(fruit)
for i in range(0,len(Fruits)):
    print(Fruits[i])