def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)
    
print(f(7))

""" Print fib numbers in the sequence """

num = 7

def f2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f2(n-1) + f2(n-2)

values = [str(f2(x)) for x in range(num+1)]
print(','.join(values))

