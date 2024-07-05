''''
Problem Statement: Credit Card Eligibility Checker
Create a Python program to determine the eligibility of an individual for different 
types of credit cards based on their personal and financial information. The program 
should evaluate the eligibility for a "premium credit card" and a "basic credit card" 
based on the following criteria:

Employment Status:
The individual must be "employed" to be considered for a premium credit card.

Income:
For a premium credit card, the individual must have an annual income of at least $50,000.

For a basic credit card (if the individual is not employed), the individual must have an annual income of at least $30,000.
Age:

For a premium credit card, the individual must be at least 25 years old.
Credit Score:

For a premium credit card, the individual must have a credit score of at least 650.
For a basic credit card (if the individual is not employed), the individual must have a credit score of at least 600.
Input:
income: Annual income of the individual (an integer).
age: Age of the individual (an integer).
credit_score: Credit score of the individual (an integer).
employment_status: Employment status of the individual (a string, e.g., "employed" or "unemployed").
Output:
Print an appropriate message indicating the type of credit card the individual is eligible for or stating that they do not meet the eligibility criteria for any credit card.
Example:
Given the following inputs:

income = 75000
age = 28
credit_score = 700
employment_status = "employed"
The output should be:
You are eligible for the premium credit card.

Steps:
Check if the individual is employed.
If employed, check if their income is at least $50,000.
If the income condition is satisfied, check if their age is at least 25.
If the age condition is satisfied, check if their credit score is at least 650.
If any of these conditions fail, print appropriate messages.
If the individual is not employed, check if their income is at least $30,000 and their credit score is at least 600.
Print the appropriate message based on the evaluations.
This program helps individuals understand which type of credit card they are eligible for based on their financial and personal information.

'''

employment_status =input("Are you employed ? Y or N")
income=int(input("Enter your income:"))
age=int(input("Enter your age:"))
credit_score=int(input("Enter your credit score:"))
if employment_status == "Y":
    if income >= 50000:
        if age >= 25:
            if credit_score >= 650:
                print("You are eligible for the premium credit card.")
            else:
                print("Your credit score is too low for the premium credit card.")
        else:
            print("You are not old enough for the premium credit card.")
    else:
        print("Your income is too low for the premium credit card.")
else:
    if income >= 30000 and credit_score >= 600:
        print("You may be eligible for a basic credit card.")
    else:
        print("You do not meet the eligibility criteria for a credit card.")