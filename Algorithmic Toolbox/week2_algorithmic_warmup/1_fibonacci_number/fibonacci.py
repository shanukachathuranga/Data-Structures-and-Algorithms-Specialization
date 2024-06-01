# def fibonacci_number(n):
#     if n <= 1:
#         return n
#
#     return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_number(n):
    if n<= 1:
        return n
    else:
        first_number = 0
        second_number = 1
        fib_number = 0;
        for i in range(2, n+1):
            fib_number = first_number + second_number
            first_number = second_number
            second_number = fib_number

        return fib_number


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
