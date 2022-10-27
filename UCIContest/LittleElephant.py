import math


def count_with_same_start_and_end(x):
    if (x < 10):
        return x
    tens = x // 10
    res = tens + 9

    num_digits = int(math.log10(x))
    first_digits = int(x / pow(10, num_digits))
    last_digit = x % 10
    if last_digit < first_digits:
        res -= 1
    return res

def sums_interval(l: int, r: int) -> int:
    return count_with_same_start_and_end(r) - count_with_same_start_and_end(l-1)

l, r = [int(x) for x in input().split()]
print(sums_interval(l, r))
