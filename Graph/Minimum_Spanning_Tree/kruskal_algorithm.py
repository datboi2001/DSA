from typing import List, Tuple


class UnionFind:
    def __init__(self):
        self.id = {}

    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)


class Edge:
    def __init__(self, weight, a, b):
        self.weight = weight
        self.a = a
        self.b = b


def cmp():
    def compare(x, y):
        return x.weight < y.weight

    return compare

# Kruskal algorithm
def minimum_spanning_tree(n: int, edges: List[edge]) -> int:
    # sort list, make sure to define custom comparator class cmp to sort edge based on weight from lowest to highest
    edges.sort(key=cmp)
    dsu = UnionFind()
    ret, cnt = 0, 0
    for edge in edges:
        # check if edges belong to same set before merging and adding edge to mst
        if dsu.find(edge.a) != dsu.find(edge.b):
            dsu.union(edge.a, edge.b)
            ret = ret + edge.weight
            cnt += 1
            if cnt == n - 1:
                break
    return ret
