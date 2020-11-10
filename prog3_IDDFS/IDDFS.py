# Python program to print DFS traversal from a given
# given graph
from collections import defaultdict


# This class represents a directed graph using adjacency
# list representation
class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A function to perform a Depth-Limited search

    # from given source 'src'
    def DLS(self, src, target, maxDepth):

        if src == target: return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0: return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            if (self.DLS(i, target, maxDepth - 1)):
                return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self, src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False


print("Iterative deepening depth first search")
n = int(input("Enter the number of vertices: "))
g = Graph(n);
e1 = 1
print("Enter the connecting vertices and -1 to stop")
while e1 != -1:
    e1 = int(input("add edge between: "))
    if e1 == -1:
        break
    e2 = int(input("and: "))
    g.addEdge(e1, e2)


target = int(input("Enter the target to search: "))
maxDepth = int(input("Enter the maximum depth: "))
src = 0

if g.IDDFS(src, target, maxDepth) == True:
    print("Target is reachable from source " +
          "within max depth")
else:
    print("Target is NOT reachable from source " +
          "within max depth")

'''
Output

Iterative deepening depth first search
Enter the number of vertices: 7
Enter the connecting vertices and -1 to stop
add edge between: 0
and: 1
add edge between: 0
and: 2
add edge between: 1
and: 3
add edge between: 1
and: 4
add edge between: 2
and: 5
add edge between: 2
and: 6
add edge between: -1
Enter the target to search: 6
Enter the maximum depth: 3
Target is reachable from source within max depth

Process finished with exit code 0


Iterative deepening depth first search
Enter the number of vertices: 4
Enter the connecting vertices and -1 to stop
add edge between: 0
and: 1
add edge between: 1
and: 2
add edge between: 2
and: 3
add edge between: -1
Enter the target to search: 3
Enter the maximum depth: 1
Target is NOT reachable from source within max depth
'''