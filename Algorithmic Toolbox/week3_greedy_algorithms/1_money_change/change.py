def change(money):
    changes = [10,5,1]
    coin_count = 0

    for coin in changes:
        coin_count += money // coin
        money %= coin

    return coin_count


if __name__ == '__main__':
    m = int(input())
    print(change(m))
