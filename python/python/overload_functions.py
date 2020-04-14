# https://www.codementor.io/@arpitbhayani/overload-functions-in-python-13e32ahzqt
from inspect import getfullargspec
import time

class Function(object):
  """
  Class that wraps a function. It can be callable by overriding the __call__ method.
  It wraps the function so it can be found in the Namespace.
  """

  def __init__(self, fn):
    self.fn = fn

  def __call__(self, *args, **kwargs):    
    # return self.fn(*args, **kwargs) -Before
    ## Finde the function
    fn = Namespace.get_instance().get(self.fn, *args) # Used to find the right function 
    if not fn:
      raise Exception("No matching function found")
    ## And execute it
    return fn(*args, **kwargs) # Execute the function
  
  def key(self, args=None):
    """
    Used to create an idnetifier for the function
    """
    if not args :
      args = getfullargspec(self.fn).args

    return tuple([
      self.fn.__module__,
      self.fn.__class__,
      self.fn.__name__,
      len(args or [])
    ])

class Namespace(object):
  """
  Singleton that Stores the overloaded functions.
  - can register a function using a decorator
  - get method used to retrieve a function based on the number of arguments.
  """
  __instance = None
  def __init__(self):
    if not self.__instance:
      self.function_map = dict()
      Namespace.__instance = self
    else:
      raise Exception("You can't instantiate this class twice")

  @staticmethod
  def get_instance():
    if not Namespace.__instance:
      Namespace()
    return Namespace.__instance
  
  def register(self, fun):
    function = Function(fun)
    self.function_map[function.key()] = fun
    return function

  def get(self,fn, *args):
    func = Function(fn)
    return self.function_map.get(func.key(args=args))

def overloaded(fn):
  """
  Decorator that registers an overloaded function
  """
  # Returns an instance of Function. The instance overrides __call__ function so it can
  # find the funciton in the Namespace and execute it.
  return Namespace.get_instance().register(fn) 

### Example
if __name__ == "__main__":
  def timer(fun):
    def wrapper(*args, **kwargs):
      start = time.time()
      value = fun(*args, **kwargs)
      print("Elapsed time: ", start - time.time(), "")
      return value
    return wrapper

  @overloaded
  def area(l , b):
    return l * b
  
  # fun = Function(area)
  # print(fun.key)
  # print(fun(3,4))

  # fun2 = Namespace.get_instance().register(area)
  # print(fun2(3,4))

  @overloaded
  def area(r):
    import math
    return math.pi * r ** 2
  
  print(area(3,4))
  print(area(3))