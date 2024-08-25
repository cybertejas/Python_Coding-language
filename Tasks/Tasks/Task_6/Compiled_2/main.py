import os
os.system('clear')
"""finding the product of even numbers till 15"""

prod = 1

for n in range(2,16):
    if n % 2 == 0:
        prod = prod * n
    else:
        continue
    # for j in range():
    # prod = prod * n

print(prod)