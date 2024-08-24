import os
os.system('clear')
# 1 
# 2 4
# 3 6 9 
# 4 8 12 16
num_1 = 1
for i in range (0,6):
    for j in range (1,i+2):
        print(j*num_1,end=" ")
    num_1 += 1
    print()
