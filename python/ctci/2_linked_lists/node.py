class Node:
  def __init__(self, data):
    self.data = data
    self.nxt = None

  def add(self, data):
    nxt = self
    while nxt.nxt is not None:
      nxt = nxt.nxt
    
    nxt.nxt = Node(data)
    return nxt.nxt
  
  def join(self, node):
    self.nxt = node

def get_size(n):
  count = 1
  while n.nxt is not None:
    count += 1
    n = n.nxt
  return count

  
def print_nodes(node, msg='--', separator='->'):
  r = ''
  while node is not None:
    r += str(node.data) + separator
    node = node.nxt
  if len(separator) > 0:
    print(msg, r[0:-1 * len(separator)])
  else:
    print(msg, r)

def print_node_mem(node, msg='--'):
  while node is not None:
    print(node, end='-')
    node = node.nxt


if __name__ == "__main__":
  head = Node(1)
  n2 = head.add(2)
  head.add(3)

  print_nodes(head)
  print_nodes(n2)
    