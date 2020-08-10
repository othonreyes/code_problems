# a global variable
my_var = "hello"

def greeting():
  print(my_var)   

def greeting2():
  # my_var = my_var * 2 # this fails because my_var is a global variable and to change it we need to declare it as global in the function
  global my_var
  my_var = my_var * 2
  print(my_var)

def non_local():
  x = "local"
  print("non_local {} time {}".format(1, x))
  def inner():
    nonlocal x
    x = "nonlocal"
    x = x * 2
    print("non_local {} time {}".format(2, x))

  inner()
  print("non_local {} time {}".format(3, x))



if __name__ == "__main__":
  double = lambda x: x * 2

  print(double(7))
  print(my_var)
  greeting()
  greeting2()
  print("3rd time {}".format(my_var))
  non_local()