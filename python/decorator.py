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
