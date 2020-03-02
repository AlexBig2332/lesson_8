import time
import os
import psutil

def show_time(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        print('Исп. память до вып. функции:' + str(proc.memory_info().rss / 1000000))
        start = time.time()
        f(*args, **kwargs)
        print('Исп. память после вып. функции:' + str(proc.memory_info().rss / 1000000))
        stop = time.time()
        print("Выполнение {} заняло {:.5} секунд".format(f, stop - start))
        print()
    return wrapper

@show_time
def list_create_gen(N):
    for i in range(N):
         yield (i)

@show_time
def list_create_gen_sequence(N): # Создание списка генератором последовательностей
    list_gen = [i for i in range(1, N+1)]
    return list_gen

@show_time
def list_create(N): # Создание списка в цикле
    list = []
    for i in range(N):
        list.append(i+1)
    return list

N = 1000000
list_create_gen(N)
list_create_gen_sequence(N)
list_create(N)

