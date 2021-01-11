
def fibonacci():
    '''Generate Fibonacci number sequentially.'''
    a, b    = 0, 1
    while True:
        yield a
        a, b    = b, a+b
fibonacci   = fibonacci()
