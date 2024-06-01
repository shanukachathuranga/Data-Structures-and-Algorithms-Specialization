import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# def lcmBasic(a, b):
#     for l in range(1, a * b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#
#     assert False


def lcm(a, b):
    return (a * b) // gcd(a, b)


# def test():
#     while True:
#         a, b = random.randint(1, 100000), random.randint(1, 100000)
#         print(a, b)
#         c = lcmBasic(a, b)
#         print(c)
#         d = lcm(b, a)
#         if c != d:
#             print(f"[{a},{b}] --> {c} != {d}]")
#             break
#
#         print(f"[{a},{b}] --> {c} = {d}")
#

# test()

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
