import os
""" create a charity fund manager """

""" donate functions, for 1 dollar , for 2 dollar , 5 dollar ,  and 10 doller or any amount """

""" if it is 1$, it should print to the respected request """

""" every function has to return a value and print that value in a print after storing that value in a VAR """

os.system('clear')

def one_doller():
    print("thanks for donating 1$")

def two_doller():
    print("thanks for donating 2$")

def five_doller():
    print("thanks for donating 5$")

def ten_doller():
    print("thanks for donating 10$")

def any_doller():
    z = int(input(f"Dear {x} In option {y}, which amount you have to donate?:-> "))
    print(f"thanks for donating {z}")



x = input("enter your name:-> ")
y = int(input(f"\nSo dear {x}, tell me how much to donate? Hear are some of the options listed below\n1)for 1$\n2)for 2$\n3)for 5$\n4)for 10$\n5)for any amount\n\n:-> "))
if y == 1:
    one_doller()
elif y == 2:
    two_doller()
elif y == 3:
    five_doller()
elif y == 4:
    ten_doller()
elif y == 5:
    any_doller()
else:
    print("try again\n\n\n\n\n\n\n\n\n\n")








