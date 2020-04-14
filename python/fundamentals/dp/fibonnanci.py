import time
def timer(fun):
    def wrapper(*args, **kwargs):
      start = time.time()
      value = fun(*args, **kwargs)
      print("Elapsed time: ", start - time.time(), "")
      return value
    return wrapper

@timer
def fibonnanci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibonnanci(n-1) + fibonnanci(n-2)

@timer
def fibo_memo(n, mem):
  """
  top-down approach
  """
  if n == 0:
    return 0
  if n == 1:
    return 1
  if mem[n] is not None:
    return mem[n]
  mem[n] = fibo_memo(n-1, mem) + fibo_memo(n-2, mem)
  return mem[n]

@timer
def fibo_bottom_up(n):
  mem = [None] * (n + 1)
  mem[0] = 0
  mem[1] = 1
  for i in range(2,n + 1):
    mem[i] = mem[i-1] + mem[i-2]
  
  return mem[n]


if __name__ == "__main__":
  n = 1
  print(n,"=",fibonnanci(n))
  n = 2
  print(n,"=",fibonnanci(n))
  n = 5
  print(n,"=",fibonnanci(n))

  n = 5
  mem = [None] * (n+1)
  print(n,"=",fibo_memo(n, mem))

  print(fibo_bottom_up(n))