from typing import Dict, List

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
  
  def reset(self):
    for n in self.nodes:
      n.visited = False