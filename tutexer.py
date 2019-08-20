import datetime
"""fi = open("foo.txt", "r+")

str = fi.read(10)
position = fi.tell()
print(position)
print("str is printed: ", str)
#print(li)
#line = fi.readLine(10)
#print(line)

fi.close()
"""







#dob = datetime.date(2001, 5,3 )
date_entry = input('Enter date of birth in YYYY-MM-DD format: ')
year, month, day = map(int, date_entry.split('-'))
dateofbirth = datetime.date(year, month, day)
print(dateofbirth)
