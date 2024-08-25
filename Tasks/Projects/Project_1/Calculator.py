#Calculator Code
def add(a,b):
    print(f"Addition of {a} and {b} is : {a+b}")
    
def sub(a,b):
    print(f"Difference of {a} and {b} is : {a-b}")

def mul(a,b):
    print(f"Product of {a} and {b} is : {a*b}")

def div(a,b):
    if b ==0:
        print("Division with zero is not possible.")
    else:
        print(f"Division of {a} and {b} is : {a/b}")

def display_menu():
    print("\n Welcome to Calculator \n")
    num1 = int(input("Enter First number:"))
    num2 = int(input("Enter Second number:"))
    print('''
            Select one option:
                    1. Addition
                    2. Subtraction
                    3. Multiplication
                    4. Division
''')
    choice = int(input("Enter your choice (1-4):"))
    if choice ==1 :
        add(num1, num2)
    elif choice==2:
        sub(num1, num2)
    elif choice==3:
        mul(num1, num2)
    elif choice ==4:
        div(num1, num2)
    else:
        print("Invalid Input")



display_menu()



