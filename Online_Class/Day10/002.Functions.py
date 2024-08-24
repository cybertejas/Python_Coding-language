def first():
    print("I am first Function")    #print---->1
    second()                        #6
    print("Function calls ended")        # print ---->4

def second():
    third()                         #10
    print("I am second Function")       # print---->3

def third():
    print("I am third Function")        #print----> 2


# function calls are pushed to stack
first()
# third()
# second()