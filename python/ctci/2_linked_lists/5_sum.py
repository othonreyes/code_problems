from node import Node, print_nodes
# Having 2 linked lists in reverse order, sum them and return a list
# 9-5-6 + 659
# 1-2-3   321
# 0-8-9 = 980

# option 1:
# iterate both lists
# get the node valus and sum them with the carry over 
# if the result is >= 10 then there is a carry over
# add the result to the new list
def get_value(n):
  if n is None:
    return 0
  return n.data

def get_nxt(n):
  if n is None:
    return None
  return n.nxt

def sum_lists(l1, l2):
  result = None

  carryover = 0
  while l1 is not None or l2 is not None:
    value = get_value(l1) + get_value(l2) + carryover
    carryover = value // 10
    if result is None:
      result = Node(value % 10)
    else:
      result.add(value % 10)
    l1 = get_nxt(l1)
    l2 = get_nxt(l2)
  
  if carryover == 1:
    result.add(carryover)

  return result

### Follow up:
"""
Now numbers are in normal order in a linked list like:
Input:
    4->2->3 = 423
    7->8->2 = 782
Output:
    1->2->0->5 = 1205
"""
class Result:
  def __init__(self, node = None, carryover=0):
    self.node = node
    self.carryover = carryover

def get_size(node):
  count = 1
  while node is None:
    node = node.nxt
    count += 1
  return count

def pad_with_zeros(node, zeros):
  for _ in range(zeros):
    new_node = Node(0)
    new_node.nxt = node
    node = new_node
  return node

def add_before_node(result_node, previous_node):
  if previous_node is None:
    return result_node
  result_node.nxt = previous_node
  return result_node

def sum_regular(n1, n2):
  """
    Input:
      4->2->3 = 423
      7->8->2 = 782
  Output:
      1->2->0->5 = 1205
  """
  if n1 is None and n2 is None:
    return Result() # Null object
  result = sum_regular(n1.nxt, n2.nxt)
  value = n1.data + n2.data + result.carryover
  carryover = value // 10
  result_node = Node(value % 10)
  result_node = add_before_node(result_node, result.node)
  return Result(result_node, carryover)

def sum_regular_lists(l1, l2):
  size_1 = get_size(l1)
  size_2 = get_size(l2)

  l1 = pad_with_zeros(l1, abs(size_1 - size_2))
  l2 = pad_with_zeros(l2, abs(size_1 - size_2))

  result = sum_regular(l1,l2)
  
  result_head = result.node
  if result.carryover > 0:
    new_node = Node(1)
    new_node.nxt = result_head
    result_head = new_node
  
  return result_head




if __name__ == "__main__":
  l1 = Node(9)
  l1.add(5)
  l1.add(6)

  l2 = Node(1)
  l2.add(2)
  l2.add(3)

  print_nodes(l1)
  print_nodes(l2)
  print_nodes(sum_lists(l1,l2))

  l2.add(4)
  print_nodes(sum_lists(l1,l2))

  l1.add(9)
  print_nodes(l1, separator='')
  print_nodes(l2, separator='')
  print_nodes(sum_lists(l1,l2), separator='')
  print_nodes(l1, '**',separator='')
  print_nodes(l2, '**',separator='')
  print_nodes(sum_regular_lists(l1,l2), '**',separator='')