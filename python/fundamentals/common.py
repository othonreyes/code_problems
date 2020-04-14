import time

def timer(fun):
  def wrapper(*args, **kwargs):
    start = time.time()
    value = fun(*args, **kwargs)
    print("Elapsed time: ", start - time.time(), "")
    return value
  return wrapper
