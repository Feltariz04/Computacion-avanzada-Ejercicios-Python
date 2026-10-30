import math
import functools as ft



def count_calls(func):

    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1

        resultado = func(*args, **kwargs)
        return resultado

    wrapper.calls = 0

    return wrapper


@count_calls
def fib_rec(n):
    
    if n < 2:
        return n

    return fib_rec(n - 1) + fib_rec(n - 2)

@count_calls
@ft.lru_cache(maxsize=None)
def fib_cache(n):
   
    if n < 2:
        return n

    return fib_cache(n - 1) + fib_cache(n - 2)

@ft.lru_cache(maxsize=None)
@count_calls
def fib_cache_invertido(n):
   
    if n < 2:
        return n

    return fib_cache_invertido(n - 1) + fib_cache_invertido(n - 2)



# Prueba
n = 10
fib_rec.calls = 0

print("\nSin caché:")
print("Fibonacci:", fib_rec(n))
print("Llamadas:", fib_rec.calls)


fib_cache.calls = 0
fib_cache.__wrapped__.cache_clear()

print("\nCon caché:")
print("Fibonacci:", fib_cache(n))
print("Llamadas:", fib_cache.calls)

fib_cache_invertido.calls = 0


print("\nCon caché invertido:")
print("Fibonacci:", fib_cache_invertido(n))
print("Llamadas:",fib_cache_invertido.__wrapped__.calls)