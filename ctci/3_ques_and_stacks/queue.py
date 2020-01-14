class Node:
  def __init__(self, data):
    self.data = data
    self.nxt = None

class Queue:
  """
  First in first out
  """
  def __init__(self):
    self.first = None
    self.last = None
  
  def add(self, data):
    if self.first is None:
      self.first = Node(data)
      self.last = self.first
    else:
      new = Node(data)
      self.last.nxt = new
      self.last = new
    return self.last
  
  def remove(self):
    assert self.first is not None
    data = self.first.data
    self.first = self.first.nxt
    return data
  
  def peek(self):
    assert self.first is not None
    return self.first.data
  
  def is_empty(self):
    return self.first is None

def print_queue(queue):
  r = []
  n = queue.first
  while n is not None:    
    r.append(str(n.data))
    n = n.nxt
  t = ''
  for i in reversed(r):
    t+=i+','
  print('[',t[:-1],']')



if __name__ == "__main__":
  queue = Queue()
  print('add:          ', queue.add(1))
  print('peek:         ', queue.peek())
  print('is_empty:     ', queue.is_empty())
  print('remove:       ', queue.remove())
  print('is_empty:     ', queue.is_empty())
  
  print('add:          ', queue.add(1))
  print('peek:         ', queue.peek())
  print('is_empty:     ', queue.is_empty())
  queue.add(2)
  queue.add(3)
  print_queue(queue)
  print('remove:       ', queue.remove())
  print('remove:       ', queue.remove())
  print('remove:       ', queue.remove())
  print('is_empty:     ', queue.is_empty())
  print_queue(queue)