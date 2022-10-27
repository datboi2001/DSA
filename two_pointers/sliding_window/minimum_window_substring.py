from collections import Counter, defaultdict


def get_minimum_window(s: str, t: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    if t == "":
        return ""
    check_char = Counter(t)
    window = defaultdict(int)
    have, need = 0, len(check_char)
    res, res_len = [-1, -1], float("inf")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] += 1

        if c in check_char and window[c] == check_char[c]:
            have += 1

        # Move left pointers
        while have == need:
            # update our results
            cur_len = r - l + 1
            if cur_len < res_len:
                res = [l, r]
                res_len = cur_len
            elif cur_len == res_len and s[l:r + 1] < s[res[0]:res[1] + 1]:
                res = [l, r]

            window[s[l]] -= 1
            if s[l] in check_char and window[s[l]] < check_char[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r + 1] if res_len != float("inf") else ""


if __name__ == '__main__':
    original = input()
    check = input()
    res = get_minimum_window(original, check)
    print(res)
