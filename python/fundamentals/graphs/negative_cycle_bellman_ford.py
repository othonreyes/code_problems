from graph_common import *

maxint = 999999

def has_negative_cycle(graph:Graph):
  # STEP 1:  Create a vector of distance filled with infinite(maxint)
  dist = [maxint] * graph.V()
  # STEP 2: Set distance of source node to 0
  source_n = graph.nodes[0]
  dist[0] = 0

  # STEP 3: Calculate the distance for all nodes
  # If dist[v] > dist[u] + weight[u->v] Then
  #   dist[v] = dist[u] + weight[u->v]

  for i in range(graph.V()):
    n = graph.nodes[i]
    for ni in n.adjacent:
      u = n.value
      v = ni.value
      dist_u = dist[u]
      dist_v = dist[v]
      weight_uv = graph.weights[u][v]
      if dist_v > dist_u + weight_uv:
        dist_v = dist_u + weight_uv

  # STEP 4: Do it again
  # but if we need to update the dist_v then there is a negative cycle
  for i in range(graph.V()):
    n = graph.nodes[i]
    for ni in n.adjacent:
      u = n.value
      v = ni.value
      dist_u = dist[u]
      dist_v = dist[v]
      weight_uv = graph.weights[u][v]
      if dist_v > dist_u + weight_uv:
        return True
  return False


if __name__ == "__main__":
  graph = Graph()
  graph.addVertexes([0,1,2,3,4,5,6,7,8])
  graph.addEdgesWithWeights( \
    {1:[(2,4), (3,4)],
    2:[],
    3:[(6,-2), (5,4)],
    4:[(1,3), (3,2)],
    5:[(4,1), (7,-2)],
    6:[(2,3)],
    7:[(6,2), (8,-2)],
    8:[(5,-2)]
    })
  
  hnc = has_negative_cycle(graph)
  print(hnc)