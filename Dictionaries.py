dict1 = {1: "one", 2: "two"}
dict2 = {3: "three", 4: "four"}
dict3 = {5: "five", 6: "six"}
dict4 = {**dict1, **dict2, **dict3}
print("dict4 = ", dict4)

print("**********************")

#n = int(input("Enter an integer: "))
#dictionary = {}


#for n in range(1, n+1):
#    dictionary[n] = n**2
#print(dictionary)

def char_frequency(text):
    dict = {}
    for n in text:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency(input('Enter text:')))