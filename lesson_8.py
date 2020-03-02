# 1. Написать декоратор, замеряющий время выполнение декорируемой функции.
# 2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000
#    (создание объектов оформить в виде функций).

import time

def show_time(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        finish = time.time()
        print("Создание списка {} заняло {:.5} секунд".format(f, finish - start))
    return wrapper

@show_time
def list_create_gen(N):
    list_gen = [i for i in range(1, N+1)]
    return list_gen

@show_time
def list_create(N):
    list = []
    for i in range(N):
        list.append(i+1)
    return list

list_create_gen(1000000)
list_create(1000000)

