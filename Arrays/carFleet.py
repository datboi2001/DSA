class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """
    There are n cars going to the same destination along a one-lane road. 
    The destination is target miles away.
    You are given two integer array position and speed, both of length n,
    where position[i] is the position of the ith car and speed[i] is the
    speed of the ith car (in miles per hour).
    A car can never pass another car ahead of it, but it can catch up to it
    and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).
    A car fleet is some non-empty set of cars driving at the same position and
    same speed. Note that a single car is also a car fleet.
    If a car catches up to a car fleet right at the destination point,
    it will still be considered as one car fleet.

    Return the number of car fleets that will arrive at the destination.
        :param target: int
        :param position: list[int]
        :param speed: list[int]
        :param return: int
        """
    # Main idea: Sort the cars by position. Iterate through the cars from the
    # back and calculate the time it takes for the car to reach the target.
    # If the time is greater than the previous car, then it is a new fleet.
    # If the time is less than the previous car, then it is not a new fleet.
        car_info = sorted(zip(position, speed), key=lambda x: x[0],  reverse=True)
        print(car_info)
        fleets = 0
        prev_time = 0
        for pos, car_speed in car_info:
            # Calculate the time it takes for the car to reach the target.
            time = (target - pos) / car_speed
            # If the time is greater than the previous car, then it is a new fleet because it will never catch up to the previous car.
            if time > prev_time:
                fleets += 1
                prev_time = time
        return fleets

print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))


