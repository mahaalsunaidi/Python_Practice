'''M = {1: "Maha", 2: "Saad", 3: "AlSunaidi"}

print(M)
print("M Values: ", M.values())
print("M Keys: ", M.keys())

a = 10
b = 2
print(a ** b)'''

"""""
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

if __name__ == "__main__":
    string = "LOVE"
    print(reverse(string))

"""""

list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
print ("Max value element : ", max(list1))
print ("Max value element : ", max(list2))

list1 = ['physics', 'chemistry', 'maths']
list2=list(range(5)) #creates list of numbers between 0-4
list1.extend(list2)
print (list1)


list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.pop()
print ("list now : ", list1)
list1.pop(1)
print ("list now : ", list1)