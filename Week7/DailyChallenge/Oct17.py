import numpy as np
import pandas as pd

def filterHighSales(data):
    df= pd.DataFrame(data)
    print(df)
    df['Total'] = df['Quantity'] * df['Price']
    filtered_df= df[df['Total'] >=1000]
    return filtered_df

data ={"Product" : ["Pen","Book","Bag","Laptop"],
       "Quantity" :[10,5,2,1],
       "Price" :[20,200,600,1500]}
print(data)
print(filterHighSales(data))