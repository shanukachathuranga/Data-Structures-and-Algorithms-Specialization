import random

# def fibonacci_sum_basic(n):
#     if n <= 1:
#         return n
#
#     previous, current, _sum = 0, 1, 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         _sum += current
#
#     return _sum % 10

def fibonacci_sum_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current%10, (previous + current)%10
        sum += current

    return sum % 10

# def test():
#     while True:
#         n = random.randint(1,10000)
#         print(n)
#         a,b = fibonacci_sum(n), fibonacci_sum_basic(n)
#         if a != b:
#             print(f"[{n}] --> {a} != {b}")
#             break
#         else:
#             print(f"[{n}] --> {a} == {b}")
# test()

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_last_digit(n))
