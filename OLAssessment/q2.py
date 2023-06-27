def solution(A: list[int]):
    """
    Returns the length of the longest bi-valued (at most two different numbers)
    slice in given array A
    """
    # write your code in Python 3.6
    seen = set()
    cur_length = 0
    max_length = -float('inf')
    consec_seq_length = 1
    for i in range(len(A)):
        num = A[i]
        if num not in seen:
            if len(seen) < 2:
                cur_length += 1
                seen.add(num)
            else:
                max_length = max(max_length, cur_length)
                cur_length = consec_seq_length + 1
                seen = set([num, A[i-1]])
                consec_seq_length = 1
        else:
            cur_length += 1
            if num == A[i -1]:
                consec_seq_length += 1
            else:
                consec_seq_length = 1
    max_length = max(max_length, cur_length)
    return max_length

print(solution([0, 5, 5, 4, 5, 12]))