
# Multiples of 3 and 5

_sum = 0
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        print(x)
        _sum +=x

# one-liner        
_sum2 = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
        
print(_sum)
print(_sum2)

