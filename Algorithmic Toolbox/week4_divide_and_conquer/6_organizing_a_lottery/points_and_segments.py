from sys import stdin
import bisect
# import random
# import time

# def points_cover_naive(starts, ends, points):
#     assert len(starts) == len(ends)
#     count = [0] * len(points)
#
#     for index, point in enumerate(points):
#         for start, end in zip(starts, ends):
#             if start <= point <= end:
#                 count[index] += 1
#
#     return count


def points_cover(starts, ends, points):
    starts.sort()
    ends.sort()

    results = []

    for p in points:
        startsCount = bisect.bisect_right(starts, p)
        endsCount = bisect.bisect_left(ends, p)
        results.append(startsCount - endsCount)

    return results


# def bisect(array, point):
#     left = 0
#     right = len(array)
#
#     while left < right:
#         mid = (left + right) // 2
#         if array[mid] > point:
#             right = mid
#         else:
#             left = mid + 1
#
#     return left


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)



# def generate_test_data(num_segments, num_points, max_value):
#     starts = [random.randint(0, max_value) for _ in range(num_segments)]
#     ends = [random.randint(start, max_value) for start in starts]
#     points = [random.randint(0, max_value) for _ in range(num_points)]
#     return starts, ends, points
#
#
# def stress_test(num_tests, num_segments, num_points, max_value):
#     for _ in range(num_tests):
#         starts, ends, points = generate_test_data(num_segments, num_points, max_value)
#
#         start_time = time.time()
#         result_naive = points_cover_naive(starts, ends, points)
#         naive_time = time.time() - start_time
#
#         start_time = time.time()
#         result_efficient = points_cover(starts, ends, points)
#         efficient_time = time.time() - start_time
#
#         assert result_naive == result_efficient, f"Mismatch found! naive: {result_naive} ---- advance: {result_efficient}"
#
#         print(f"Test passed. Naive time: {naive_time:.4f}s, Efficient time: {efficient_time:.4f}s")
#
#
# if __name__ == '__main__':
#     num_tests = 10
#     num_segments = 1000
#     num_points = 1000
#     max_value = 10000
#
#     stress_test(num_tests, num_segments, num_points, max_value)
