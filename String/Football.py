def football(player_str: str) -> str:
    """
    :param player_str: Binary representatation of the players
    :return: YES if the situation is dangerous, otherwise NO
    """
    for i in range(len(player_str)-6):
        if all(c == "1" for c in player_str[i:i+7]) or all(c == "0" for c in player_str[i:i+7]):
            return "YES"
    return "NO"


players = input()
print(football(players))