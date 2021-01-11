

import itertools as it
from itertools import takewhile
from fibo import fibonacci
def fib():
	a = 0
	b = 1
	while True:
		yield b
		a, b = b, a+b


result = sum(filter(lambda y: y%2==0, it.takewhile(lambda x: x<=4e6, fib())))
print(result)                

result2 = sum(e for e in (takewhile(lambda x: x<4*10**6, fibonacci)) if e%2==0)
print(result2)
