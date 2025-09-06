""" Assignment Details: 
You are given a list of student marks: 
marks = [78, 85, 62, 90, 55, 88] 
Write a Python program to: 
1. Print the highest and lowest marks. 
2. Print the average marks. 
3. Print all marks above 75 (distinction). 
4. Add a new mark 95 to the list. 
5. Remove a mark 55 from the list. 
6. Sorting of the marks  """

marks = [78, 85, 62, 90, 55, 88] 
# 1. Print the highest and lowest marks. 
print(f"Highest Mark , {max(marks)}")
print(f"Lowest Mark , {min(marks)}")
# 2 Print the average marks. 
average= sum(marks)/len(marks)
print(f"Average Mark , {average}")
#3. Print all marks above 75 (distinction). 
for i in marks:
    if(i > 75):
        print(f"Above 75(Distinction), {i} ")
# 4. Add a new mark 95 to the list. 
marks.append(95)
print(marks)

#5. Remove a mark 55 from the list. 
marks.remove(55)
print(marks)

#6. Sorting of the marks  
marks.sort(reverse=True)
print(marks)

    