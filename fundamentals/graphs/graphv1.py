"""
Graph data structure:


Opeartions:
- addNode
- addEdge
- removeNode
- removeEdger

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
  
  def reset(self):
    for n in self.nodes:
      n.visited = False

def dfs_graph_recursive(graph:Graph):
  for i in graph.nodes:
    dfs_node_recursive(i)

def dfs_node_recursive(node:GraphNode, source:GraphNode = None):
  val = None if not source else source.value
  log.info("From {} ->DFSing: {}".format(val, node.value))
  if node.visited:
    return
  visit(node)
  for n in node.adjacent:
    if not n.visited:
      dfs_node_recursive(n, node)

def dfs_graph_stack(graph:Graph):
  stack = [graph.nodes[0]]
  while stack:
    n = stack.pop()
    log.info("->DFSing: {}".format(n.value))
    visit(n)
    for n1 in n.adjacent:
      if not n1.visited:
        stack.append(n1)

def visit(node:GraphNode):
  node.visited = True
  log.info("Node: {}".format(node.value))


def bfs(graph:Graph):
  queue = [graph.nodes[0]]
  while queue:    
    n = queue.pop(0)
    if n.visited:
      continue
    log.info("->BFSing: {}".format(n.value))
    visit(n)
    for n1 in n.adjacent:
      if not n1.visited:
        queue.append(n1)

if __name__ == "__main__":
  graph = Graph()
  graph.addVertexes([0,1,2,3,4,5])
  graph.addEdges({0:[1,4,5], 1:[3,4], 2:[1], 3:[2,4]})
  dfs_graph_recursive(graph)
  graph.reset()
  log.info("." *10)
  dfs_graph_stack(graph)
  graph.reset()
  log.info("." *10)  
  bfs(graph)
