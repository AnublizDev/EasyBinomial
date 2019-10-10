def fact(n):

    if n == 0:
        return 1
  
    return n * fact(n - 1)

def binom(n, k):
  
    return fact(n) / (fact(k) * fact(n - k))

def decorate_output(text):
    print('==============================')
    print('Your binomail is', int(text))
    print('==============================')

decorate_output(binom(int(input('Enter your 1st number : ')), int(input('Enter your 2nd number : '))))