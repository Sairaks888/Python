def fib_generator():
    a = 1
    b = 2
    def next_fib():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return result
    return next_fib
fib = fib_generator()
print(fib())  
print(fib())  
print(fib())  
print(fib())  
print(fib())  
print(fib())  
print(fib()) 