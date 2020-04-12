from graph_common import *

maxint = 999999

def minDistance(stpSet:[bool], dist:[int], g: Graph,):
  # Finds the vertex with the minimum distance not yet included in the
  # shortest path set
  min_dist = maxint
  min_index = -1
  for i in range(g.vertixes):    
    if not stpSet[i] and dist[i] < min_dist:
      min_dist = dist[i]
      min_index = i
  return min_index


def dijkstra(g: Graph, source: int):
  # 1. set the sShortest Path Set  to empty
  stpSet = [False] * g.vertixes
  # ...and set the distances to infinite
  dist = [maxint] * g.vertixes
  # set the distance to the source to 0
  dist[source] = 0

  # 2. travel all nodes:
  for c in range(g.vertixes):
    # 3. chose the node with the smallest distance that is not
    # in the shortest path
    u = minDistance(stpSet, dist, g)

    # 4. add the node to the shortest path
    stpSet[u] = True

    #Update the distance for the adjacent nodes of u only 
    # if the current distance is greater than 
    # (the u distance  + weighted distance of u-v )
    # AND the vertex is not in the shotest path tree 
    node_u = g.nodes[u]
    for node_v in node_u.adjacent:
      v = node_v.value
      if stpSet[v] == False and \
        dist[v] > dist[u] + g.weights[u][v]:
        dist[v] = dist[u] + g.weights[u][v]
  return dist

def print_distances(g:Graph, dist:[int])->None:
  print("Vertix\tDistance")
  for i in range(g.vertixes):
    print("{}\t{}".format(i, dist[i]))

if __name__ == "__main__":
  graph = Graph()
  graph.addVertexes([0,1,2,3,4,5,6,7,8])
  graph.addEdgesWithWeights({0:[(1,4), (7,8)], \
    1:[(2,8), (7,11)], \
    2:[(1,8), (3,7), (5,4), (8,2)], \
    3:[(2,7), (5,14), (4,9)], \
    4:[(3,9), (5,10)], \
    5:[(2,4), (3,14), (4,10), (6,2)], \
    6:[(5,2), (7,1), (8,6)], \
    7:[(0,8), (1,11), (6,1), (8,7)], \
    8:[(2,2), (6,6), (7,7)]
    })
  source = 0
  distances = dijkstra(graph, source)
  print_distances(graph, distances)