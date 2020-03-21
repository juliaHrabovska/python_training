"""
These are different solutions of "Task 5: Multiples of 3 and 5. Find the best algorithm"

Let's find out which of the proposed algorithms is the most effective
"""
import logging
import multiprocessing
import time

logging.basicConfig(level=logging.INFO)


class timer:

    def __init__(self, name):
        self.name = name
        self._start = None

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        duration = round(end - self._start, 2)
        logging.info(f"'{self.name}' -> {duration} sec")


N = 300000000


def simple_iteration():
    res = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


def several_for_loops():
    res = 0
    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    return res


def iterate_over_fifteen():
    range_diff = [0, 3, 5, 6, 9, 10, 12]
    res = 0
    for i in range(0, N, 15):
        for d in range_diff:
            v = i + d
            if v >= N:
                break
            res += v
    return res


def math_formula():
    upper = N - 1
    threes = int(3 * (upper / 3) * ((upper / 3) + 1) / 2)
    fives = int(5 * (upper / 5) * ((upper / 5) + 1) / 2)
    fifteens = int(15 * (upper / 15) * ((upper / 15) + 1) / 2)
    res = threes + fives - fifteens
    return res


def run_all_calculations_in_parallel():
    # Use multiprocessing library to run all above functions in parallel
    # Print execution time of each function
    proc_dict = {
        "simple_iteration": multiprocessing.Process(target=simple_iteration),
        "several_for_loops": multiprocessing.Process(target=several_for_loops),
        "iterate_over_fifteen": multiprocessing.Process(target=iterate_over_fifteen),
        "math_formula": multiprocessing.Process(target=math_formula)
    }

    for key, value in proc_dict.items():
        with timer(key):
            value.start()
            value.join()


if __name__ == '__main__':
    run_all_calculations_in_parallel()
