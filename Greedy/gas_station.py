
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
        :param gas: gas[i] is the amount of gas at the ith station 
        :param cost: the cost of gas to travel from the ith station to the next station 
        :return: the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1
        """
        # Main idea: Greedy. We start at the first gas station and keep track of the amount of gas we have left. If we
        # run out of gas, we start at the next gas station.

        # Time complexity: O(n) where n is the number of gas stations
        # Space complexity: O(1)

        if len(gas) == 0:
            return -1
        
        # The amount of gas we have left
        gas_left = 0

        # The index of the gas station we start at
        start = 0

        # The total amount of gas we have left
        total_gas_left = 0

        for i in range(len(gas)):
            gas_left += gas[i] - cost[i]
            total_gas_left += gas[i] - cost[i]
            if gas_left < 0:
                start = i + 1
                gas_left = 0

        if total_gas_left < 0:
            return -1
        return start