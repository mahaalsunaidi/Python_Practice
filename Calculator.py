def calculate():

    option = int(input(
        "Choose the operation you wish to apply on the numbers you entered:\n"
        " 1- sum \n "
        "2- subtract \n "
        "3- multiply \n "
        "4- division \n "
        "or 0 to quit \n"
    ))

    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if option == 0:
        print("Quit")

    if option == 1:

        add(number1, number2)

    elif option == 2:
        subtract(number1, number2)

    elif option == 3:
        multiply(number1, number2)

    elif option == 4:
        division(number1, number2)

    else:
        print("Invalid numbers")




def add(n1, n2):
    sum_result = n1 + n2
    print("The sum of ", n1, " and ", n2, " = ", sum_result)


def subtract(n1, n2):
    subtract_result = n1 - n2
    print("The subtraction of ", n1, " and ", n2, " = ", subtract_result)


def multiply(n1, n2):
    multiply_result = n1 * n2
    print("The multiplication of ", n1, " and ", n2, " = ", multiply_result)


def division(n1, n2):
    division_result = n1 / n2
    print("The division of ", n1, " by ", n2, " = ", division_result)


def repeat():
    
    again = input("Do you want to calculate different numbers? ")

    if again == 'yes':
        calculate()
    elif again == 'no':
        print("Thank you for trying our project")
    else:
        repeat()


calculate()
