"""THIS IS A PROGRAM TO CALCULATE AMOUNT TO BE RECEIVED FROM COVID-19 STIMULUS"""
def min_refund(kids):
    return kids * 500
def med_refund(n, income, kids):
    child_amount = kids * 500
    if n == 's':
        return round(amountByMaritalStatus['single'] - (((income - 75000) / 100)*5) + child_amount)

    else:
        return round(amountByMaritalStatus['married'] - (((income - 150000) / 100)*5) + child_amount)


def max_refund(n,kids):
    child_amount = kids * 500
    if n == 's':
        return amountByMaritalStatus['single'] + child_amount

    else:
        return amountByMaritalStatus['married'] + child_amount


def get_status():
    if (n == 's' and income > 99000) or (n == 'm' and income > 198000):
        print(f'Your stimulus refund is', min_refund(kids))

    elif (n == 's' and income > 75000) or (n == 'm' and income > 150000):
        print(f'Your stimulus refund is', med_refund(n, income, kids))

    else:
        print(f'Your refund is', max_refund(n, kids))


if __name__ == '__main__':
    amountByMaritalStatus = {'single': 1200, 'married': 2400}

    while True:
        n = input('Enter Your Filing Status. S for single, Head of Household or Married filing Separate and \
M for married: ').lower()

        if n not in ('s', 'm'):
            print('Please enter S or M')
            continue
        try:
            income = int(input('Enter your 2019 Federal Income: '))
        except ValueError:
            print('Please enter a number')
            continue
        try:
            kids = int(input('Enter the number of dependents under 17: '))
        except ValueError:
            print('Please enter a number')
            continue
        get_status()
        break
