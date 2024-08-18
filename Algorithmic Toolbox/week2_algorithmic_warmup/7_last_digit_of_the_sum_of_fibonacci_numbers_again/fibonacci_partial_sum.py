# Uses python3
import sys

def fibonacci_partial_sum_naive(m, n):
    pisano_period = 60

    fib_last_digits = [0, 1]
    for i in range(2, pisano_period):
        fib_last_digits.append((fib_last_digits[-1] + fib_last_digits[-2]) % 10)

    def fibonacci_sum_last_digit(x):
        x = (x + 2) % pisano_period
        if x == 0:
            return 9
        return (fib_last_digits[x] - 1) % 10

    last_digit_sum_n = fibonacci_sum_last_digit(n)
    last_digit_sum_m_minus_1 = fibonacci_sum_last_digit(m - 1)

    return (last_digit_sum_n - last_digit_sum_m_minus_1) % 10




if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
