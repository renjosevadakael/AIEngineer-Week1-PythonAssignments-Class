"""Calculate Final Bill Amount"""
import pandas as pd

def calculateTotalRevenue(data):
    df=pd.DataFrame(data)
    df['Quantity'] = pd.to_numeric(df['Quantity'],errors='coerce').fillna(0)
    df['Price'] = pd.to_numeric(df['Price'],errors='coerce').fillna(0)
    df['Total']=df['Quantity']*df['Price']
    #print(df['Total'])
    total_revenue= round(df['Total'].sum())
    return total_revenue

data={"Product":["Pen","Book","Bag","Laptop"],"Quantity":[10,5,2,1],"Price":[20,200,600,1500]}
print(calculateTotalRevenue(data))