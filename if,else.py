amount = int(input("Enter an amount: "))
if amount < 1000:
    discount = amount * 0.05
    print("Discount is: ", discount)
else:
    discount = amount * 0.10
    print("Discount is: ", discount)