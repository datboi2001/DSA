def jumpingOnClouds(c):
    """
    :param c: an array of cloud. 0 means it's safe, 1 means it must be avoided
    :return: the minimum number of jumps required, as an integer
    """
    # Write your code here
    num_jump = 0
    i = 0
    while i < len(c) - 1: 
        # At each step, we can jump 1 or 2 steps
        # We want to jump 2 steps if it's safe
        if i < len(c) - 2 and c[i + 2] == 0:
            num_jump += 1
            i += 2
        else:
            # We want to jump 1 step if it's safe
            num_jump += 1
            i += 1
    return num_jump

print(jumpingOnClouds([0, 0, 0, 1, 0,0]))