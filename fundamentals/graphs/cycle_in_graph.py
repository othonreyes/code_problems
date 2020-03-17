from graph_common import *

maxint = 999999

def has_cycle(g):
  source = g.nodes[0]
  n = len(g.nodes)
  visited = [None] * n
  return bsf_cycle(source, visited)

def bsf_cycle(n, visited):
  if visited[n.value]:
    return True
  visited[n.value] = True
  for i in n.adjacent:
    if visited[i.value] or bsf_cycle(i, visited):
      return True
  return False

if __name__ == "__main__":
  graph = Graph()
  graph.addVertexes([0,1,2,3])
  graph.addEdges({0:[1,2], 1:[2], 2:[0,3], 3:[3]})
  print(has_cycle(graph))

  graph = Graph()
  graph.addVertexes([0,1,2,3])
  graph.addEdges({0:[1,2], 1:[], 2:[3], 3:[]})
  print(has_cycle(graph))