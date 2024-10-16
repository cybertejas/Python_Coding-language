def powerOfNum(base, exp):
    if exp ==0:
        return 1
    else:
        return base*powerOfNum(base,exp-1)

print(powerOfNum(12,2))