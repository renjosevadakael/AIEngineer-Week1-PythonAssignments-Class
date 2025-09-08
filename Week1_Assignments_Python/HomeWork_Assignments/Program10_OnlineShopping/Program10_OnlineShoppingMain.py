import Program10_OnlineShoppingModule as module

if __name__=="__main__":
    bill1 = module.calculate_bill(500,2)
    print("Bill 1:", bill1) 
    bill2 = module.calculate_bill(500,2,tax=0.1)
    print("Bill 2:", bill2) 
    # With custom discount 
    bill3 = module.calculate_bill(500, 2, discount=50)
    print("Bill 3:", bill3) 
    # With custom tax and discount 
    bill4 = module.calculate_bill(500, 2, tax=0.08, discount=100)
    print("Bill 4:", bill4)

