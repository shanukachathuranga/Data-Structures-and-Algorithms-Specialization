import random

# def fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % m

def fibonacci(n,m):
    if n <= 1:
        return n%m

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def pisano_period(m):
    previous, current = 0, 1
    for i in range(m*m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            # print(i+1)
            return i+1

def fibonacci_huge(n, m):
    return fibonacci((n%pisano_period(m)),m)

# def test():
#     while True:
#         n,m = random.randint(1,100),random.randint(2,100)
#         print(n,m)
#         a,b = fibonacci_huge(n,m), fibonacci_huge_naive(n,m)
#         if a != b:
#             print(f"[{n},{m}] --> {a} != {b}")
#             break
#         else:
#             print(f"[{n},{m}] --> {a} == {b}")
# test()

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
