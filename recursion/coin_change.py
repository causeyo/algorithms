# classic recursion
def rec_coin(target, coins):

    # DEFAULT VALUE SET TO TARGET
    min_coins = target

    # BASE CASE - CHECK TO SEE IF TARGET IS IN COIN VALUES LIST
    if target in coins:
        return 1

    else:

        # for every coin value that is <= my_target
        for i in [c for c in coins if c <= target]:

            # ADD A COIN COUNT + RECURSIVE CALL
            num_coins = 1 + rec_coin(target-i, coins)

            # RESET MINIMUM IF THE NEW NUM_COINS LESS THAN MIN COINS
            if num_coins < min_coins:

                min_coins = num_coins

    return min_coins


print(rec_coin(13, [1, 2,  5, 10]))
