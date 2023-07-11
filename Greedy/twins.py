min_num_coin = int(input())
coins = [int(x) for x in input().split()]
coins.sort(reverse=True)

# Main idea: To find the answer, we need to find the sum of the coins and divide it by 2.
# Then, we need to find the minimum number of coins that sum up to the sum of the coins divided by 2.
sum_coins = sum(coins)
sum_half = sum_coins // 2

sum_twin = 0
min_num_coin = 0
for coin in coins:
    if sum_twin <= sum_half:
        sum_twin += coin
        min_num_coin += 1
    else:
        break

print(min_num_coin)