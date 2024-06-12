# Why Conditionals

#Without Conditionals
# print("First")
# print("Second")
# print("Third")

# if True :
#     print("Hello")

# if False :
#     print("Listen")
# else:
#     print("Hi")

#Truthy and Falsy values in Python
# 1 is treated as True 
if 1:
    print("Print 1")
# -1 is treated as True 
if -1 :
    print("Print -1")
# 0 is treated as False 
if 0 :
    print("Print 0")

# treated as True 
if True:
    print("True")
# treated as False 
if False :
    print("False")

# 3+4 is treated as True 
if 3+4 :
    print("Print 3+4")

# 3 > 4 is treated as False
if 3 > 4 :
    print("Print 3 > 4")

# "" -> Empty String is treated as False
if "":
    print("Empty String")

# " " String is treated as True
if " ":
    print("String")

# "A" is treated as True
if "A" :
    print("Print A")

# Will throw an error
# if A :
#     print("Print A without quotes")
x=20
# x ==20 can't be used except conditionals  
# x ==20

# if x =20 :
#     print("True / False")

if x ==20:
    print(x)


print("--------------------------------------------------------")
if x ==10 :
    print("10")
elif x ==20:
    print("20")
elif x==30 :
    print("30")
else : 
    print("I don't know")

