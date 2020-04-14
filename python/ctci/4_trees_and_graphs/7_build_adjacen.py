from graph_common import * 

def build(graph:Graph): 
  deps = []
  added = [False] * len(graph.nodes)

  for i in range(len(graph.nodes)):
    error = resolve_dependencies(graph.nodes[i], deps, added)
    if error == -1:
      return "Projects have a cycle"

  return ".".join([str(c) for c in deps])

def resolve_dependencies(node:GraphNode, deps, added, visited = None):
  if visited is None:
    visited = set()
  if node.value in visited:
    return -1
  if added[node.value]:
    return
  visited.add(node.value)
  for n in node.adjacent:
    resolve_dependencies(n, deps, added, visited)
  deps.append(node.value)
  added[node.value] = True
  

if __name__ == "__main__":
  graph = Graph()
  #graph.addVertexes(["a","b","c","d", "e", "f"])
  #graph.addEdges({"a":["f"], "b":["f"], "c":["d"], "d":["a", "b"]})
  graph.addVertexes([0,1,2,3,4,5])
  graph.addEdges({0:[5], 1:[5], 2:[3], 3:[0, 1]})
  print(build(graph))
  