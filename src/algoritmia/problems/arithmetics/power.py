#coding: latin1

#< power1
def power1(a, n):
    if n == 0: 
        return 1
    elif n == 1: 
        return a
    elif n % 2 == 0: 
        return power1(a, n//2) * power1(a, n//2)
    else: 
        return power1(a, n//2) * power1(a, n//2+1)
#> power1

#< power
def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        return power(a, n//2)**2
    else:
        return a * power(a, n//2)**2
#> power