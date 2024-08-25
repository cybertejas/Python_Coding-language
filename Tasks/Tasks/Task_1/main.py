"""


Fizz Buzz Problem states that given an integer n, for every integer i <= n, the task is to print “FizzBuzz”
if i is divisible by 3 and 5, “Fizz” if i is divisible by 3, “Buzz” if i is divisible by 5 or i .(as a string) 
if none of the conditions are true


"""

#code
while True:

    print("\n\n\nfizz buzzer problem quiz started\n\n")

    n = int(input("\n\nany integer for the quiz. it should be divisible or not divisible by 5 or 3\n\n-> "))
    n_dby_3 = n%3
    n_dby_5 = n%5

    if (n_dby_3 == 0 and n_dby_5 == 0):
        print("\n\nFizzBuzz\n\n")

    elif (n_dby_3 == 0 and n_dby_5 != 0):
        print("\n\nFizz\n\n")

    elif (n_dby_3 != 0 and n_dby_5 == 0):
        print("\n\nBuzz\n\n")

    else:
        n = str(n)
        print(f"\n\nthe number is not divisible by 3 and 5\n\n")
        print(n,type(n),"\n\n\n")
