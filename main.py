import timeit


def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]

    dp = {0: (0, [])}

    for i in range(1, amount + 1):
        min_coins = float('inf')
        used_coins = []
        for coin in coins:
            if i - coin >= 0 and i - coin in dp:
                current_min_coins = dp[i - coin][0] + 1
                if current_min_coins < min_coins:
                    min_coins = current_min_coins
                    used_coins = dp[i - coin][1] + [coin]
        if min_coins < float('inf'):
            dp[i] = (min_coins, used_coins)

    if amount not in dp:
        return {}

    result = {}
    for coin in dp[amount][1]:
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1

    return result


if __name__ == '__main__':

    find_coins_greedy_time = timeit.timeit(lambda: find_coins_greedy(113), number=10000)
    print(find_coins_greedy(113), find_coins_greedy_time)  # Output: {50: 2, 10: 1, 2: 1, 1: 1} 0.006542875000377535

    find_min_coins_time = timeit.timeit(lambda: find_min_coins(113), number=10000)
    print(find_min_coins(113), find_min_coins_time)  # Output: {1: 1, 2: 1, 10: 1, 50: 2} 0.6452214580003783
