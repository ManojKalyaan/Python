from os import system
import art

def add(n1 , n2):
    return n1+n2

def sub(n1 , n2):
    return n1-n2

def mul(n1 , n2):
    return n1*n2

def div(n1 , n2):
    return n1/n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div}

def calculator():

    num1 = int(input("what is the first number?\n"))


    for operater in operations:
        print (operater)

    symbol = input("pick an operation symbol from above\n")

    opera = operations[symbol]

    num2 = int(input("what is the second number?\n"))

    first_ans = opera(num1,num2)

    print(f"{num1} {symbol} {num2} = {first_ans}")

    sec_op = input ("do you want to continue calculation?(Yes/No) or start fresh calculation (Fresh)\n").lower()

    if sec_op == "fresh":
        system("clear")
        print (art.logo)
        calculator()
    
    while sec_op == "yes":

        for operater in operations:
            print (operater)

        symbol = input("pick another operation symbol from above\n")

        num3 = int(input("what is the next number?\n"))

        opera = operations[symbol]

        second_ans = opera(first_ans,num3)

        print(f"{first_ans} {symbol} {num3} = {second_ans}")

        first_ans = second_ans

        sec_op = input ("do you want to continue calculation?(Yes/No) or start fresh calculation (Fresh)\n").lower()

        if sec_op == "fresh":
            system("clear")
            print (art.logo)
            calculator()
    system("clear")


system("clear")
print (art.logo)
calculator()
