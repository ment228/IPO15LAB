import time #импорт time
from functools import wraps#импорт wraps из functools
import random#импорт рандома
def timeit(method):#функция timeit
    @wraps(method)#декоратор wraps
    def timeit(*args, **kw):#функция timed
        ts = time.monotonic()#
        res = method(*args, **kw)#
        te = time.monotonic()#
        ms = (te - ts) * 1000#
        return res, ms#
    return timeit#
@timeit#декоратор timeit
def elements(arr):#функция elements
    n = len(arr)#n присваюваем длину массива
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]#сортировка обменом по убыванию
    return arr#возвращаем arr
sizes = [10, 100, 1000, 10000]#присваиваем sizes список из таблицы
print("\ номер | Кол-во элементов | Отсортированный список | Время выполнения (ms) /")#вывод таблицы
for i, size in enumerate(sizes, 1):
    arr = [random.randint(0, 100) for _ in range(size)]  #создаем список в момент вызова функции
    res, timing = elements(arr)
    print(f"| {i} | {size} | {res} | {timing:.2f} |")#вывод результата