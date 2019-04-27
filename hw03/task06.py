s = float(input('Enter a number:\n'))

if s<100:
    l = 3000 - (125 * (s*s))
    print(l)
elif s>=100:
    l = 12000/ 4 + ((s*s) / 14900)
    print(l)