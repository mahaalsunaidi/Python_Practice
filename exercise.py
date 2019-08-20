"""def names(str):
    print("Hello", name, "!!")


if __name__ == "__main__":
    name = input("What's your name? ")
names(name)


age = int(input("How old are you? "))
year = str((2018 - age) + 100)
print("You will be 100 year old in ", year)


number = int(input("Enter a number: "))
if number % 2 == 0:
    print("This is an even number")

else:
    print("Error: please enter a valid number")

num = int(input("Give me a number to check"))
check = int(input("Give me a number to divide by"))

if num % check == 0:
    print(num,"divides evenly with ",check, "and it = ", num/check)
else:
    print(num,"number doesn't divide equally with", check)"""


"""def intersect(s1, s2):
    list1 =[]
    for x in s1:
        if x in s2:
            list1.append(x)
    return list1


if __name__ == "__main__":
    str1 = "Banana"
    str2 = "Sacana"

print(intersect(str1, str2))

print('{} {}'.format(1, 2))
x = format(0.5, '%')

print(x)"""


def print_options():
    print()
    print("Options:")
    print(" 'p' print options")
    print(" 'c' convert from Celsius")
    print(" 'f' convert from Fahrenheit")
    print(" 'q' quit the program")


def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32


def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0


if __name__ == '__main__':
    choice = "p"
    while choice != "q":
        if choice == "c":

            c_temp = float (input("Celsius temperature: "))
            print("Fahrenheit:", celsius_to_fahrenheit(c_temp))
            choice = input("option: ")

        elif choice == "f":

            f_temp = float(input("Fahrenheit temperature: "))
            print("Celsius: ", fahrenheit_to_celsius(f_temp))
            choice = input("option: ")
        else:
            print_options()
            choice = input("option: ")


