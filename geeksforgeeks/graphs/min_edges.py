"""
Minimum number of edges between two vertices of a Graph
https://www.geeksforgeeks.org/minimum-number-of-edges-between-two-vertices-of-a-graph/
"""

from graph_adjacent_list import *

def find_min_edges(graph, src, target):
  src_n = graph.nodes[src]
  return find_min_node_edges(src_n, set(), target)

def find_min_node_edges(n: GraphNode, path:set, target)->int:
  if n.value == target:
    return len(path)
  
  path.add(n.value)
  min_e = 999999
  for i in n.adjacent:
    if i.value in path:
      continue
    min_e = min(min_e, find_min_node_edges(i, path.copy(), target))
  return min_e


if __name__ == "__main__":
  graph = Graph()
  graph.addVertexes([0,1,2,3,4,5,6])
  graph.addEdges({0:[1,2,4], 1:[0,2], 2:[0,1,5], 3:[4], 4:[3,6], 5:[2], 6:[4]})
  
  src = 0
  target = 5 
  print(find_min_edges(graph, src, target))
