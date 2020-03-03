import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        took = round(time.time() - start, 3)
        print(f'function {func.__name__} exclude in {took} sec')
        return res
    return inner


@timeit
def say_hello(name):
    time.sleep(1)
    print('Hello ' + name)


say_hello('Yuliia')
