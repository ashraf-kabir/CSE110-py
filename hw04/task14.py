r = int(input('Enter the range:\n'))
if (r <= 0):
    print('Try again')
    exit()
else:
    product = 1
    for i in range(1, r+1):
        x = float(input('Enter number:\n'))
        product = product * x
    print('The product is '+str(product))
