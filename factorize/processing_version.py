
# from ast import main
from time import time


def factorize(*number):
    start_time = time()
    all_result = []
    for x1 in number:
        result = []
        for i in range(1, x1+1):
            if x1 % i == 0:
                result.append(i)
        all_result.append(result)
    end_time = time()
    print(end_time - start_time)
    return all_result

    # raise NotImplementedError()

# a = factorize(128)
a, b, c, d  = factorize(128, 255, 99999, 10651060)


assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]






# принимает список чисел и возвращает список чисел, 
# на которые числа из входного списка делятся без остатка.

# Реализуйте синхронную версию и измерьте время выполнения.

# Потом улучшите производительность вашей функции, 
# реализовав использование нескольких ядер процессора для 
# параллельных вычислений, и замерьте время выполнения опять.

# python3 main.py