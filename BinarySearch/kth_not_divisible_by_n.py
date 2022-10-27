def solve(n: int, k: int):
    """
    Find kth number that is not divisible by n
    """
    

t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    print(solve(n,k))
