def coins(n) :
  m = [1,5,10,25]
  possibilities = set()
  count_ways(n,m, "", possibilities)
  print(possibilities)
  return len(possibilities)

def count_ways(n,m, variation, possibilities):
  if variation in possibilities:
    return
  if n < 0:
    return
  if n == 0:
    possibilities.add(variation)
  
  for i in (m):
    count_ways(n - i, m, variation + str(i), possibilities)

def coins2(n):  
  m = set()
  count_ways2(n, m)
  print(m)
  return len(m)

def count_ways2(n, m):
  if n < 0:
    return 0
  if n == 0:
    return 1
  if n in m:
    return n
  v = count_ways2(n -1, m) + count_ways2(n - 5, m) + count_ways2(n - 10, m) + count_ways2(n - 25, m)
  m.add(v)
  return v

def coins3(n) :
  m = [1,5,10,25]    
  return count_ways3(n,m, len(m) - 1)

def count_ways3(n,m, index):
  coin = m[index]
  if index == 0:
    remaining = n % coin
    return 1 if remaining == 0 else 0
  
  ways = 0
  for i in range(0,n +1,coin):
    ways += count_ways3(n - i, m, index - 1)
  return ways

def coins3_m(n) :
  m = [1,5,10,25]
  mem = [[None for _ in range(n+1)] for _ in range(len(m))]
  return count_ways3_mem(n,m, len(m) - 1, mem)

def count_ways3_mem(n,m, index, mem):
  if mem[index][n]:
    return mem[index][n]
  coin = m[index]
  if index == 0:
    remaining = n % coin
    return 1 if remaining == 0 else 0
  
  ways = 0
  for i in range(0,n +1,coin):
    ways += count_ways3_mem(n - i, m, index - 1, mem)
  mem[index][n] = ways
  return ways



if __name__ == "__main__":
  # print(coins(5))
  # print(coins(10))

  # print(coins2(1))
  # print(coins2(5))
  # print(coins2(10))

  print(coins3(1))
  print(coins3(5))
  print(coins3(10))
  print(coins3_m(1))
  print(coins3_m(5))
  print(coins3_m(10))