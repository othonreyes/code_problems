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
  for i in len(dist):
    if stp[i]:
      n = i
      break
  return n

def min_heap(dist:List[Tuple[int, int]], stp:List[bool]):
  n = find_len(dist, stp)
  start = n // 2 - 1
  for i in reversed(range(start + 1)):
    heapify(dist, n, i)

def heapify(dist:List[Tuple[int, int]], n:int, i:int):
  smallest = i
  left = i * 2 +1
  right = i * 2 + 2
  if left < n and dist[left] < dist[smallest]:
    left = smallest
  if right < n and dist[right] < dist[smallest]:
    right = smallest
  if smallest != i:
    # swap
    dist[smallest], dist[i] = dist[i], dist[smallest]
    heapify(dist, n, smallest, stp)

def extract_min(dist:[int], stp) -> int:
  n = len(dist)
  value = dist[0]
  dist[0] = dist[n - 1] # assign the highest value to the top
  del dist[-1]
  heapify(dist, n, 0, stp)
  return value

def dijkstra(g: Graph, source: int):
  stp = [False] * g.vertixes
  dist = [i, 1000) for i in range(5)]
  dist[source] = 0
  
  for i  in range(len(g.nodes)):
    # get the node with the shortest distance
    min_heap(dist, stp)
    u = extract_min(dist, stp)


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