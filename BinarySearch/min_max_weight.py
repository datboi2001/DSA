from typing import List

def min_max_weight(weights: List[int], d: int) -> int:
    """

    :param weights: A list of packages and their weights.
    :param d:The number of days to deliver all packages.
    :return: The minimum weight capacity of the truck
    """
    def truck_weight_is_feasible(weights: List[int], d: int, truck_weight: int):
        """

        :param weights: A list of packages and their weights
        :param d: The number of day to deliver all packages
        :param truck_weight: Truck capacity
        :return: a boolean that indicates if it's possible to ship the packages within d days
        given this truck weight
        """
        i = 0
        num_days = 1
        capacity = truck_weight
        while i < len(weights):
            if weights[i] <= capacity:
                capacity -= weights[i]
                i += 1
            else:
                num_days += 1
                capacity = truck_weight
        return num_days <= d

    left, right = max(weights), sum(weights)
    optimal_capacity = right
    while left <= right:
        mid = (left + right) // 2
        if truck_weight_is_feasible(weights, d, mid):
            optimal_capacity = mid
            right = mid - 1
        else:
            left = mid + 1
    return optimal_capacity



    return 0

if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    d = int(input())
    res = min_max_weight(weights, d)
    print(res)
