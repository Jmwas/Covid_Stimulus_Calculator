"""THIS IS A PROGRAM TO CALCULATE AMOUNT TO BE RECEIEVED FROM COVID-19 STIMULUS"""


def min_refund(*args):
    print(childAmount)
    return


def med_refund(*args):
    if n == 's':
        print(round(singleAmount - ((income - 75000) / 100) + childAmount))

    else:
        print(round(marriedAmount - ((income - 150000) / 100) + childAmount))


def max_refund(*args):
    if n == 's':
        print(singleAmount + childAmount)

    else:
        print(marriedAmount + childAmount)


n = input('Enter Your Filing Status. S for single, Head of Household or Married filing Separate and  M for married: ').lower()
income = int(input('Enter your 2018 Federal Income: '))
kids = int(input('Enter the number of dependents under 17: '))

singleAmount = 1200
marriedAmount = 2400
childAmount = 500 * kids


if (n == 's' and income > 99000) or (n == 'm' and income > 198000):
    min_refund()

elif (n == 's' and income > 75000) or (n == 'm' and income > 150000):
    med_refund()

else:
    max_refund()