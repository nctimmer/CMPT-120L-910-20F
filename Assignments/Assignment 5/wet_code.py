# We're looking to find out how much money we have after a day with friends on Saturday. 
# Our code does the trick but we learned about keeping out code DRY recently and want to make it more efficent by making it DRY.
# I want you to accomplish this by making functions where you see repeated code. 
# Some things to note. When we have a positive number that gets split up and 85% goes into checking and 15% goes into savings. 
# All negative numbers gets taken out of the checking account.

# checking += transations[1]
#LOOKING FOR: CHECKING $2007.44, SAVINGS $1456.20!!!
def saturdays_bank_transactions(transations) -> (float, float):
    savings = 1096.25
    checking = 1590.80

    CHECKING_PERCENT = float(0.85)
    SAVINGS_PERCENT = float(0.15)

    checking += (transations[0] * CHECKING_PERCENT)
    savings += (transations[0] * SAVINGS_PERCENT)
    
    for i in range(1,4):
        checking += transations[i]

    checking += (transations[4] * CHECKING_PERCENT)
    savings += (transations[4] * SAVINGS_PERCENT)
    
    checking += (transations[5] * CHECKING_PERCENT)
    savings += (transations[5] * SAVINGS_PERCENT)

    for i in range(6,11):
        checking += transations[i]

    return checking, savings

if __name__ == "__main__":
    transations = [300.00, -50.00, -5.00, -20, 15.72, 2083.93, -1034.00, -420.00, -5.23, -15.93, -72.90]
    new_balance = saturdays_bank_transactions(transations)
    print("Your new checking balance is:", '${:.2f}'.format(round(new_balance[0], 2)), "\n", "Your new savings balance is:", '${:.2f}'.format(round(new_balance[1], 2)))