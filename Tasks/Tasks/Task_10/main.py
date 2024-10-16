import os
os.system('clear')
# write a code that gives a power of the number

def exponents(a, b):
    return a**b

x = int(input("enter a number you like\n:-> "))
y = int(input("\nenter a number to power it to\n:-> "))
z = exponents(x, y)
print(f"\n\nthe number {x} to its power {y} is = {z}")
