"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:
A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
"""


def countingValleys(steps, path):
    """
    We define the vallye as a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
    :param steps: number of steps on the hike
    :param path: an array describing the path. 'U' for uphill and 'D' for downhill
    :return: number of valleys walked through
    """
    # Write your code here
    # Main idea: if we are at sea level and we go down, we are in a valley
    # if we are at sea level and we go up, we are in a mountain
    # if we are in a valley and we go up, we are out of the valley
    # if we are in a mountain and we go down, we are out of the mountain
    # if we are in a valley and we go down, we are still in the valley

    # We start at sea level
    sea_level = 0
    # We start at the beginning of the path
    # We start with 0 valleys
    valleys = 0
    # We start with 0 mountains
    mountains = 0
    # We start with 0 steps
    step = 0

    while step < steps:
        if path[step] == 'U':
            sea_level += 1
            # if we are at sea level and we go up, we are in a mountain
            if sea_level == 0:
                valleys += 1
        else:
            # path[step] == 'D'
            sea_level -= 1
            # if we are at sea level and we go down, we are in a valley
            if sea_level == 0:
                mountains += 1
        step += 1

    return valleys

print(countingValleys(8, "UDDDUDUU"))
