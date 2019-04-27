payment = float(input('Enter your payment:\n'))
age = int(input('Enter your age:\n'))
tax = 0

if payment < 10000:
    print('no tax')

elif (payment >= 10000) and (payment <= 20000):
    tax = payment * 5/100
    print(tax)