def square_root(n: int) -> int:
    """
    :param n: the number
    :return: the square root of the number
    """
    left, right = 0, n
    answer = None
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)