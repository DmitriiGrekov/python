cache = {}
#from functools import lru_cache
#def fib2(n):
#
#    if n not in cache:
#        cache[n] = n if n<=1 else  fib2(n-1)+fib2(n-2) 
#    return cache[n]
#
#def fib1(n):
#    if n<=1:
#        return 1
#    else:
#        return fib1(n-1)+fib1(n-2)
##
#def memo(f):
#    cache = {}
#    def inner(n):
#        if n not in cache:
#            cache[n]=f(n)
#        return cache[n]
#    return inner
#
#
#
#
#fibs = memo(fib1)

#Лучший алгоритм
def fib3(n):

    f0,f1=0,1
    for i in range(n-1):
        f0,f1=f1,f0+f1
    return f1

print(fib3(800))
#Функция для вычисления времени
import time
def timed(f,*args,n_iter = 100):
    acc = float('inf')
    for i in range(n_iter):
        t0=time.perf_counter()
        f(*args)
        t1= time.perf_counter()
        acc = min(acc,t1-t0)
    return acc



print(timed(fib3,800))


