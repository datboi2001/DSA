# Time complexity O(n), space complexity is O(n)
def decode_ways(digits: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    dp = {}
    def dfs(i: int):
        if i in dp:
            return dp[i]
        if i == len(digits):
            return 1
        if digits[i] == "0":
            return 0
        res = dfs(i + 1)
        if 10 <= int(digits[i: i + 2]) <= 26:
            res += dfs(i + 2)
        dp[i] = res
        return res

    return dfs(0)


if __name__ == '__main__':
    digits = input()
    res = decode_ways(digits)
    print(res)
