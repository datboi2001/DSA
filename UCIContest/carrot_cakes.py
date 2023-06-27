from math import ceil


def carrot_cakes(n, t, k, d):
    # One oven
    num_loads = ceil(n / k)
    one_oven_duration = num_loads * t

    num_loads_before_second = d // t
    cakes_before_second = num_loads_before_second * k
    num_cakes_left = n - cakes_before_second
    num_remainin_loads = ceil(num_cakes_left / (2*k))
    two_oven_duration = num_remainin_loads * t + d

    if (one_oven_duration <= two_oven_duration):
        return "NO"
    else:
        return "YES"


n, t, k, d = [int(x) for x in input().split()]
print(carrot_cakes(n, t, k, d))
