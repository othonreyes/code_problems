"""
Dijkstra’s Algorithm for Adjacency List Representation | Greedy Algo-8 | Minheap
https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/
"""

from graph_adjacent_list import *
from typing import Dict, List

maxint = 999999

# Heap methods
def find_len(dist:List[Tuple[int, int]], stp:List[bool]) -> int:
  n = len(dist)
  for i in range(len(dist)):
    if stp[i]:
      n = i
      break
  return n

def min_heap(dist:List[Tuple[int, int]], stp:List[bool], n:int):
  # n = find_len(dist, stp)
  start = n // 2 - 1
  for i in reversed(range(start + 1)):
    heapify(dist, n, i)

def heapify(dist:List[Tuple[int, int]], n:int, i:int):
  largest = i
  left = i * 2 +1
  right = i * 2 + 2
  if left < n and dist[left][1] < dist[largest][1]:
    largest = left
  if right < n and dist[right][1] < dist[largest][1]:
    largest = right
  if largest != i:
    # swap
    dist[largest], dist[i] = dist[i], dist[largest]
    heapify(dist, n, largest)

def extract_min(dist:List[Tuple[int, int]], stp:List[bool], n:int) -> int:
  # n = find_len(dist, stp)
  node_value = dist[0]
  dist[0] = dist[n - 1] # assign the highest value to the top
  # del dist[-1] no need to delete but add it to the end  
  heapify(dist, n - 1 , 0) # n-1 because we don't want to hipify the whole thing
  dist[n - 1] = node_value # add the extaracted tuple at the end
  return node_value

def find_distance(dist:List[Tuple[int, int]], index:int):
  for i in range(len(dist)):
    if dist[i][0] == index:
      return dist[i]
  return None

def update_dist(dist:List[Tuple[int, int]], index:int, distance:int):
  for i in range(len(dist)):
    if dist[i][0] == index:
      dist[i] = (index, distance)
      break
  

def dijkstra(g: Graph, source: int) -> List[Tuple[int, int]]:
  stp = [False] * g.vertixes
  dist = [(i, maxint) for i in range(g.vertixes)]
  update_dist(dist, source, 0)

  n = g.vertixes  
  for i  in range(len(g.nodes)):
    # get the node with the shortest distance
    min_heap(dist, stp, n)
    t_u = extract_min(dist, stp, n)
    stp[t_u[0]] = True

    #Update the distance if the adjacent nodes v is:
    # - not in the stp
    # - the distance of v > distance of u + weighted[u][v]
    node_u = g.nodes[t_u[0]]
    for v in node_u.adjacent:
      dist_v = find_distance(dist, v.value)
      dist_u = find_distance(dist, node_u.value)      
      if stp[v.value] == False and \
        dist_v[1] > dist_u[1] + g.weights[node_u.value][v.value]:
        new_distance = dist_u[1] + g.weights[node_u.value][v.value]
        update_dist(dist, v.value, new_distance)
    n -= 1
  return dist


def print_distances(g:Graph, dist:List[Tuple[int, int]])->None:
  print("Vertix\tDistance ", dist)
  for i in range(g.vertixes):
    print("{}\t{}".format(i, find_distance(dist, i)[1]))

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