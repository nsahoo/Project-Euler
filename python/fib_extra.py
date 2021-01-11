
# not finished 
# function for nth Fibonacci number
fibArr = [0,1]

def fib(n):
    a, b = 0, 1
    if n<=0:
        print("incorrect input")
    elif n==1:
        return a
    else:
        for i in range(2,n):
            a, b = b, a+b
        fibArr.append(b)    
        return b

for x in range(1,20):
    print("#{}: \t {} \t {}".format(x, fib(x), fibArr))


### fibonacci numbers in series [ first n fib numbers ]
def fibRange(n): 
    fibs= [0,1] 
    for i in range(2, n):
        fibs.append(fibs[-1]+fibs[-2])
    print(max(fibs))
    return fibs

print(fibRange(100))
