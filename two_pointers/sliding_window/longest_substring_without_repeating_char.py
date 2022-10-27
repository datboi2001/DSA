def longest_substring_without_repeating_characters(s: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(s)
    i = j = 0
    longest = 0
    window = set()

    while j < n:
        if s[j] not in window:
            window.add(s[j])
            j += 1
        else:
            window.remove(s[i])
            i += 1
        longest = max(longest, j - i)
    return longest


if __name__ == '__main__':
    s = input()
    res = longest_substring_without_repeating_characters(s)
    print(res)
