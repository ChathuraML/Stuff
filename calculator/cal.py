import os
import art


print(art.logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def dev(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": dev
}

ans = True
n1 = float(input("Type the first number: "))
while ans:
    for symbol in operators:
        print(symbol)

    task = input("Pick an operator: ")

    if task not in operators:
        print("Please enter a valied operator.")
        break
    
    n2 = float(input("Type the next number: "))
    
    result = operators[task](n1,n2)
    
    if result:
        print(f"{n1} {task} {n2} = {result}")
        next_operation = input(f"Type 'y' to contineue with {result}, or 'n' to start a new calculation. ")
        if next_operation == 'y':
            n1 = result
        elif next_operation == 'n':
            os.system("cls")
            n1 = float(input("Type the first number: "))
        else:
            print('''
==========================
   CALCULATOR CLOSED 🧮
==========================
                  ''')
            break
    else:
        ans = False


