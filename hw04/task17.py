nterms = 10
a = 0
b = 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(a)
else:
   print("Fibonacci sequence upto",nterms,":")
   while (count < nterms):
       print(a, end=', ')
       nth = a + b
       a = b
       b = nth
       count += 1