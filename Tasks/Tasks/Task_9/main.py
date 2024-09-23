import os
""" Create all the important function in the given ATM provided to you """

os.system('clear')


def pin_check():
        pass

def check_bal():
        print(f"your total balance is {total_bal}")

def add_money():
        pass

def with_money():
        pass

# def with_money(b):
#         if b == '1234':
#             return 1
#         else:
#             return 0

total_bal = 10000000

a = input("Hey user, whats your name:-> ")
os.system('clear')
# b = input(f"\nDear {a} please authenticate by the pin provided by the bank:-> ")
# check = with_money(b)
# if check == '1':
#         print("\n\nAuthenticated, continuing to the site..........")
# else:
#         print("\n\nAuthentication Failed, Please try again later or write the correct pin")
c = int(input("\n\nwhat do you want to do?:\n1)Deposit\n2)Withraw\n3)Total Money\n:-> "))
if c == 1:
        add_money()
elif c == 2:
        with_money()
elif c == 3:
        check_bal()
else:
        os.system('clear')
        print("\nPlease Try Again.")
        




