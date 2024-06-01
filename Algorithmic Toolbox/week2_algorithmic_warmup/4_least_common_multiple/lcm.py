import random


def gcd(a, b):
    firstNumber = a
    secondNumber = b

    while firstNumber != 0 and secondNumber != 0:
        if firstNumber > secondNumber:
            firstNumber = firstNumber % secondNumber
        elif secondNumber > firstNumber:
            secondNumber = secondNumber % firstNumber
    if firstNumber == 0:
        return secondNumber
    elif secondNumber == 0:
        return firstNumber
    else:
        return 0


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
