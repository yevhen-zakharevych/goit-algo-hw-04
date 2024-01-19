import timeit
import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort

if __name__ == '__main__':
    data_small = [random.randint(0, 100) for _ in range(100)]
    data_medium = [random.randint(0, 1_000) for _ in range(1_000)]
    data_large = [random.randint(0, 10_000) for _ in range(10_000)]

    time_small_insertion = timeit.timeit(lambda: insertion_sort(data_small[:]), number=10)
    time_medium_insertion = timeit.timeit(lambda: insertion_sort(data_medium[:]), number=10)
    time_large_insertion = timeit.timeit(lambda: insertion_sort(data_large[:]), number=10)

    time_small_merge = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium[:]), number=10)
    time_large_merge = timeit.timeit(lambda: merge_sort(data_large[:]), number=10)

    time_small_sort = timeit.timeit(lambda: data_small[:].sort(), number=10)
    time_medium_sort = timeit.timeit(lambda: data_medium[:].sort(), number=10)
    time_large_sort = timeit.timeit(lambda: data_large[:].sort(), number=10)

    time_small_sorted = timeit.timeit(lambda: sorted(data_small[:]), number=10)
    time_medium_sorted = timeit.timeit(lambda: sorted(data_medium[:]), number=10)
    time_large_sorted = timeit.timeit(lambda: sorted(data_large[:]), number=10)

    print(f"{'| Algorithm': <20} | {'Time for small data 100': <30} | {'Time for medium data 1k': <30} | {'Time for large data 10k': <30}")
    print(f"{'-' * 20} | {'-' * 30} | {'-' * 30} | {'-' * 30}")
    print(f"{'| Insertion sort': <20} | {time_small_insertion:<30.5f} | {time_medium_insertion:<30.5f} | {time_large_insertion:<30.5f}")
    print(f"{'| Merge sort': <20} | {time_small_merge:<30.5f} | {time_medium_merge:<30.5f} | {time_large_merge:<30.5f}")
    print(f"{'| Sort': <20} | {time_small_sort:<30.5f} | {time_medium_sort:<30.5f} | {time_large_sort:<30.5f}")
    print(f"{'| Sorted': <20} | {time_small_sorted:<30.5f} | {time_medium_sorted:<30.5f} | {time_large_sorted:<30.5f}")
