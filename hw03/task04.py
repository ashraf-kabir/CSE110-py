payment = float(input('Enter your payment:\n'))
age = int(input('Enter your age:\n'))
tax = 0

if (age < 18):
    print('no tax')

elif (age >=18):
    if (payment <10000):
        print('no tax')
    elif (payment >= 10000) and (payment <= 20000):
        tax = payment * 5/100
        print(tax)
    elif (payment > 20000):
        tax = payment * 10/100