def sum(a,b):
    return a+b

def difference(a,b):
    return a-b

def product(a,b):
    return a*b

def division(a,b):
    return a/b

def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print("Not Prime Number")
                break
        else:
            print("Prime Number")
    else:
        print("Not Prime Number")

def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        fact= fact*i
    return fact