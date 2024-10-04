# NO return no passing 
"""
def Greet():
    print("This function neither accepts arguments nor returns anything.")

Greet()
"""
# no return passing 
"""
def Greet(name):
    print(f"This function accepts a value : {name} but does not return anything.")

Greet("Arvinder")
"""

# return no passing
"""
def Greet():
    return f"This function returns a value but does not accept anything."

print(Greet())
"""

# We store the result in a variable 

# x = Greet()
# print(x)

# return passing
def Greet(name):
    return f"This function returns a value and also accepts a value : {name}."

# print(Greet("Arvinder"))
x = Greet("Arvinder")
print(x)
