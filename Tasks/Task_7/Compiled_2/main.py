import os
os.system('clear')
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
for i in range (0,6):
    for j in range (0,i+1):
        print(j+1, end=" ")
    print()