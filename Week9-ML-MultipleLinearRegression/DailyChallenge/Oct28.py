"""Apply Discount on High Priced Products"""
import pandas as pd

def applyDiscount(data):
    df= pd.DataFrame(data)
    high_priced_mask=df['Price']>=500
    df['DiscountedPrice']=df['Price']
    df.loc[high_priced_mask,'DiscountedPrice']=df.loc[high_priced_mask,'Price']*0.9
    updated_list= df.to_dict('records')
    print(df)
    print(updated_list)

data={"Product":["Pen","Book","Bag","Laptop","Shoes"],
      "Price":[20,200,600,1500,800],
      "Quantity":[10,5,2,1,3]
      }
applyDiscount(data)
