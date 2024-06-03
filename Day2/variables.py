#Variables - is a container to stroe values 

#Write a program Greet someone 10 times in a day

# print("Hello Raju")
# print("Hello Raju")
# print("Hello Raju")
# print("Hello Raju")
# print("Hello Raju")
# print("Hello Raju")
# print("Hello Raju")
# print("Hello Raju")
# print("Hello Raju")
# print("Hello Raju")

# Problem - If we have to change the name of a person - I need to modify each line

name = "Raju"
print("Hello" , name)
print("Hello" , name)
print("Hello" , name)
print("Hello" , name)
print("Hello" , name)

"""
If I want to change the variable value 
"""
name = "Vikram"
print("Hello" , name)
print("Hello" , name)
print("Hello" , name)
print("Hello" , name)
print("Hello" , name)

"""
Variables - 
"""

x = 10
#variable = Value

print(x+10)   #Output : 20

# Variables can be reassigned 
x =45
print(x)      #Output : 45

"""
Naming convention for variables :
1. AGE , Age , age are three different variables 
""" 
Age = 30
AGE = 20
print("Age : ", Age)
print("AGE :",AGE)

"""
2. Use of reserved keyword is not allowed as variables.
main, def , while , for
"""
# for = 20
# print(for)

"""
3. Spaces and other special characters are not allowed in the variable name except _
"""
# $Arvi = 30
_arv = "Arvinder"


"""
4. Starting  character of a variable can't be a digit. 
"""
#4ASr = 30

#Shadowing 
"""
case 1 : 
"""
message = "Hello Go"
def Greet():
    message = "Hello Python"
    print(message)  #Hello Python 

Greet()

message2 = "Hello Go"
def Greet2():
    # message2 = "Hello Python"
    print(message2)  #Hello Go

Greet2()






