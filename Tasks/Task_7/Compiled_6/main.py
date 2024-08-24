import os
os.system('clear')
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
for i in range (0,7):
    for j in range(0,i+1):
        print("*", end=" ")
    print()


for i in range (7,0,-1):
    for j in range(0,i-1):
        print("*", end=" ")
    print()