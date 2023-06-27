

def is_palindrome(s: str) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    i, j = 0, len(s) - 1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    s = input()
    res = is_palindrome(s)
    print('true' if res else 'false')
