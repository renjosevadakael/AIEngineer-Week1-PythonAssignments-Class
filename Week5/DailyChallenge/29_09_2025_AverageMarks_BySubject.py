import pandas as pd

def averageMarksBySubject(data):
    # 1. Convert the dictionary into a Pandas DataFrame
    df = pd.DataFrame(data)
    
    # 2 & 3. Calculate the mean for the subject columns 
    average = df[["Math", "Science", "English"]].mean()
    
    # Print the final dictionary output
    print(average.to_dict())

# Example Input Data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Math": [80, 70, 90],
    "Science": [85, 75, 95],
    "English": [78, 82, 88]
}

# Execution
averageMarksBySubject(data)