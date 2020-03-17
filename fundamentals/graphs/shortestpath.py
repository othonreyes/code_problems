"""
Graph data structure:


Opeartions:
- addNode
- addEdge
- removeNode
- removeEdger

"""
from graph_common import *

maxint = 999999


def visit(node:GraphNode):
  node.visited = True
  print("Node: {}".format(node.value))


def bfs_shortest_path(graph:Graph, source, target):
  n = len(graph.nodes)
  visited = [False] * n
  visited[source] = True
  queue = [graph.nodes[source]]
  parents = [None for n in range(n)] 
  while queue:
    n = queue.pop(0)
    for n1 in n.adjacent:      
      if not visited[n1.value]:
        parents[n1.value] = n.value
        visited[n1.value] = True
        queue.append(n1)
    if visited[target]:
      break

  path = [target]
  i = target
  while i!= source:
    path.append(parents[i])
    i = parents[i]
  print(" ",source,"->",target,"=",",".join([str(n) for n in path]))

def printParents(parents, source, target):
  path = []
  i = target
  while i!= source:
    path.append(i)
    i = parents[i]
  print(path)

if __name__ == "__main__":
  graph = Graph()
  graph.addVertexes([0,1,2,3,4,5, 6,7])
  graph.addEdges({0:[1,3], 1:[0,2], 2:[1], 3:[4,7], 4:[3,5,7], 5:[4,6], 7:[3,4,6]}) 
  source = 0
  target = 7
  bfs_shortest_path(graph, source, target)
