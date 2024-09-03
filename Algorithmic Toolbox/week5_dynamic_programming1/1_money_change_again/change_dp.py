def change(money):
    denominations = [1, 3, 4]

    dp = [float('inf')] * (money + 1)

    dp[0] = 0

    for i in range(1, money + 1):
        for coin in denominations:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[money]



if __name__ == '__main__':
    m = int(input())
    print(change(m))
