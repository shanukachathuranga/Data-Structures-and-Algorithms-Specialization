from sys import stdin
def partition3(values):
    total_sum = sum(values)

    if total_sum % 3 != 0:
        return 0

    target = total_sum // 3
    n = len(values)

    dp = [[[False for _ in range(n + 1)] for _ in range(target + 1)] for _ in range(target + 1)]

    dp[0][0][0] = True

    for k in range(1, n + 1):
        for i in range(target + 1):
            for j in range(target + 1):
                dp[i][j][k] = dp[i][j][k - 1]

                if i >= values[k - 1]:
                    dp[i][j][k] |= dp[i - values[k - 1]][j][k - 1]

                if j >= values[k - 1]:
                    dp[i][j][k] |= dp[i][j - values[k - 1]][k - 1]

    return 1 if dp[target][target][n] else 0

if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
