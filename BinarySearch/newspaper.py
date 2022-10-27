from typing import List
import sys
def newspapers_split(newspapers: List[int], coworkers: int) -> int:
    """
    :param newspapers: a list where newspapers[i] is the time it takes to read the ith newspaper
    :param coworkers: number of coworkers
    :return: the minimum time it takes to go read the newspapers
    """
    min_time, max_time = 0, sys.maxsize

    def feasible_split(possible_duration: int):
        """
        :param possible_duration: the minimum amount of time
        :return: If it's possible to for the coworkers to go through the newspapers in possible_duration minutes
        """
        total_time, num_split = 0, 0
        for num in newspapers:
            if num > possible_duration:
                return False
            if total_time + num > possible_duration:
                total_time = 0
                num_split += 1
            total_time += num
        if total_time != 0:
            num_split += 1
        return num_split <= coworkers

    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        if feasible_split(mid_time):
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1
    return max_time + 1

if __name__ == '__main__':
    newspapers = [int(x) for x in input().split()]
    coworkers = int(input())
    res = newspapers_split(newspapers, coworkers)
    print(res)
