"""

You are given a directed acyclic graph (DAG) that contains N nodes.

Write a function that can find all the possible paths from node 0 to node N - 1. You can return the path in any order.

graph[a] is a list of all nodes b for which the edge a -> b exists.

Example:
Graph illustration

Input: graph = [[1, 2],[3],[3],[4],[]]
Output: [[0,1,3,4], [0,2,3,4]]
Note: although you can print the different paths in any order, you should keep the order of nodes within one path in order.

[execution time limit] 4 seconds (py3)

[input] array.array.integer graph

[output] array.array.integer



"""

from collections import deque

def csFindAllPathsFromAToB(graph):
    stack = deque()
    stack.append((0, [0]))
    res = []
    destinationNode = len(graph) - 1

    while len(stack) > 0:
        curr = stack.pop()
        currNode, currPath = curr[0], curr[1]
        for neighbor in graph[currNode]:
            newPath = currPath.copy()
            newPath.append(neighbor)
            if neighbor == destinationNode:
                res.append(newPath)
            else:
                stack.append((neighbor, newPath))
    res.sort()
    return res