# https://www.thecodeship.com/patterns/guide-to-python-function-decorators/
# functions are first class citizens
def greeting(name):
  return "hello " + name

greeter = greeting
print(greeter("Othon"))


# functions inside functions
def greet2(name):
  def get_message():
    return "Hello "
  return get_message() + name
print(greet2("Othon"))

# Functions can be passed as parameters to other functions
def greet3(name):
  return "hello " + name

def call_func(fun): # fun is a parameter
  name = "Othon"
  return fun(name) # passing parameters to the fun parameter

print(call_func(greet3)) # Passing fun as parameter to the fun that invoke the function

#Functions can return other functions
def compose_greet_func():
  def get_message():
    return "Hello there!"
  
  return get_message() # returnning the function 

print(compose_greet_func())

# Inner functions have access to the enclosing scope
def using_closure(name):
  def closure_func():
    return "Hello " + name # name can only be read and can be accessed outside the scope
  return closure_func

hi = using_closure
print(hi("babayaga")()) # Double parenthesis as hi returns a function

hi_with_params = using_closure("wawayaga")
print(hi_with_params()) # NO need of double parenthesis becasue the function was already has a parameter

# decorating a function to add html to a greeting function
def greeting_fun(name):
  return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorator(fun): # The function that wold be wrapped
  def add_p_tags(name): # name is the parameter of the wrapped fun
    return "<p>{0}</p>".format(fun(name)) # invoking the fun
  return add_p_tags # return the function that decorates the greeting message

p_decorated = p_decorator(greeting_fun) # p_decorated is add_p_tags
print(p_decorated("Tata"))

# we can even reassing the greeting function to have a more friendly way to use it
greeting_fun = p_decorator(greeting_fun) # p_decorated is add_p_tags
print(greeting_fun("Tata"))


### Using the decorator
def p_decorator2(fun):
  def add_p_tag(name):
    return "<p>{0}</p>".format(fun(name))
  return add_p_tag

@p_decorator2
def hi(name):
  return "Hello {0}".format(name)

print(hi("Tata"))

# Adding more decorators
def b_decorator2(fun):
  def add_p_tag(name):
    return "<b>{0}</b>".format(fun(name))
  return add_p_tag

def p_decorator3(fun):
  def add_p_tag(name):
    return "<p>{0}</p>".format(fun(name))
  return add_p_tag

@b_decorator2
@p_decorator3
def hi2(name):
  return "Hello {0}".format(name)

print(hi2("Tata"))


# Decorating a method
def p_self_decorator(fun):
  def func_wrapper(self):
    return "<p>{0}</p>".format(fun(self))
  return func_wrapper

class Person:
  def __init__(self):
    self.name = "John"
    self.last = "Doe"
  
  @p_self_decorator
  def get_name(self):
    return "{0} {1}".format(self.name, self.last)

person = Person()
print(person.get_name())

## Making the decxorator more generic by passing args and kwargs
def p_generic_decorator(fun):
  def func_wrapper(*args, **kwargs):
    return "<p2>{0}</p2>".format(fun(*args, **kwargs))
  return func_wrapper

class Person2:
  def __init__(self):
    self.name = "John"
    self.last = "Doe"
  
  @p_generic_decorator
  def get_name(self):
    return "{0} {1}".format(self.name, self.last)

person = Person2()
print(person.get_name())

# Pasing parameters to the decorators
def tag(tag):
  def tag_wrapper(fun):
    def func_wrapper(*args, **kwargs):
      return "<{0}>{1}</{0}>".format(tag,fun(*args, **kwargs))
    return func_wrapper
  return tag_wrapper

class Person3:
  def __init__(self):
    self.name = "John"
    self.last = "Doe"
  
  @tag("p")
  @tag("b")
  def get_name(self):
    return "{0} {1}".format(self.name, self.last)

person = Person3()
print(person.get_name())

