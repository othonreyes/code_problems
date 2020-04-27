from graph_common import *

maxint = 999999
from functools import cmp_to_key

def sort_queue(q:List): 
  def comparator(o1,o2):
    # sort in ascending order by distance. Distance is in the `1`
    # position in the tuple
    return o1[1] - o2[1]
  return sorted(q, key=cmp_to_key(comparator))  

def dijkstra(graph:Graph, source):
  # Step 1: create a queue
  q = []
  # create a list to store the distances
  dist = [maxint] * len(graph.nodes)
  # Step 2: Assign zero distance to the source
  q.append((source, 0))
  dist[source] = 0

  # Step 3: have a set of visited nodes maybe
  # Step 4: iterate over all nodes? - Better do a BFS
  while q:    
    # Step 5: get the node with the smallest distance called node u
    q = sort_queue(q)
    node_u_ix, dist_u = q.pop(0)
    node_u = graph.nodes[node_u_ix]

    # Step 6: for all adjacent nodes
    for node_v in node_u.adjacent:
      dist_v = dist[node_v.value]
      #  If the adjacent node v is not visited and 
      #   dist[v] > dist[u] + weight[u][v]
      if dist_v > dist_u + graph.weights[node_u.value][node_v.value]:
        #   then update the dist[v] = dist[u] + weight[u][v]
        dist[node_v.value] = dist_u + graph.weights[node_u.value][node_v.value]
        #   add the node and the distance to the queue
        q.append((node_v.value, dist[node_v.value]))
    
  return dist  

def print_distances(g:Graph, dist:List[int])->None:
  print("Vertix\tDistance")
  for ix in range(len(dist)):
    print("{}\t{}".format(ix, dist[ix]))

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