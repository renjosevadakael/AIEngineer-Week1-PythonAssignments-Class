""" Assignment Details: 
  Create a Python script named test_report.py that: 
1. Write Operation: 
o Create a file named report.txt and write the following sample test results: 
                              TestCase1 - Passed   
                              TestCase2 - Failed   
                              TestCase3 – Passed 
 Append Operation: Append 2 more test results to the same file: 
           TestCase4 - Passed   
     TestCase5 – Failed 
 Read Operation: Read the file and print the content line by line. 
 Summary: 
o Count the total number of tests, how many Passed, and how many Failed. 
o Print a summary like this: 
        Total Tests: 5   
        Passed: 3   
        Failed: 2   """

#Writing
try:
    with open("report.txt", "w") as f:
        f.write("TestCase1 - Passed\n")
        f.write("TestCase2 - Passed\n")
        f.write("TestCase3 - Failed\n")
    print("Writing to File ")
except Exception as e:
    print("Exception occured in Writing")

#Append
try:
    with open("report.txt", "a") as f:
        f.write("TestCase4 - Passed\n")
        f.write("TestCase5 - Passed\n")
    print("Appending to File ")
except Exception as e:
    print("Exception occured in Appending")

#Read
try:
    with open("report.txt", "r") as f:
        lines=f.readlines()
        for line in lines:
            print(line)       
    print("Reading from File ")
except Exception as e:
    print("Exception occured in Reading")

#Manipulation
try:
    passed = 0
    failed = 0
    with open("report.txt", "r") as f:
        lines=f.readlines()
    print("Total Number of Test Cases " , len(lines))
    for line in lines:
         if "Passed" in line:
              passed += 1
         elif "Failed" in line:
              failed += 1
              
    print("Failed Testcase are ", failed)       
    print("Passed Testcase are ", passed)   
except Exception as e:
    print("Exception occured in Reading")


