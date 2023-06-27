#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    """
    Given an undirected weighted connected graph, find the Really Special SubTree in it.
    The Really Special SubTree is defined as a subgraph consisting of all the nodes in
    the graph and:

    There is only one exclusive path from a node to every other node.
    The subgraph is of minimum overall weight (sum of all edges) among all such subgraphs.
    No cycles are formed


    To create the Really Special SubTree, always pick the edge with smallest weight. Determine if including it will create a cycle. If so, ignore the edge. If there are edges of equal weight available:

Choose the edge that minimizes the sum u + v + wt  where u and v are vertices and wt
 is the edge weight.
If there is still a collision, choose any of them.
Print the overall weight of the tree formed using the rules.

    g_nodes: number of nodes
    g_from: list of source nodes
    g_to: list of destination nodes
    g_weight: list of weights
    :return: weight of the Really Special SubTree
    """     
    # List of edges
    roots = [-1] * g_nodes

    def find(n):
        if roots[n] < 0:
            return n
        else:
            res = find(roots[n])
            roots[n] = res
            return res
        
    def union(i, j):
        ri = find(i)
        rj = find(j)
        size1 = roots[ri] * -1
        size2 = roots[rj] * -1
        if size1 < size2:
            # bring ri into rj
            roots[ri] = rj
            roots[rj] = (size1 + size2) * -1
        else:
            roots[rj] = ri
            roots[ri] = (size1 + size2) * -1

    edges = []
    for i in range(len(g_from)):
        edges.append((g_from[i], g_to[i], g_weight[i]))
    edges.sort(key=lambda x: x[2])
    res = 0
    for start, to , weight in edges:
        if find(start - 1) != find(to - 1):
            union(start - 1, to - 1)
            res += weight
    return res
    



if __name__ == '__main__':

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    print(res)