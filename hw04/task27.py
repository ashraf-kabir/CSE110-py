def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status

for n in range(1,1000):
    if is_prime(n):
        print(int(n), sep='', end=', ', flush=True)