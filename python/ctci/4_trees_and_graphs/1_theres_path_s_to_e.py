from graph_common import *

maxint = 999999

"""

"""

def has_path(g, source, target):
  s = g.nodes[source]
  visited = create_visited(g)

  stack = [s]
  while stack:
    n = stack.pop()
    if n.value == target:
      return True
    visited[n.value] = True
    for ni in n.adjacent:
      if not visited[ni.value]:
        stack.append(ni)
  return False

### not tested
if __name__ == "__main__":
  graph = Graph()
  graph.addVertexes([0,1,2,3,4,5])
  graph.addEdges(
    {
    0:[3,4], 
    1:[2],
    2:[],
    3:[2],
    4:[],
    5:[4, 0]
    })
  print(has_path(graph, 0, 2))
  print(has_path(graph, 0, 1))
  
  