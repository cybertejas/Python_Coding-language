"""


your task is to implement a calculator


"""

#code

import math
import os

"""functions for code"""


def add():
    print("\n\nadding",calc_num,"and",calc_num2,"gives a summation of:",calc_num+calc_num2,"\n\n")
def sub():
    print("\n\nsubbtracting",calc_num,"and",calc_num2,"gives a difference of:",calc_num-calc_num2,"\n\n")
def mul():
    print("\n\nmultiplying",calc_num,"and",calc_num2,"gives a product of:",calc_num*calc_num2,"\n\n")
def div_quo():
    print("\n\ndividing",calc_num,"and",calc_num2,"gives a quotient of:",calc_num/calc_num2,"\n\n")
def div_rem():
    print("\n\ndividing",calc_num,"and",calc_num2,"gives a remainder of:",calc_num%calc_num2,"\n\n")
"""for other def"""

def fact():
    print("\n\nthe factorial of",calc_num_other,"is:-> ",math.factorial(calc_num_other),"\n\n")
def cube():
    print("\n\nthe cube of the number",calc_num_other,"is",calc_num_other**3,"\n\n")
def square():
    print("\n\nthe square of the number",calc_num_other,"is",calc_num_other**2,"\n\n")
def sqrt():
    print("\n\nthe square root of the number",calc_num_other,"is",math.sqrt(calc_num_other),"\n\n")
def cbrt():
    print("\n\nthe cube root of the number",calc_num_other,"is",math.cbrt(calc_num_other),"\n\n")

"""for trignometry"""

def sin():
    print(f"\n\nthe sin of number {calc_num_trig} is:",math.sin(calc_num_trig),"\n\n")
def cos():
    print(f"the cos of number {calc_num_trig} is:",math.cos(calc_num_trig),"\n\n")
def tan():
    print(f"the tan of number {calc_num_trig} is:",math.tan(calc_num_trig),"\n\n")

"""for clearing the screen"""

def clear():
    os.system('clear')
"""main code"""

while True:
    options = input("do you want basic arethmatic or other:-> ")
    if options == "other" or options == "OTHER" or options == "O" or options == "o":
        print("\n\ngoing to option other...\n\n")
        trig = input("do you want trig.:-> ")
        if trig == "yes" or "y" or "Y":

            print("\n\non the way to trig\n\n")
            operation_trig = int(input("\n\n\nenter a trig function\n\n1)sin\n2)cos\n3)tan\n\n-> "))
            calc_num_trig = int(input("\n\n\nenter a number to trig:-> "))
            if operation_trig == 1:
                sin()

            if operation_trig == 2:
                cos()

            if operation_trig == 3:
                tan()



        if trig == "no" or "n" or "N":
            operation_other = int(input("\n\n\nenter which operation you want to do\n\n1)fact\n2)cube\n3)square\n4)cbrt\n5)sqrt\n\n:-> "))
            calc_num_other = int(input("\n\nwhat is the number:-> "))
            if operation_other == 1:
                fact()


            if operation_other == 2:
                cube()


            if operation_other == 3:
                square()


            if operation_other == 5:
                sqrt()


            if operation_other == 4:
                cbrt()


        else:
            print("\n\ninvalid token or input. try again\n\n")

    elif options == "basic" or options == "arethmatic" or options == "a" or options == "A":

        operation = int(input("\n\n\n\n\nenter which to do\n\n1)add\n2)sub\n3)mul\n4)div-quo\n5)div-rem\n\n-> "))

        calc_num = int(input("\n\nenter 1st number:-> "))
        calc_num2 = int(input("\n\nenter 2nd number:-> "))


        if operation == 1:
            add()


        if operation == 2:
            sub()


        if operation == 3:
            mul()


        if operation == 4:
            div_quo()


        if operation == 5:
            div_rem()


    else:
        print("\n\ninvaled token or input, try again")



