# def gcd(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d
#
#     return current_gcd

def gcd(a,b):
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

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
