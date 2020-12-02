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

def csFindAllPathsFromAToB(graph):
    
