"""finding the product of even numbers till 15"""

prod = 1

for n in range(2,16,2):
    prod = prod * n

print(prod)