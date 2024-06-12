import time
balance,withdraw,deposit = 1000,0,0
print("adding account details")

time.sleep(3)

deposit = 50
balance = deposit + balance
withdraw = 100
withdraw_1 = balance - withdraw

print("\n\nyou balanace is:",balance)
print("\n\n\nwithrawing money...")
time.sleep(5)
print("\n\nwithrawing",withdraw)
print("\n\n\nyour total money after withdrawal is:",withdraw_1)


