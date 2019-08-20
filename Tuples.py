tup1 = (1, 4, [5, 3, 8], 7, 9)
print(tup1)
tup1[2][1] = 2
print(tup1)

print("**************")

print("The element 1 appeared: ", tup1.count(1), "times in the tuple")
print("The element 8 appeared: ", tup1.count(8), "times in the tuple")
print("The element 5 appeared: ", tup1.count(5), "times in the tuple")

print("**************")

PurchaseDate = ("1/1/2017", "3/2/2017", "11/3/2017")
PurchasePrice = (55.85, 40.3, 21.9)
NumberOfItems = (3, 2, 4)

print("Purchase Date: ", PurchaseDate)
print("Purchase Price: ", PurchasePrice)
print("Number of Items: ",NumberOfItems)

total = sum(element for element in PurchasePrice)
print("The total amount paid for purchasing items :", round(total, 2))


