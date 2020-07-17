n = int(input('Enter your number n = '))
factorial = 1
if n==0:
    factorial
else:
    for i in range(1,n+1):
        factorial = factorial*i
print('factorial of', n,'=', factorial)