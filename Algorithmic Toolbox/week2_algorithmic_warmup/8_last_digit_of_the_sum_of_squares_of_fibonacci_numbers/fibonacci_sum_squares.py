def fibonacci_sum_squares(n):
    pisano_period = 60

    fib_last_digits = [0, 1]
    for i in range(2, pisano_period):
        fib_last_digits.append((fib_last_digits[-1] + fib_last_digits[-2]) % 10)

    def get_fib_last_digit(x):
        return fib_last_digits[x % pisano_period]

    last_digit_fn = get_fib_last_digit(n)
    last_digit_fn_plus_1 = get_fib_last_digit(n + 1)

    return (last_digit_fn * last_digit_fn_plus_1) % 10




if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
