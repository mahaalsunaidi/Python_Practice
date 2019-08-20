import operator
import math
'''var = 10
while var < 15:
   num = input("Enter a number: ")
   print("the number you entered is ", num)
   var +=1
print("thank you!!")'''

"""fruits = ["apple", "mango", "orange", "banana", "grape", "strawberry", "peach"]
for index in range(0, 4):
    print(fruits[index])
print(len(fruits))
print(list(range(3)))"""""

"""numbers = [11, 33, 55, 39, 55, 75, 37, 21, 23, 41, 13]
for num in numbers:
    if num % 2 == 0:
        print("there's an even number")

else:
        print("there's no even number")"""

"""dic1= {1:"Atheer", 2:"Aljohara", 3:"Laila", 4:"Nura"}
print(dic1)
dicsort = sorted(dic1.items(), reverse=False)
print(dicsort)
dicrev = sorted(dic1.items(), reverse=True)
print(dicrev)
dic1.update({5:"Maha"})
print(dic1)
dic2 = {1:10}
dic3 = {2:20}
dic4 = {3:30}
dic5 = {}
for d in (dic2, dic3, dic4):
    dic5.update(d)
print(dic5)"""
"""list = []
for n in range(2000, 3200):
    if n % 7 == 0 and not n % 5 == 0:
        list.append(n)
print(list)"""

"""def facto(x):
    if x == 0:
        return 1
    return x * facto(x-1)


num = int(input("enter a number: "))
print(facto(num))"""

"""dic = {}
num = int(input("Enter a number: "))
for n in range (1, num+1):
    dic.update({n:n*n})
print(dic)"""
'''values = input()
l = values.split(",")
t = tuple(l)
print(sorted(l))
print(t)'''

"""class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


if __name__ == '__main__':
    square = shape(10,10)
    print(square.area())"""













'''num = int(input("Enter a number to convert it to binary: "))
binary = bin(num)

print(binary)'''














"""str = input("Enter a text to reverse it: ")
#print(str[::-1])
rev = "".join(reversed(str))
print(rev)"""
















"""str = input("Enter a sentence to capitalize it ")
cap = str.upper()
print(cap)"""









"""


dic= {1:100,2:200,3:300,4:400}
print("Maximum value = ",max(dic.values()))
print("Minimum value = ", min(dic.values()))

"""













"""for n in range (1,16):
    dic[n] = n*n
print(dic)"""








"""def countbits(number):
    return int((math.log(number)/math.log(2)) +1)

num = 65
print(countbits(num))"""






"""num = 3.000001345
print("{:.2f}".format(num))"""










"""num = 3481/3

print("{:.2f}".format(num))"""






"""num = int(input("Enter a number to check: "))
y = "{0:b}".format(num)
print(y)
print(len(y))"""

print("**********************")


"""str = input("enter a text to capitalize it: ")
print(str.upper())"""

"""wrd = input("enter a word: ")
rev = "".join(reversed(wrd))
print(rev)"""

"""def funli(x):
    return list(set(x))

a = [1,2,4,5,6,4,7,1]
print(a)
print(funli(a))"""

"""list1 = [(10,20,50),(30,60,70),(10,30,90)]

print([t[:-1]+(400,) for t in list1])"""






class Circle:
    def __init__(self,r):
        self.radius = r


    def area(self):
        return self.radius ** 2 * 3.14


    def prtimeter(self):
        return 2 * self.radius * 3.14

if __name__ == '__main__':
    C = Circle(8)
    print(C.area())
    print(C.prtimeter())















