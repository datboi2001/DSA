from typing import List


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    number_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }


    def dfs(path: List[str], result: List[str]):
        if len(path) == len(digits):
            result.append(''.join(path))
            return
        cur_number = digits[len(path)]
        for char in number_map[cur_number]:
            path.append(char)
            dfs(path, result)
            path.pop()

    result = []
    if digits:
        dfs([], result)
    return result

if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))
