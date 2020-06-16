"""
https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/
We are given an array of n points in the plane, and the problem is to find out the closest pair of points in the array.
"""

# A divide and conquer program in Python3  
# to find the smallest distance from a  
# given set of points. 
import math 
  
# A class to represent a Point in 2D plane  
class Point(): 
  def __init__(self, x, y): 
    self.x = x 
    self.y = y 

def dist(p1, p2):
  return math.sqrt((p1.x-p2.x) * (p1.x-p2.x) + (p1.y - p2.y) * (p1.y - p2.y))

def closest_util(strip, n, d):
  min_dist = d
  # sort the nodes by a coordinate
  strip.sort(key = lambda point: point.y)

  for i in range(n):
    j = i + 1
    while j < n and ( strip[j].y - strip[i].y  < min_dist):
      min_dist = dist(strip[j], strip[i])
  return min_dist


def closest(points, n):
  if n<=3:
    min_val = float('inf')  
    for i in range(n):
      for j in range(i+1, n):
        min_val = min(min_val, dist(points[i], points[j]))
    return min_val

  # find the middle
  m = n//2
  # obtain the smaller distance of points between left and right
  dl = closest(P[:m], m)
  dr = closest(P[m:], n-m)
  # get the smallest distance between them
  d = min(dl, dr)
  
  strip = []
  # find all the points in the middle that might have a 
  # distance smaller than the new distance
  for i in range(n) :
    if dist(P[i], P[m]) < d:
      strip.append(P[i])
  # find the smaller distance between those points and
  # return the minimal distance
  return closest_util(strip, len(strip), d)


if __name__ == "__main__":
  P = [Point(2, 3), Point(12, 30), 
     Point(40, 50), Point(5, 1),  
     Point(12, 10), Point(3, 4)] 
  n = len(P)
  print("The smallest distance is",  
                    closest(P, n))   