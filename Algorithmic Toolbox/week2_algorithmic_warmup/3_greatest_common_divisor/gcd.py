import random
def gcdBasic(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

# def gcd(a,b):
#     firstNumber = a
#     secondNumber = b
#
#     while firstNumber != 0 and secondNumber != 0:
#         if firstNumber > secondNumber:
#             firstNumber = firstNumber % secondNumber
#         elif secondNumber > firstNumber:
#             secondNumber = secondNumber % firstNumber
#     if firstNumber == 0:
#         return secondNumber
#     elif secondNumber == 0:
#         return firstNumber
#     else:
#         return 0

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def test():
    while True:
        a,b = random.randint(1,100000),random.randint(1,100000)
        c = gcd(a, b)
        d = gcdBasic(b, a)
        if c != d:
            print(f"[{a},{b}] --> {c} != {d}")
            break
        print(f"[{a},{b}] --> {c} = {d}")

test()

# if __name__ == "__main__":
#     a, b = map(int, input().split())
#     print(gcd(a, b))
