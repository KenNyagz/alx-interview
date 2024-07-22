#!/usr/bin/python3
'''
Algo to calculate the least no of coins for a given figure from a specified
array of figures
'''


def makeChange(coins, amount):
    '''Algorithm to find the minimum number of coins(coins are
       given by `coins` array) for a given input (total)'''
    if amount == 0:
        return 0

    dp = [float('inf')] * (amount + 1)  # An arbitray value to be a placeholdr
    dp[0] = 0  # Base case: 0 coins are needed to make the amount 0

    # Iterate through each coin and update the dp list
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[amount] is still float('inf'), then it's not possible
    # to make that amount with the given coins
    return dp[amount] if dp[amount] != float('inf') else -1
