# A function shpould be called to perform any operation / task 
# We can directly call the functions / A function can be called ny another function
# A function when it is called by itself --- Recursion


# def Hello():
#     print("Hello")
#     Hello()

# Hello()



def Decreement(x):
    if x<0:
        return 0
    else:
        
        Decreement(x-1)
        print(x)

Decreement(10)