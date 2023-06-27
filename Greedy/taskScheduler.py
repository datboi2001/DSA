import collections
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        :param tasks: list of tasks
        :param n: cooldown period between the two same tasks
        :return: The least number of intervals the CPU will take to finish all the given tasks.
        """
        # Greedy algorithm
        # The idea is to schedule the most frequent tasks first
        # The number of intervals is the sum of the number of tasks and the number of idle intervals
        
        # Count the number of tasks
        taskCount = list(collections.Counter(tasks).values())

        # Sort the tasks by the number of occurrences
        max_frequency = max(taskCount) 

        # The number of intervals is the sum of the number of tasks and the number of idle intervals
        intervals = 0

        # The number of tasks with the maximum number of occurrences
        max_frequency_task_count = taskCount.count(max_frequency)
        # The number of intervals is the sum of the number of tasks and the number of idle intervals
        intervals = (max_frequency - 1) * (n + 1) + max_frequency_task_count
        # If the number of intervals is less than the number of tasks, return the number of tasks
        return max(intervals, len(tasks))










print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
    