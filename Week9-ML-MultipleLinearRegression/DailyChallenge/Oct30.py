import pandas as pd

def calculate_final_bill_amount(product_data):
    df = pd.DataFrame(product_data)
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0)
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0)
    df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce').fillna(0)
    df['FinalAmount'] = df['Price'] * df['Quantity'] * (1 - (df['Discount'] / 100))
    return df.to_dict('records')

example_input = {
    "Product": ["Pen", "Book", "Bag", "Laptop"],
    "Price": [20, 200, 600, 1500],
    "Quantity": [10, 5, 2, 1],
    "Discount": [0, 10, 20, 15]
}

final_bill_list = calculate_final_bill_amount(example_input)
print(final_bill_list)