"""


User can withdraw , deposit and view the balance:

- W for withdrawal 
- D for deposit 
- B for Balance

Balance = 100000 

MINIMUM Balance required in the account =1000 RS




"""

# code

import time

def pin_wth():
    pin = int(input("\nenter upi pin:-> "))
    if pin == 1234:
        time.sleep(3)
        print("\n\nwithdrawed. the total balance is now",total_money,"after withdrawing",bank_wdw,"\n\n\n")
    else:
        time.sleep(3)
        print("\n\ntry again\n\n\n","\n\n\n")



def pin_dep():
    pin = int(input("\nenter upi pin:-> "))
    if pin == 1234:
        time.sleep(3)
        print("\n\ndeposited money to the bank, your total money is",total_money,"after depositing",bank_dep,"\n\n\n")
    else:
        time.sleep(3)
        print("\n\ntry again\n\n\n","\n\n\n")



def pin_bal():
    pin = int(input("\nenter upi pin:-> "))
    if pin == 1234:
        time.sleep(3)
        print("\n\nyour balance is",total_money,"\n\n\n")
    else:
        time.sleep(3)
        print("\n\ntry again\n\n\n")



def add_money():
    bank_dep = int(input("\n\nenter how much $ you may deposit\n:-> "))
    print("\n\ndepositing...\n\n")
    time.sleep(3)
    pin_dep()












bank_bal = 100000
y = 0
print("\n\n\nsetting bank balance...")
time.sleep(2)
while y == 0:
    if bank_bal <= 1000:
        print("\n\ninsufficiant balance.. there should be more than 1000 in your ballance, total money is",bank_bal)
        add_money = input("\n\ndo you want to add money to access the bank, yes or no?: ")
        time.sleep(1)
        if add_money == "yes":
            add_money()
        else:
            y = 1
    else:
        bank = input("\n\n\n\n\nW for withdraw, D for deposit, B for check balance\n-> ")
        if bank == "W":
            bank_wdw = int(input("\n\nenter how much $ to withraw\n:-> ")) 
            if bank_wdw < 0:
                print("\n\ntry again\n")
            else:
                total_money = bank_bal - bank_wdw
                if total_money <= 0:
                    print("\n\ntry again")
                else:
                    print("\n\nwithdrawing...\n\n")
                    pin_wth()



        if bank == "D":
            bank_dep = int(input("\n\nenter how much $ you may deposit\n:-> "))
            print("\n\ndepositing...\n\n")
            time.sleep(3)
            total_money = bank_bal + bank_dep
            pin_dep()

        if bank == "B":
            print("\n\nviewing bank balance...\n\n")
            time.sleep(3)
            pin_bal()

