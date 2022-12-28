from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
        :param numCourses: int
        :param prerequisites: list of prerequisites
        :return: The ordering of courses you should take to finish all courses
        """
        # Idea: DFS
        # Step 1: build the graph
        graph = defaultdict(list) 
        for i, j in prerequisites:
            graph[i].append(j)
        # Step 2: DFS
        # 2.1: if there is a cycle, return []
        # 2.2: if there is no cycle, return the topological order
        # Step 3: return the topological order
        visited = [0] * numCourses
        order = []
        def dfs(i):
            if visited[i] == 1:
                return True
            if visited[i] == -1:
                return False
            visited[i] = 1
            for j in graph[i]:
                if dfs(j):
                    return True
            visited[i] = -1
            order.append(i)
            return False
        for i in range(numCourses):
            if dfs(i) == True:
                return []
        return order

print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))