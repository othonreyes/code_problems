"""
https://www.geeksforgeeks.org/bidirectional-search/
Bidirectional Search

"""
from typing import Dict, List
from collections.abc import Mapping, Sequence
import logging 

log = logging.getLogger('Console')
log.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.name = 'SystemOut'
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
log.addHandler(consoleHandler)

class GraphNode:
  def __init__(self, value):
    self.value = value
    self.visited = False
    self.adjacent:[GraphNode] = []

class Graph:
  def __init__(self):
    self.nodes: [GraphNode] = []

  def addVertexes(self, nodes:[int])-> None:
    for i in nodes:
      self.nodes.append(GraphNode(i))
  
  # TODO add aa type to edges
  def addEdges(self, edges:Dict[int, List[int]] ) -> None:
    for key, value in edges.items():
      source = self.nodes[key]
      for j in value:
        dest = self.nodes[j]
        source.adjacent.append(dest)

def bfs(queue, parent, visited):
  node = queue.pop(0)
  for n in node.adjacent:
    if not visited[n.value]:
      parent[n.value] = node.value
      visited[n.value] = True
      queue.append(n)

def isIntersection(s_visited, t_visited):
  V = len(s_visited)
  for i in range(V):
    if s_visited[i] and t_visited[i]:
      return i
  return -1

def print_nodes(s_parent, t_parent, source, target, intersection):
  path = [intersection]
  i = intersection
  while i != source:
    path.append(s_parent[i])
    i = s_parent[i]
  
  path = path[::-1]

  i = intersection
  while i != target:
    path.append(t_parent[i])
    i = t_parent[i]
  
  print(",".join(path))


def bidirectional(graph:Graph, source:int, target:int):
  V = len(graph.nodes)
  s_queue = [graph.nodes[source]]
  s_visited = [False] * V
  s_parent = [None] * V
  s_visited[source] = True

  t_queue = [graph.nodes[target]]
  t_visited = [False] * V
  t_parent = [None] * V
  t_visited[target] = True
  

  while s_queue and t_parent:
    bfs(s_queue, s_parent, s_visited)
    bfs(t_queue, t_parent, t_visited)
    intersection = isIntersection(s_visited, t_visited)    
    if intersection:      
      # There is a result
      print_nodes(s_parent, t_parent, source, target, intersection)
      return
  print("No interseaction")




if __name__ == "__main__":
  graph = Graph()
  graph.addVertexes([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
  graph.addEdges({0:[4], 1:[4], 2:[5], 3:[5], 4:[0,1,6], 5:[2,3,6], \
    6:[4,5,7],7:[6,8],8:[7,9,10],9:[8,11,12],10:[8,13,14], \
    11:[9], 12:[9], 13:[10], 14:[10]})
  bidirectional(graph, 0, 14)