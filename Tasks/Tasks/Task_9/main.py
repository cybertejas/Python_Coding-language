import os
from time import sleep as st

def clear():
        st(1)
        os.system('clear') 
        st(1)


""" Create all the important function in the given ATM provided to you """
try:
        clear()
        a = input("Hey user, whats your name:-> ")

        total_bal = 10000000




        def add_money(money,tb):
                if money > 0:
                        total_bas = money + tb
                        return total_bas
                else:
                        clear()
                        print("please try again")
                        clear()
                                

        def with_money(money,tb):
                if money > 0:
                        if money > tb:
                                clear()
                                print("please try again")
                                clear()
                        else:
                                total_bas = tb - money
                                return total_bas
                
                else:
                        clear()
                        print("please try again")
                        clear()


        def pin_check_deposit(a,b):
                if a == b:
                        clear()
                        print("please try again")
                        clear()
                else:
                        total_bal = add_money(dep_mon,total_bal)
                        print("your balance after depositing rs",dep_mon,"is :->",total_bal)
                        st(2)

        def pin_check_withdraw(a,b):
                if a == b:
                        clear()
                        print("please try again")
                        clear()
                else:
                        total_bal = with_money(withraw_money,total_bal)
                        print("you balance after withdrawing rs",withraw_money,"is :->",total_bal)
                        st(2)



        while True:

                clear()

                c = input(f"\n\nSo {a}, what do you want to do?:\n1)Deposit\n2)Withraw\n3)Total Money\n:-> ")
                if c.isdigit:
                        c = int(c)
                        if c == 1:
                                clear()
                                dep_mon = input('How much do you want to deposit?:-> ')
                                if dep_mon.isdecimal:
                                        dep_mon = float(dep_mon)
                                        clear()
                                        check_pin = int(input("enter your upi pin:-> "))
                                        correct_pin = 1234
                                        pin_check_deposit(check_pin,correct_pin)
                                        clear()

                                else:
                                        clear()
                                        print("try again")
                                        clear()
                                
                        elif c == 2:
                                clear()
                                withraw_money = input('How much do you want to withraw?:-> ')
                                if withraw_money.isdecimal:
                                        withraw_money = float(withraw_money)
                                        clear()
                                        check_pin = int(input("enter your upi pin:-> "))
                                        correct_pin = 1234
                                        pin_check_deposit(check_pin,correct_pin)
                                        
                                else:
                                        clear()
                                        print('please try again')
                                        clear()


                        elif c == 3:
                                clear()
                                print("total balance is",total_bal)
                                st(2)
                                
                        else:
                                clear()
                                print("please try again")
                                clear()
                else:
                        clear()
                        print("please try again")
                        clear()
                        





except KeyboardInterrupt:
        os.system('clear')
        print("\nProgram interrupted! Exiting...")
        st(1)
        os.system('clear')


except ValueError:
        os.system('clear')
        print("\nInvaled Value! Retry...")
        st(1)
        os.system('clear')






