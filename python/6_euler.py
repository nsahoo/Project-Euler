

def diff_sq(n):
    result1 = sum(x**2 for x in range(1,n+1))
    result2 = sum(x for x in range(1,n+1))**2
    return (abs(result1-result2))


print(diff_sq(10))
print(diff_sq(100))
