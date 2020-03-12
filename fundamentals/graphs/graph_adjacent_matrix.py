import logging 

log = logging.getLogger('Console')
log.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.name = 'SystemOut'
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
log.addHandler(consoleHandler)

visited = [False] * 6
graph = [
    [0,1,0,0,1,1],
    [0,0,0,1,1,0],
    [0,1,0,0,0,0],
    [0,0,1,0,1,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    ]

def visit(i):
  log.info("Visiting {}".format(i))
  visited[i] = True

def dfs_recursive(graph):
  n = len(graph)
  for i in range(n):
    log.info("Checking node {}".format(i))
    if visited[i]:
      continue
    dfs_nodes(i, graph[i])

def dfs_nodes(index:int, nodes):
  visit(index)
  m = len(nodes)
  for j in range(m):
    if nodes[j] == 1 and not visited[j]:
      dfs_nodes(j, graph[j])

def bfs(graph:[[int]]):
  queue = [0]
  while queue:
    i = queue.pop(0)
    log.info("Checking node {}".format(i))
    if visited[i]:
      continue
    visit(i)
    for j in range(len(graph[i])):
      if graph[i][j] == 1 and not visited[j]:
        queue.append(j)        

def dfs_stack(graph):
  stack = [0]
  while stack:
    i = stack.pop()
    log.info("Checking {}".format(i))
    if visited[i]:
      continue
    visit(i)
    for j in range(len(graph[i])):
      if graph[i][j] == 1 and not visited[j]:
        stack.append(j)

if __name__ == "__main__":
  log.info("DFS recursive")
  dfs_recursive(graph) 
  
  log.info("BFS")
  visited = [False] * 6
  bfs(graph)
  
  log.info("DFS - Stack")
  visited = [False] * 6
  dfs_stack(graph)
