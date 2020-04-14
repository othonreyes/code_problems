"""
Print all paths from a given source to a destination using BFS
https://www.geeksforgeeks.org/print-paths-given-source-destination-using-bfs/
"""

from graph_adjacent_list import *

def dfs_print_paths(graph: GraphNode, src, target):
  src_node = graph.nodes[src]
  if not src_node:
    return
  find_paths(src_node, target, str(src_node.value))

def find_paths(node:GraphNode, target: int, visited:str) ->None:
  for i in node.adjacent:
    if i.value == target:
      print("{},{}".format(visited, str(i.value)))
      return
    find_paths(i, target, "{},{}".format(visited, str(i.value)))

def bfs_print_paths(graph: GraphNode, src, target):
  src_node = graph.nodes[src]
  if not src_node:
    return
  queue = [[src_node]] # needs to be a queue of lists to store the paths
  while queue:
    path = queue.pop()
    n = len(path)
    last = path[n-1]
    if last.value == target:
      print(",".join([str(x.value) for x in path ]))
      continue
    for i in last.adjacent:
      newpath = path.copy()
      newpath.append(i)
      queue.append(newpath) 


if __name__ == "__main__":
  graph = Graph()
  graph.addVertexes([0,1,2,3])
  graph.addEdges({0:[1,3], 1:[3], 2:[0,1], 3:[]})
  
  src = 2
  target = 3
  dfs_print_paths(graph, src, target)
  print()
  bfs_print_paths(graph, src, target)
