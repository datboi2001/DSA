def find_message(s: str, a: list[int]) -> str:
    """
    We are playing a game. The game is simple. We are given a string s and a list of integers a.
    In the beginning, the 0th person uses the character s[0] and sends a message to a[0]-th person.
    When the kth-person receives the message, they append their letter s[k] to the message and send it to a[k]-th person. 
    The game ends when the message reaches the 0th person, Find the final message
    :param s: a string
    :param a: a list of integers
    :return: the final message
    """
    final_message = s[0]
    cur_receiver = a[0]
    while cur_receiver != 0:
        final_message += s[cur_receiver]
        cur_receiver = a[cur_receiver]
    return final_message

print(find_message("bytdag", [4,3,0,1,2,5]))
