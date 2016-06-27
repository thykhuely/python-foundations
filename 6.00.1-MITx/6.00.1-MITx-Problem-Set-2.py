# -*- coding: utf-8 -*-
'''
PAYING OFF CREDIT CARD DEBT

Each month, a credit card statement will come with the option for you to pay a minimum amount of your charge, usually 2% of the balance due. However, the credit card company earns money by charging interest on the balance that you don't pay. So even if you pay credit card payments on time, interest is still accruing on the outstanding balance.

Say you've made a $5,000 purchase on a credit card with an 18% annual interest rate and a 2% minimum monthly payment rate. If you only pay the minimum monthly amount for a year, how much is the remaining balance?

You can think about this in the following way.

At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount we will call b0 (b for balance; subscript 0 to indicate this is the balance at month 0).

Any payment you make during that month is deducted from the balance. Let's call the payment you make in month 0, p0. Thus, your unpaid balance for month 0, ub0, is equal to b0−p0.

ub0=b0−p0

At the beginning of month 1, the credit card company will charge you interest on your unpaid balance. So if your annual interest rate is r, then at the beginning of month 1, your new balance is your previous unpaid balance ub0, plus the interest on this unpaid balance for the month. In algebra, this new balance would be

b1=ub0+r12.0⋅ub0

In month 1, we will make another payment, p1. That payment has to cover some of the interest costs, so it does not completely go towards paying off the original charge. The balance at the beginning of month 2, b2, can be calculated by first calculating the unpaid balance after paying p1, then by adding the interest accrued:

ub1=b1−p1
b2=ub1+r12.0⋅ub1

If you choose just to pay off the minimum monthly payment each month, you will see that the compound interest will dramatically reduce your ability to lower your debt.


''' 

# Problem 1: Paying the Minimum 

# Write a program that calculate the credit card balance if a person only pays a min monthly payment required each month
# balance = the outstanding balance on credit card, rounded to 2 decimal place
# annualInterestRate = annual interest rate as a decimal
# monthlyPaymentRate = min monthly payment rate as a decimal

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


monthlyInterestRate = annualInterestRate / 12

i = 1
numberMonth = 12
totalPaid = 0

while i <= numberMonth:
    
    #Calculate monthly balance
    min_payment = monthlyPaymentRate * balance
    unpaid_balance = balance - min_payment
    balance = unpaid_balance * (monthlyInterestRate + 1)
    print('Month: '+ str(i) + '\n' 
    + 'Minimum monthly payment: ' + str(round(min_payment,2)) + '\n'
    + str('Remaining Balance: ' + str(round(balance,2))))

    #Accumulate total payment
    totalPaid += min_payment
    
    i = i + 1
    
    #EOY balance result
    if i > 12: 
        print('Total paid: '+ str(round(totalPaid,2)) +  '\n' + 'Remaining Balance: ' + str(round(balance,2)))

# Problem 2
# Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). 
# The monthly payment must be a multiple of $10 and is the same for all months.
# balance = the outstanding balance on credit card, rounded to 2 decimal place
# annualInterestRate = annual interest rate as a decimal

balance = 4773
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12

numberMonth = 12
EOY_remaining_balance = 0

i = 0
j = 1
original_balance = balance

while EOY_remaining_balance >= 0:  
    
    balance = original_balance
    
    for i in range (1, 13):
            min_payment = 10 * j 
            unpaid_balance = balance - min_payment
            balance = unpaid_balance * (monthlyInterestRate + 1)
            i = i + 1
        
            EOY_remaining_balance = balance
            
    j = j + 1

print('Lowest Payment: ' + str(min_payment))

# Problem 3: Using Bisection Search to Make the Program Faster
# Monthlt payment lower bound: Balance / 12
# Monthly payment upper bound: (Balance x (1 + Monthly interest rate)^12) / 12.0

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12

EOY_remaining_balance = 0
epsilon = 0.1

original_balance = balance
low = balance / 12
high = (balance * ((1 + monthlyInterestRate)**12)) / 12.0

min_payment = round((high+low) /2, 2)

while True:  
    
    balance = original_balance
    
    # Calculating each month balance for a year
    for i in range (1, 13): 
            unpaid_balance = balance - min_payment
            balance = unpaid_balance * (monthlyInterestRate + 1)
            EOY_remaining_balance = balance
    
    # If the EOY balanceis close to zero, break the loop
    if abs(EOY_remaining_balance - 0) < epsilon: 
        print('Lowest Payment: ' + str(round(min_payment,2)))
        break
    
    # If the balance is more than zero, i.e. min_payment is too low
    elif EOY_remaining_balance > 0:
        low = min_payment
    
    # If the balance is less than zero, i.e. min_payment is too high
    elif EOY_remaining_balance < 0:
        high =  min_payment
        
    # Update new fixed min payment    
    min_payment = (high+low) / 2
