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

def mst_forest(trees : int, pairs : List[Tuple[int]]) -> int:
    # sort list, make sure to define custom comparator class cmp to sort edge based on weight from lowest to highest
    pairs.sort(key = lambda pair: pair[2])
    dsu = UnionFind()
    ret = 0
    for pair in pairs:
      # check if pairs belong to same set before merging and adding edge to mst
      if dsu.find(pair[0]) != dsu.find(pair[1]):
        dsu.union(pair[0], pair[1])
        ret += pair[2]
    return ret

if __name__ == '__main__':
    trees = int(input())
    pairs = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = mst_forest(trees, pairs)
    print(res)