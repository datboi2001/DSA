# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S: str) -> int:
    # write your code in Python 3.6
    S = S.lstrip("0")
    result = 0
    for c in reversed(S):
        if c == "0":
            result += 1
        else:
            result += 2
    return result - 1

print(solution("1" * (4 * 10 ** 5)))