from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
        :param numCourses: int
        :param prerequisites: list of prerequisites
        :return: if it is possible to finish all courses
                """
        # Main idea: Topological sort. We do a DFS on the graph and keep track of the nodes we have already visited.
        # If we encounter a node that we have already visited, we return False. If we have not visited a node, we
        # mark it as visited and add it to the stack. We also add the neighbors of the current node to the stack.
        # If we have visited all the nodes in the graph, we return True. If we have not visited all the nodes in the
        # graph, we return False.

        # Dictionary to keep track of the nodes we have already visited
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # Dictionary to keep track of the nodes we have already visited
        seen = {}
        # Stack to keep track of the nodes we have visited
        # Do a DFS on the graph
        def dfs(node):
            if node in seen:
                return False
            seen[node] = True
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True

print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))