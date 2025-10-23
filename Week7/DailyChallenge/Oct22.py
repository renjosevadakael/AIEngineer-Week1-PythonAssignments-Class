""" Sort by total sales"""

import pandas as pd

def sortProductBySales(data):
    dataFrame= pd.DataFrame(data)
    print("Original", dataFrame)
    dataFrame['Total'] = dataFrame['Quantity'] * dataFrame['Price']
    df_sorted = dataFrame.sort_values(by='Total', ascending=False)
    print("Sorted with Total\n", df_sorted)
    sorted_list_dictionaries= df_sorted.to_dict(orient='records')
    return sorted_list_dictionaries

data ={"Product" :["Pen","Book","Bag","Laptop"],
       "Quantity" :[10,5,2,1],
       "Price" :[20,200,600,1500]
}
print("Sorted List Of Dictionaries\n", sortProductBySales(data))