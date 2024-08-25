import os
os.system('clear')
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1
var = 6
for i in range (0,6):
    for j in range (i,6):
        print(var, end=" ")
    var-=1
    print()