"""
Count nodes within K-distance from all nodes in a set
https://www.geeksforgeeks.org/count-nodes-within-k-distance-from-all-nodes-in-a-set/
"""


from graph_adjacent_list import *

def nodes_k_distance(graph: GraphNode, k:int, marked_nodes:[int]) ->int:
  
  nodes_found = {}
  iter = 0
  for i in marked_nodes:
    node = graph.nodes[i]    
    node_set = set()
    node_set.add(node.value)
    
    find_nodes_k_distance(node, 0, k, node_set)
    
    nodes_found[str(i)] = node_set
    iter += 1
  
  similar_nodes = []
  g_len = len(graph.nodes)
  for i in range(g_len):
    valid = True
    for node_set in nodes_found.values(): # we could have use a list instead
      if i not in node_set:
        valid = False
        break
    if valid:
      similar_nodes.append(i)
  return len(similar_nodes)

def find_nodes_k_distance(node:GraphNode, current_distance:int, k:int, node_set)->None:
  if current_distance == k:
    # node_set.add(node.value)
    return
  for i in node.adjacent:
    if i.value not in node_set:
      node_set.add(i.value)
      find_nodes_k_distance(i, current_distance + 1, k, node_set)


if __name__ == "__main__":
  graph = Graph()
  graph.addVertexes([0,1,2,3,4,5,6,7,8,9])
  graph.addEdges({0:[1,3,8], 1:[0], 2:[3], 3:[0,2,5,6,7], 4:[5], \
   5:[3,4,9], 6:[3], 7:[3], 8:[0], 9:[5]})
  
  k = 3
  marked_nodes = [1,2,4]
  print(nodes_k_distance(graph, k, marked_nodes))
