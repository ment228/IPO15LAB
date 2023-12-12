import time#импорт библиотеки time
from functools import wraps#импорт wraps из библиотеки functools
def timeit(method):#функция timeit
    @wraps(method)#декоратор wraps
    def timed(*args, **kw):#функция timed
        ts = time.monotonic()
        result = method(*args, **kw)
        te = time.monotonic()
        ms = (te - ts) * 1000
        all_args = ', '.join(tuple(f'{a!r}' for a in args)
                             + tuple(f'{k}={v!r}' for k, v in kw.items()))
        print(f'{method.__name__}({all_args}): {ms:2.2f} ms')
        return result
    return timed
# использование:
@timeit
def slow_func(x, y, sleep):
    time.sleep(sleep)
    return x + y
slow_func(10, 20, sleep=2)#принимает в себя аргументы и выводит скорость
