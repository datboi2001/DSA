from collections import deque

def bfs(root):
    queue = deque([root])
    visited = set([root])
    level = 0
    while len(queue) > 0:
        n = len(queue) # get # of nodes in the current level
        for _ in range(n):
            node = queue.popleft()
            for neighbor in get_neighbors(node):
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        # increment level after we have processed all nodes of the level
        level += 1