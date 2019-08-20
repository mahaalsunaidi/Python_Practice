def add(num1, num2):

    res = num1 + num2
    return res


def multiply(num1, num2):
    res = num1 * num2
    return res


def print_num(num1, num2):
    print(num1, num2)


if __name__ == '__main__':
    option = '0'
    while option != '4':

        if option == '1':
            num1 = int(input("Enter the first number"))
            num2 = int(input("Enter the second number"))
            add(num1,num2)
        elif option == '2':
            num1 = int(input("Enter the first number"))
            num2 = int(input("Enter the second number"))
            multiply(num1, num2)
        elif option == '3':
            num1 = int(input("Enter the first number"))
            num2 = int(input("Enter the second number"))
            print_num(num1, num2)
        else:
            print("Enter the number of operation:  ")
            print("1 for adding two numbers")
            print("2 for multiplying two numbers")
            print("3 for printing the two numbers you entered")
            print("4 to exit")
            choice = input("Choose an operation:")








