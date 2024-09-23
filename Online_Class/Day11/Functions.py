# Functions are coce blocks which is used go perform a specific task 

# Print something to console , Asking for user input , payment processing 
# 
# Payment Gateway - GooglePay , PhonePe , AmazonPay , Paytm 
# 
# User initiates the transactions  - 1 - Function1 
# Sending and processing  --- 2 - Functions2
# Successful -- Confirmations - 3 - Functions3 


# How to Identify a function  ---> name() ---> Funtion

# Types of Functions - User defined and Built-in 

# Built-in ----> We don't have def keyword with them 
# User-defined ----> def keyword is used 

# Parenthesis are used in both cases 

# print("Hello")
# def Hello():
#     pass
   
# Hello()

# Creating a functions 
def Greeting():
    print("Hello , I am Python Tutor")

#Calling am function
# Greeting()


# Passing the values to the functions 
def NewGreet(name):
    print("Hello ,"+name)

NewGreet("Python")
NewGreet("Golang")


# Returning values from functions 

# return keyword ----> 1. return some value from function

# 2. To exit the code execution 

def GreetWithMessage(name):
    return "Hello ",+ name+"! Welcome to New World."

# GreetWithMessage("Arvinder") #None 
X = GreetWithMessage("Arvinder")

print(GreetWithMessage())


