from typing import List
import bisect


def drink(shop_prices: List[int], coins: List[int]) -> List[int]:
    """
    :param shop_prices: an array containing prices of drink of all the shop
    :param coins: Number of coins on i-th day
    :return: A list of integers indicating how many shops you can buy a bottle of drink
    on the i-th day
    """
    shop_prices.sort()
    num_shops = []
    for coin in coins:
        num_shop = bisect.bisect_right(shop_prices, coin)
        num_shops.append(num_shop)
    return num_shops


n = int(input())
shop_prices = [int(i) for i in input().split()]
q = int(input())
coins = []
for _ in range(q):
    coin = int(input())
    coins.append(coin)
num_shops = drink(shop_prices, coins)
for shop in num_shops:
    print(shop)
