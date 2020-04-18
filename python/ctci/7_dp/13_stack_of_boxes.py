def stackOfBoxe(boxes):
  """
  didn't work becaseu the boxes are not sroted, that makes it difficult to handle the case
  where we want to test a given box but combined with the other boxes to the lift and the right
  of it so . if the box that we want to try is i then we want to check it with [0...i) + [i+1...n].
  It's hard becasue we need to to slice and concatenate the list which leads to a bad
  space complexity. 
  """
  # if i pass the initial box AND do a sublist then i can't iterate over all of them
  # return so(boxes[0], boxes[1:]) <-- can't do this
  if not boxes or len(boxes) == 0:
    return 0
  return so(boxes)

# To deal with the initialization problem I decided to use 2 methods
# one to iterate over the boxes and another to do the recursive calls
def so(boxes):
  height = 0
  for i in range(len(boxes)): 
    ## Can't do backtracking by removing and adding on a list
    # Remove it so we can search in a subset of boxes   
    # currentBox = boxes.pop(i) # this one eliminates entirely the element from the list    
    # temp_height = so2(currentBox, boxes)
    # boxes[i] = currentBox # add it back so backtracking
    
    # Instead, we weill pass the index that we are checking
    currentBox = boxes[i]
    temp_height = so_iteration(currentBox, i, boxes)
    height = max(temp_height, height)
  return height

def so_iteration(currentBox, i, boxes):
  if len(boxes) == i + 1:
    # return the heigth
    return boxes[i][1]
  curr_height = currentBox[1]
  for j in range(i + 1,len(boxes)): # start checking after i
    ## Can't do backtracking by removing and adding on a list
    # newBox = boxes.pop(i) # Remove it so we can search in a subset of boxes
    # temp_height = so2(newBox, boxes)
    # boxes[i] = newBox # add it back so backtracking

    newBox = boxes[j] # Remove it so we can search in a subset of boxes
    temp_height = so_iteration(newBox, j, boxes)

    if newBox[0] > currentBox[0] and \
      newBox[1] > currentBox[1]  and \
      newBox[2] > currentBox[2]:
        curr_height += temp_height
  return curr_height

### Atempt 2
from functools import cmp_to_key

def stackOfBoxes2(boxes):
  if not boxes or len(boxes) == 0:
    return 0
  #  [FIXME] sort it in ascending order
  def compare(box1, box2):
    return box1[1] - box2[1]
  boxes = sorted(boxes, key=cmp_to_key(compare))
  height = 0
  for i in range(len(boxes)):
    currentBox = boxes[i]
    temp_height = so_iteration2(currentBox, i, boxes)
    height = max(temp_height, height)
  return height

def so_iteration2(currentBox, i, boxes):
  if len(boxes) == i + 1:
    # return the heigth
    return boxes[i][1]
  # [FIXME] better to add the hieght at the end. Otherwise, the results will only
  # we need to include the height of the current box every time that we want to 
  # compare curr_height
  curr_height = 0
  for j in range(i + 1,len(boxes)): # start checking after i
    ## [FIXME] Can't do backtracking by removing and adding on a list
    # newBox = boxes.pop(i) # Remove it so we can search in a subset of boxes
    # temp_height = so2(newBox, boxes)
    # boxes[i] = newBox # add it back so backtracking

    newBox = boxes[j] # Remove it so we can search in a subset of boxes
    ## [FIXME] Doesn't makes sense to explore the box if we can't stack it
    # temp_height = so_iteration2(newBox, j, boxes)

    if newBox[0] > currentBox[0] and \
      newBox[1] > currentBox[1]  and \
      newBox[2] > currentBox[2]:
      temp_height = so_iteration2(newBox, j, boxes)
      ## [FIXME] the flaw here is that it's accumulating the resulting height of the box
      # if it is bigger regardless if it is the max height obtained from the 
      # recursive call from newBox
      # curr_height += temp_height
      curr_height = max(temp_height, curr_height)
  return curr_height +  currentBox[1]

### Atempt 3 - Using memoization
from functools import cmp_to_key

def stackOfBoxes3(boxes):
  if not boxes or len(boxes) == 0:
    return 0
  #  [FIXME] sort it in ascending order
  def compare(box1, box2):
    return box1[1] - box2[1]
  boxes = sorted(boxes, key=cmp_to_key(compare))

  n = len(boxes)
  height = 0
  mem = [0] * n
  for i in range(n):
    currentBox = boxes[i]
    temp_height = so_iteration3(currentBox, i, boxes, mem)
    height = max(temp_height, height)
  return height

def so_iteration3(currentBox, i, boxes, mem):
  if len(boxes) == i + 1:    
    return boxes[i][1]
  if mem[i] > 0:
    return mem[i]

  curr_height = 0
   # start checking after i
  for j in range(i + 1,len(boxes)):    
    newBox = boxes[j]
    if newBox[0] > currentBox[0] and \
      newBox[1] > currentBox[1]  and \
      newBox[2] > currentBox[2]:
      temp_height = so_iteration3(newBox, j, boxes, mem)
      curr_height = max(temp_height, curr_height)
  mem[i] = curr_height +  currentBox[1]
  return mem[i]

  
### Atempt 5 - Using memoization and simplified
from functools import cmp_to_key

def stackOfBoxes4(boxes):
  if not boxes or len(boxes) == 0:
    return 0
  #  [FIXME] sort it in ascending order
  def compare(box1, box2):
    return box1[1] - box2[1]
  boxes = sorted(boxes, key=cmp_to_key(compare))

  n = len(boxes)
  height = 0
  mem = [0] * n
  for i in range(n):
    ## [FIXME] no need to pass the current box as we are already passing
    # the whole list and the index of the current box
    # currentBox = boxes[i]
    # temp_height = so_iteration3(currentBox, i, boxes, mem)
    temp_height = so_iteration4( i, boxes, mem)
    height = max(temp_height, height)
  return height

def so_iteration4(i, boxes, mem):
  ## [FIXME] Not need to have this if for the base case as the for loop below
  # already prevents that we look at an index out of bounds
  # if len(boxes) == i + 1:    
  #   return boxes[i][1]
  if mem[i] > 0:
    return mem[i]

  currentBox = boxes[i]
  curr_height = 0
   # start checking after i
  for j in range(i + 1,len(boxes)):    
    newBox = boxes[j]
    if newBox[0] > currentBox[0] and \
      newBox[1] > currentBox[1]  and \
      newBox[2] > currentBox[2]:
      temp_height = so_iteration4(j, boxes, mem)
      curr_height = max(temp_height, curr_height)
  mem[i] = curr_height +  currentBox[1]
  return mem[i]

### Atempt 6 - Using memoization and using or not  a box
from functools import cmp_to_key

def stackOfBoxes5(boxes):
  if not boxes or len(boxes) == 0:
    return 0
  #  [FIXME] sort it in ascending order
  def compare(box1, box2):
    return box1[1] - box2[1]
  boxes = sorted(boxes, key=cmp_to_key(compare))

  mem = [0] * len(boxes)
  # note how we pass a null as initial box but we pass an index so we cna initialize it
  return so_iteration5(None, 0, boxes, mem)

def so_iteration5(currentBox, offset, boxes, mem):
  if offset  >= len(boxes): return 0
  
  newBox = boxes[offset]
  heightWithBox = 0
  # if we can use the box then explore 
  if not currentBox or newBox[0] > currentBox[0] and \
      newBox[1] > currentBox[1]  and \
      newBox[2] > currentBox[2]:
    # update the memoization if we haven't calculated the max height for this offset
    if mem[offset] == 0:      
      mem[offset] = so_iteration5(currentBox, 
        offset + 1,  # by increasing the offest, we can iterate over the boxes array
        boxes, 
        mem)
      # add the height of the box that we know it can be stacked
      mem[offset] += newBox[1]
    heightWithBox = mem[offset]
  # calculate the height without the current box
  heightWithputBox = so_iteration5(currentBox, 
        offset + 1,  # by increasing the offest, we can iterate over the boxes array
        boxes, 
        mem)

  return max(heightWithBox, heightWithputBox)

if __name__ == "__main__":
  boxes = [
    # w,h,d
    [1,1,1],
    [3,3,3],
    [2,2,2],
    [4,4,4]
  ]

  print(stackOfBoxe(boxes))
  print(stackOfBoxes2(boxes))
  print(stackOfBoxes3(boxes))
  print(stackOfBoxes4(boxes))
  print(stackOfBoxes5(boxes))