def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized


def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

fib = count(fib)
counted_fib = fib
fib = memo(fib)
fib = count(fib)

print(fib(30))
print(fib.call_count)
print(counted_fib.call_count)
