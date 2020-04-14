"""
Sort algorith using heap sort
Best: nlog(n)
Worst: nlog(n)
Average: nlog(n)
Space: O(1) git a
"""
import logging 
log = logging.getLogger('Console')
log.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.name = 'SystemOut'
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
log.addHandler(consoleHandler)

def heapsort(arr):
  n = len(arr)
  # first, build a max heap
  build_max_heap(arr, n)
  # Then, sort by swaping the max value with the smallest value
  # and then bubble up the max value
  for i in reversed(range(n)):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, i, 0)

def build_max_heap(arr, n):  
  # find the middle of the array
  start = n//2 - 1
  for i in reversed(range(start + 1)): # +1 becasue range end is exclusive
    # Then, bubble up the max value in the subtree until we reach the top
    heapify(arr, n, i)

def heapify(arr, n, i):
  l = i * 2 + 1  # left child of i
  r = i * 2 + 2 # left child of i
  largest = i 
  # if the left child is bigger than parent then largest is left
  if l < n and arr[l] > arr[largest]:
    largest = l
  # if the left child is bigger than largest i.e left or parent, then largest is right
  if r < n and arr[r] > arr[largest]:
    largest = r
  # if largest is not the parent
  if largest != i:
    # swap values
    arr[largest], arr[i] = arr[i], arr[largest]
    # repeat for process for the new parent
    heapify(arr, n, largest)

if __name__ == "__main__":
  items = [1,12,9,5,6,10, 13 ,8 ,59, 63, 45]
  log.info(items)
  heapsort(items)
  log.info(items)
