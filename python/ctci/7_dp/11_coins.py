def coins(n) :
  m = [1,5,10,25]
  possibilities = set()
  count_ways(n,m, "", possibilities)
  print(possibilities)
  return len(possibilities)

# Doens't work becasue it doens't consider when we don't want to use a given coin
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
# Doens't work becasue it's tryng to aggregate all possible ways to give change even when they are repeated
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
  # We eventually reduce the number of possible coins to use
  #  to pennies so we might as well just calculate it
  if index == 0: 
    remaining = n % coin # Divide to avoid substracting which will take O(n) time. % will take O(1) time
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

m = [1,5,10,25]
# Works but is slow
# substracting takes O(n) time. % will take O(1) time
def coins4(n, index):
  if n == 0:
    return 1
  if n < 0 or index < 0:
    return 0
  coin = m[index]
  
  ways = 0
  for i in range(0,n +1,coin):
    ways += coins4(n - i, index - 1)
  return ways

def coins5(n, index):
  if n == 0:
    return 1
  if n < 0 or index < 0:
    return 0
  # works by considering if the coin is used or not.  
  return coins5(n, index - 1) + coins5(n - m[index], index)



if __name__ == "__main__":
  # print(coins(5))
  # print(coins(10))

  print(coins2(1))
  print(coins2(5))
  print(coins2(10))
  print('---')
  print(coins3(1))
  print(coins3(5))
  print(coins3(10))
  print('---')
  print(coins3_m(1))
  print(coins3_m(5))
  print(coins3_m(10))
  print('---')
  print(coins4(10, 3))
  print('---')
  print(coins5(10, 3))