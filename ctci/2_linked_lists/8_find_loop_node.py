from node import Node, print_nodes

def move_double(fast_pointer):
  if fast_pointer and fast_pointer.nxt and fast_pointer.nxt.nxt:
    return fast_pointer.nxt.nxt
  return None

def find_loop_node(n):
  assert n.nxt
  slow_pointer = n
  fast_pointer =  n.nxt
  collision_steps = 0

  while slow_pointer != fast_pointer:
    slow_pointer = slow_pointer.nxt
    fast_pointer = move_double(fast_pointer)
    if fast_pointer is None:
      return None
    collision_steps += 1
  
  slow_pointer = n
  fast_pointer = fast_pointer.nxt
  for _ in range(collision_steps-1):
    slow_pointer = slow_pointer.nxt
    fast_pointer = fast_pointer.nxt
  if slow_pointer != fast_pointer:
    return None
  return slow_pointer



if __name__ == "__main__":
  l1 = Node(1)
  l1.add(2)
  l1.add(3)
  l1.add(4)
  l1.add(5)
  l1.add(6)
  print_nodes(l1)
  find_loop_node(l1)
  print_nodes(find_loop_node(l1))

  l1 = Node(1)
  l1.add(2)
  inter = l1.add(3)
  l1.add(4)
  l1.add(5)
  last_node = l1.add(6)
  last_node.nxt = inter

  loop_node = find_loop_node(l1)
  print(inter, '-', loop_node)
  