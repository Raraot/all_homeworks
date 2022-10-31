from multiprocessing import Pool
from time import time


def factorize(*number):
    all_result = []
    for x1 in number:
        result = []
        for i in range(1, x1+1):
            if x1 % i == 0:
                result.append(i)
        all_result.append(result)
    return all_result


if __name__ == '__main__':
    my_tuple = (21302128, 26627657, 53255309, 106510600)

    # Testing line version
    start_time = time()
    factorize(*my_tuple)
    end_time = time()
    print(f'\nLine version time: {end_time - start_time}')

    # Testing processing (Pool) version
    start_time = time()
    with Pool(processes=4) as pool: 
        pool.map(factorize, my_tuple)
    end_time = time()
    print(f'\nProcessing (Pool) version time: {end_time - start_time}\n')




a, b, c, d  = factorize(128, 255, 99999, 10651060)


assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


# python3 main.py