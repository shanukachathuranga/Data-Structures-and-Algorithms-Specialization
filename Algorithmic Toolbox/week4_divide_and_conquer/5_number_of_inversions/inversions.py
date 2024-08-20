from itertools import combinations
import random
import time

def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def inversion_advance(a):
    array, count = merge_sort(a)

    return count


def merge_sort(a):
    if len(a) <= 1:
        return a, 0

    middle = len(a) // 2
    l, leftCount = merge_sort(a[:middle])
    r, rightCount = merge_sort(a[middle:])

    sortedArr, mergeCount = merge(l, r)

    return sortedArr, (leftCount + rightCount + mergeCount)


def merge(left, right):
    d = []
    i = 0
    j = 0
    count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            d.append(left[i])
            i += 1
        else:
            d.append(right[j])
            count += len(left) - i
            j += 1

    d.extend(left[i:])
    d.extend(right[j:])

    return d, count


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversion_advance(elements))

# def generate_random_array(size, max_value):
#     return [random.randint(0, max_value) for _ in range(size)]
#
#
# def stress_test(iterations, max_size, max_value):
#     for i in range(iterations):
#         size = random.randint(1, max_size)
#         array = generate_random_array(size, max_value)
#
#         start_time = time.time()
#         naive_result = inversions_naive(array)
#         naive_time = time.time() - start_time
#
#         start_time = time.time()
#         advanced_result = inversion_advance(array)
#         advanced_time = time.time() - start_time
#
#         assert naive_result == advanced_result, f"Mismatch found: naive={naive_result}, advanced={advanced_result}"
#
#         print(f"Iteration {i + 1}: Size={size}, Naive Time={naive_time:.6f}s, Advanced Time={advanced_time:.6f}s")
#
#
# if __name__ == '__main__':
#     stress_test(iterations=1000, max_size=10000, max_value=1000000)


