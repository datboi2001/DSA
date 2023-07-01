

def turnStringLexicographically(s: str) -> str:
    """
    You are given a ternary string (it is a string which consists only of characters '0', '1' and '2').
You can swap any two adjacent (consecutive) characters '0' and '1' (i.e. replace "01" with "10" or vice versa)
or any two adjacent (consecutive) characters '1' and '2' (i.e. replace "12" with "21" or vice versa).
    Note than you cannot swap "02" → "20" and vice versa.
    You cannot perform any other operations with the given string excluding described above.
    You task is to obtain the minimum possible (lexicographically) string by using these
    swaps arbitrary number of times (possibly, zero).
    :param s: ternary string:
    :return: minimum possible (lexicographically) string
    """
    s: list[str] = list(s)
    # Main idea: we need to move all '2' to the end of the string
    # and all '0' to the beginning of the string
    # and all '1' will be in the middle of the string

    for i in range(len(s) -1):
        if s[i] == '2' and s[i+1] == '1':
            s[i], s[i+1] = s[i+1], s[i]
            break
    
    for i in range(len(s) -1, 0, -1):
        if s[i] == '0' and s[i-1] == '1':
            s[i], s[i-1] = s[i-1], s[i]
            break
    return ''.join(s)
string = input()
print(turnStringLexicographically(string))
