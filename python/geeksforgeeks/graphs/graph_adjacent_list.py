
from typing import Dict, List, Tuple
from collections.abc import Mapping, Sequence

class GraphNode:
  def __init__(self, value):
    self.value = value
    self.visited = False
    self.adjacent:[GraphNode] = []    

class Graph:
  def __init__(self):
    self.nodes: [GraphNode] = []
    self.weights:[[int]] = []

  def __init_weights__(self, v):
    self.vertixes = v
    # Using list comprehension instead of multiplying 
    # Because using mutiplier in 2d creates only one nested array that is referenced
    # in the other arrays
    # https://www.geeksforgeeks.org/python-which-is-faster-to-initialize-lists/
    #
    self.weights:[] = [[0 for i in range(v)] for j in range(v)]

  def addVertexes(self, nodes:[int])-> None:
    for i in nodes:
      self.nodes.append(GraphNode(i))
    self.__init_weights__(len(nodes))
  
  # TODO add aa type to edges
  def addEdges(self, edges:Dict[int, List[int]] ) -> None:
    for key, value in edges.items():
      source = self.nodes[key]
      for j in value:
        dest = self.nodes[j]
        source.adjacent.append(dest)
  
  def addEdgesWithWeights(self, edges:Dict[int, List[Tuple[int,int]]]) -> None:
    for key, value in edges.items():
      source = self.nodes[key]
      # add the adjacent vertex
      for nodeTuple in value:
        dest = self.nodes[nodeTuple[0]] # first element is the vertex
        source.adjacent.append(dest)
        weight = nodeTuple[1] # second element is the weight
        self.weights[key][nodeTuple[0]] = weight

  def reset(self):
    for n in self.nodes:
      n.visited = False