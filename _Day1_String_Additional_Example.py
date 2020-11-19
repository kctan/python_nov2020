Price = input("Enter price of item: ")

if Price.isdigit() :
    Price = int(Price)
    Discount = input("Enter discount in %: ")
    if Discount.isdigit() :
        Discount = int(Discount)
        answer = calc_disc ( Price, Discount )
        print("The discounted price for item is " + str(answer))            
    else:
        print("Please enter an integer for discount")
else:
    print("Please enter an integer for price")